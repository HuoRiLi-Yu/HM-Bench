import os
import time
from tqdm import tqdm
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import Config
from prompt_builder import build_mcq_prompt
from api_client import OpenAIImageQAClient
from parser import parse_mcq_answer
from evaluator import evaluate_predictions
from io_utils import ensure_dir, load_json, save_json, append_jsonl, load_jsonl, save_csv

def resolve_image_path(image_path):
    if os.path.isabs(image_path):
        return image_path
    return os.path.join(Config.PROJECT_ROOT, image_path)

def normalize_samples(data):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "data" in data:
        return data["data"]
    raise ValueError("QA JSON format must be a list or a dict with key 'data'.")


def build_existing_item_ids(existing_records):
    item_ids = set()
    for r in existing_records:
        if "item_id" in r:
            item_ids.add(r["item_id"])
    return item_ids

def extract_image_paths(sample, project_root):
    """
    【内部辅助函数】智能提取图片路径列表
    兼容两种格式：
    1. 单图: {"image_path": "xxx.png"}
    2. 多图: {"image1": "xxx.png", "image2": "yyy.png", ...}
    
    返回: list of absolute paths (例如: ['/root/xxx.png', '/root/yyy.png'])
    """
    paths = []
    
    # 情况 A: 标准单图字段 'image_path'
    if "image_path" in sample:
        val = sample["image_path"]
        if isinstance(val, str):
            paths = [val]
        elif isinstance(val, list):
            paths = val
        else:
            raise ValueError(f"Invalid type for image_path: {type(val)}")
            
    # 情况 B: 分离的 'image1', 'image2', 'image3'... 字段
    else:
        idx = 1
        while True:
            key = f"image{idx}"
            if key in sample:
                paths.append(sample[key])
                idx += 1
            else:
                break
        
        if not paths:
            # 如果既没有 image_path 也没有 image1，报错
            raise ValueError(f"No image path found in sample item_id={sample.get('item_id')}")

    # 统一转换为绝对路径
    resolved_paths = []
    for p in paths:
        if os.path.isabs(p):
            resolved_paths.append(p)
        else:
            resolved_paths.append(os.path.join(project_root, p))
            
    return resolved_paths

def extract_text_report_paths(sample, project_root):
    """
    【内部辅助函数】智能提取文本报告路径列表
    兼容两种格式：
    1. 单报告: {"image_path": "xxx.txt"}
    2. 多报告: {"image_path": ["a.txt", "b.txt"]} 
       或 {"image1": "a.txt", "image2": "b.txt", ...}
    
    返回: list of absolute paths (例如: ['/root/a.txt', '/root/b.txt'])
    """
    paths = []
    
    # 情况 A: 标准字段 'image_path'
    if "image_path" in sample:
        val = sample["image_path"]
        if isinstance(val, str):
            if not val.lower().endswith('.txt'):
                raise ValueError(f"Expected .txt file, got: {val}")
            paths = [val]
        elif isinstance(val, list):
            for p in val:
                if not isinstance(p, str) or not p.lower().endswith('.txt'):
                    raise ValueError(f"All items in image_path list must be .txt files. Invalid: {p}")
            paths = val
        else:
            raise ValueError(f"Invalid type for image_path: {type(val)}")
            
    # 情况 B: 分离的 'image1', 'image2', ... 字段
    else:
        idx = 1
        while True:
            key = f"image{idx}"
            if key in sample:
                p = sample[key]
                if not isinstance(p, str) or not p.lower().endswith('.txt'):
                    raise ValueError(f"Field {key} must be a .txt path. Got: {p}")
                paths.append(p)
                idx += 1
            else:
                break
        
        if not paths:
            raise ValueError(f"No report path found in sample item_id={sample.get('item_id')}")

    # 转绝对路径
    resolved_paths = []
    for p in paths:
        if os.path.isabs(p):
            resolved_paths.append(p)
        else:
            resolved_paths.append(os.path.join(project_root, p))
            
    return resolved_paths


def process_single_sample(sample, client, existing_item_ids):
    item_id = sample.get("item_id")
    if Config.SKIP_EXISTING and item_id in existing_item_ids:
        return None, None

    # === 判断模式：检查是否存在 image_path 且是否为 .txt ===
    mode = None
    image_paths = []      # 用于图像模式
    report_paths = []     # 用于文本模式
    report_contents = []  # 合并后的文本内容

    try:
        # 尝试提取路径（先看是不是文本）
        raw_val = sample.get("image_path") or sample.get("image1")
        if raw_val is None:
            raise ValueError("No image_path or image1 found.")

        # 判断是否为文本模式：只要第一个路径是 .txt 就算
        first_path = raw_val if isinstance(raw_val, str) else raw_val[0] if isinstance(raw_val, list) else sample.get("image1")
        if isinstance(first_path, str) and first_path.lower().endswith('.txt'):
            mode = "text"
            report_paths = extract_text_report_paths(sample, Config.PROJECT_ROOT)
            # 读取所有报告内容并拼接
            contents = []
            for rp in report_paths:
                if not os.path.exists(rp):
                    raise FileNotFoundError(f"Report not found: {rp}")
                with open(rp, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if len(content) > 3000:
                        content = content[:3000] + " [TRUNCATED]"
                    contents.append(f"--- Report File: {os.path.basename(rp)} ---\n{content}")
            report_contents = "\n\n".join(contents)
        else:
            mode = "image"
            image_paths = extract_image_paths(sample, Config.PROJECT_ROOT)
            missing = [p for p in image_paths if not os.path.exists(p)]
            if missing:
                raise FileNotFoundError(f"Missing images: {missing}")

    except Exception as e:
        base_record = {
            "item_id": item_id,
            "block_id": sample.get("block_id"),
            "dataset": sample.get("dataset"),
            "task_type": sample.get("task_type"),
            "level1_id": sample.get("level1_id"),
            "level2_id": sample.get("level2_id"),
            "level3_id": sample.get("level3_id"),
            "question": sample.get("question", ""),
            "options": sample.get("options", {}),
            "num_options": len(sample.get("options", [])),
            "gt_answer": str(sample.get("answer", "")).strip().upper(),
            "mode": "unknown",
            "error": f"input_load_failed: {str(e)}"
        }
        return base_record, base_record

    # === 构建基础记录 ===
    base_record = {
        "item_id": item_id,
        "block_id": sample.get("block_id"),
        "dataset": sample.get("dataset"),
        "task_type": sample.get("task_type"),
        "level1_id": sample.get("level1_id"),
        "level2_id": sample.get("level2_id"),
        "level3_id": sample.get("level3_id"),
        "question": sample["question"],
        "options": sample["options"],
        "num_options": len(sample["options"]),
        "gt_answer": str(sample["answer"]).strip().upper(),
        "mode": mode,
    }

    if mode == "image":
        base_record["image_path"] = image_paths
        base_record["num_images"] = len(image_paths)
    else:
        base_record["report_paths"] = report_paths  # 存所有报告路径
        base_record["num_reports"] = len(report_paths)

    # === 构建 Prompt ===
    prompt, valid_letters = build_mcq_prompt(
        sample, 
        report_content=report_contents if mode == "text" else None
    )

    # === 调用 API ===
    raw_result = None
    last_error = None
    for _ in range(Config.RETRY_TIMES):
        try:
            if mode == "image":
                raw_result = client.infer(image_paths, prompt)
            else:
                raw_result = client.infer([], prompt)  # 纯文本：空图列表
            break
        except Exception as e:
            last_error = str(e)
            time.sleep(Config.SLEEP_ON_ERROR)

    if raw_result is None:
        record = {
            **base_record,
            "parsed_answer": None,
            "is_correct": False,
            "raw_response": None,
            "latency": None,
            "usage": None,
            "error": f"api_failed: {last_error}"
        }
        return record, record

    parsed_answer = parse_mcq_answer(raw_result["raw_text"], valid_letters)
    gt_answer = str(sample["answer"]).strip().upper()
    is_correct = parsed_answer == gt_answer

    record = {
        **base_record,
        "gt_answer": gt_answer,
        "parsed_answer": parsed_answer,
        "is_correct": is_correct,
        "raw_response": raw_result["raw_text"],
        "latency": raw_result.get("latency"),
        "usage": raw_result.get("usage"),
        "error": None if parsed_answer is not None else "parse_failed"
    }

    error_rec = record if record["error"] is not None else None
    return record, error_rec


def run_single_task(qa_json_path: str):
    """
    运行单个任务的评估流程，并将结果保存到统一输出目录：
    /data1/zhangxinyu/Final-Project/outputs/GPT-5.4-mini/image/task1, task2, ...
    """
    # === 1. 从 qa_json_path 提取原始 task 名称（如 "task_1"）===
    task_dir_name = os.path.basename(os.path.dirname(qa_json_path))  # e.g., "task_1"
    
    # === 2. 转换为输出目录名（如 "task1"）===
    if task_dir_name.startswith("task_") and task_dir_name[5:].isdigit():
        task_num = task_dir_name[5:]  # "1", "2", ..., "13"
        output_task_name = f"task{task_num}"  # "task1", "task2", ...
    else:
        # 如果不符合 task_X 格式，保留原名（兼容性）
        output_task_name = task_dir_name.replace("_", "").replace("-", "")

    # === 3. 构建统一输出根目录和子目录 ===
    model_output_root = "/data1/zhangxinyu/Final-Project/outputs/llava-1.5-7b/image"  # 统一输出根目录，按模型分子目录
    output_task_dir = os.path.join(model_output_root, output_task_name)
    ensure_dir(output_task_dir)  # 确保目录存在

    # === 4. 定义输出文件路径（全部指向新目录）===
    pred_jsonl = os.path.join(output_task_dir, "predictions.jsonl")
    pred_csv = os.path.join(output_task_dir, "predictions.csv")
    summary_json = os.path.join(output_task_dir, "summary.json")
    error_json = os.path.join(output_task_dir, "error_cases.json")

    # === 5. 加载数据（保持不变）===
    data = load_json(qa_json_path)
    samples = normalize_samples(data)

    if Config.MAX_SAMPLES > 0:
        samples = samples[:Config.MAX_SAMPLES]

    existing_records = load_jsonl(pred_jsonl) if Config.SKIP_EXISTING else []
    existing_item_ids = build_existing_item_ids(existing_records)

    base_url = Config.get_base_urls()
    print("DEBUG: base_urls =", base_url)
    client = OpenAIImageQAClient(
        api_key=Config.OPENAI_API_KEY,
        base_url=base_url,
        model_name=Config.MODEL_NAME,
        system_prompt=Config.SYSTEM_PROMPT,
        temperature=Config.TEMPERATURE,
        max_tokens=Config.MAX_TOKENS,
        timeout=Config.TIMEOUT
    )

    new_records = []
    results_queue = []
    MAX_WORKERS = 16

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(process_single_sample, sample, client, existing_item_ids)
            for sample in samples
        ]

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc=f"{output_task_name} | Model {os.path.basename(Config.MODEL_NAME)}",
            unit="it",
            mininterval=0.5,
            ncols=120
        ):
            try:
                record, error_rec = future.result()
            except Exception as e:
                tqdm.write(f"⚠️ Task failed: {e}")
                continue

            if record is None:
                continue

            new_records.append(record)
            results_queue.append(record)
            if len(results_queue) >= 50:
                lines = [json.dumps(r, ensure_ascii=False) + '\n' for r in results_queue]
                with open(pred_jsonl, 'a', encoding='utf-8') as f:
                    f.writelines(lines)
                results_queue = []

    if results_queue:
        lines = [json.dumps(r, ensure_ascii=False) + '\n' for r in results_queue]
        with open(pred_jsonl, 'a', encoding='utf-8') as f:
            f.writelines(lines)

    all_records = existing_records + new_records
    summary = evaluate_predictions(all_records)
    summary.update({
        "model_name": Config.MODEL_NAME,
        "qa_json_path": qa_json_path,
        "skip_existing": Config.SKIP_EXISTING,
        "evaluated_records": len(all_records),
        "newly_added_records": len(new_records)
    })

    all_error_cases = [r for r in all_records if r.get("error") is not None]

    # ✅ 保存到新输出目录
    save_json(summary, summary_json)
    save_json(all_error_cases, error_json)
    save_csv(all_records, pred_csv)

    print(f"\n✅ {output_task_name} | Acc: {summary['overall_accuracy']:.4f} | Valid: {summary['valid_rate']:.4f}")

def run_multiple_tasks():
    """批量运行 task_1 到 task_13"""
    base_data_dir = "/data1/zhangxinyu/Final-Project/data/QA_Final"  # 根数据目录，下面有 task_1, task_2, ..., task_13 子目录
    task_dirs = [f"task_{i}" for i in range(1,14)]  # 这里改为 1-13，兼容所有任务

    for task_name in task_dirs:
        qa_path = os.path.join(base_data_dir, task_name, "mcq_only.json")
        if not os.path.exists(qa_path):
            print(f"⚠️ Skipping {task_name}: {qa_path} not found")
            continue

        print(f"\n🚀 Starting evaluation for {task_name}...")
        run_single_task(qa_path)

    print("\n🎉 All tasks completed!")



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate MCQ on hyperspectral QA tasks")
    parser.add_argument("--single", type=str, help="Path to a single mcq_only.json file")
    parser.add_argument("--multi", action="store_true", help="Run tasks 1 to 13")
    args = parser.parse_args()

    if args.single:
        run_single_task(args.single)
    elif args.multi:
        run_multiple_tasks()
    else:
        # 默认行为：保持原样（兼容旧用法）
        # 但注意：原 Config.QA_JSON_PATH 必须有效
        run_single_task(Config.QA_JSON_PATH)