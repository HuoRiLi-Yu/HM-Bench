import os
from dotenv import load_dotenv
from typing import List, Union
load_dotenv()

class Config:
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # ========= API =========
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    #OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1" )
    # ✅ 核心修改：支持读取多个 Base URL (用逗号分隔)
    # 例如: OPENAI_BASE_URLS="http://localhost:8000/v1,http://localhost:8001/v1,http://localhost:8002/v1"
    # 如果只配了一个，代码会自动转为列表，兼容旧版
    #_raw_base_urls = os.getenv("OPENAI_BASE_URLS", os.getenv("OPENAI_BASE_URL", "https://jeniya.cn/v1"))
    _raw_base_urls = os.getenv("OPENAI_BASE_URLS", os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1,http://localhost:8002/v1,http://localhost:8003/v1"))
    # 处理字符串分割，去除空格，生成列表
    if isinstance(_raw_base_urls, str):
        OPENAI_BASE_URLS: List[str] = [url.strip() for url in _raw_base_urls.split(",") if url.strip()]
    else:
        OPENAI_BASE_URLS: List[str] = [_raw_base_urls]
    MODEL_NAME = os.getenv("MODEL_NAME", "/data1/zhangxinyu/HSI/llava-1.5-7b-hf")

    # ========= DATA =========
    # QA_JSON_PATH_ROOT = os.getenv("QA_JSON_PATH_ROOT", "/data1/zhangxinyu/Final-Project/data/QA_for_text/task_6")
    # QA_JSON_PATH = os.getenv("QA_JSON_PATH", "/data1/zhangxinyu/Final-Project/data/QA_for_text/task_6/mcq_only.json")

    # ========= OUTPUT =========
    ROOT_OUTPUT_DIR = os.getenv("ROOT_OUTPUT_DIR", "Final-Project/outputs")
    MODEL_OUTPUT_DIR = os.path.join(ROOT_OUTPUT_DIR, MODEL_NAME)

    # PRED_JSONL = os.path.join(QA_JSON_PATH_ROOT, "predictions.jsonl")
    # PRED_CSV = os.path.join(QA_JSON_PATH_ROOT, "predictions.csv")
    # SUMMARY_JSON = os.path.join(QA_JSON_PATH_ROOT, "summary.json")
    # ERROR_JSON = os.path.join(QA_JSON_PATH_ROOT , "error_cases.json")

    # ========= RUN =========
    MAX_SAMPLES = int(os.getenv("MAX_SAMPLES", "0"))   # 0表示全量
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "64"))
    RETRY_TIMES = int(os.getenv("RETRY_TIMES", "3"))
    SLEEP_ON_ERROR = float(os.getenv("SLEEP_ON_ERROR", "1"))
    SKIP_EXISTING = os.getenv("SKIP_EXISTING", "true").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "120"))
    # ========= PROMPT =========
    SYSTEM_PROMPT = os.getenv(
        "SYSTEM_PROMPT",
            (
        "You are a visual question answering assistant for hyperspectual remote sensing imagery. "
        "You must answer the multiple-choice question strictly based on the provided image. "
        "The image is a grayscale visualization derived from the first 12 PCA components of hyperspectral data. "
        "You must carefully inspect the image before answering. "
        "Do not rely on outside knowledge alone, and do not guess if the image does not provide enough evidence. "
        "Return only one uppercase option letter from the given choices, such as A, B, C, D, E, F. "
        "Do not output any explanation or extra text."
    )
    #  (
    #     "You are a textual question answering assistant for hyperspectual remote sensing report. "
    #     "You must answer the multiple-choice question strictly based on the provided report. "
    #     "Return only one uppercase option letter from the given choices, such as A, B, C, D, E, F. "
    #     "Use your knowledge of material spectral signatures to interpret the report. "
    #     "Do not make assumptions beyond what is explicitly stated. "
    #     "Do not output any explanation or extra text."
    # )
    )

        # 辅助方法：获取 base_url 列表，方便直接传给 client
    @staticmethod
    def get_base_urls() -> List[str]:
        return Config.OPENAI_BASE_URLS