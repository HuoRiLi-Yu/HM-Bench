from collections import defaultdict
import json


def normalize_group_value(value):
    """
    把分组字段转成可哈希、可展示的形式
    """
    if value is None:
        return "unknown"

    # list / dict 不能直接做 dict key，统一转字符串
    if isinstance(value, (list, dict)):
        try:
            return json.dumps(value, ensure_ascii=False, sort_keys=True)
        except Exception:
            return str(value)

    return value


def compute_random_baseline(records):
    probs = []
    for r in records:
        num_options = r.get("num_options", 0)
        if isinstance(num_options, int) and num_options > 0:
            probs.append(1.0 / num_options)
    return sum(probs) / len(probs) if probs else 0.0


def compute_group_metrics(records, key):
    stats = defaultdict(lambda: {"total": 0, "correct": 0, "valid": 0})

    for r in records:
        raw_group_val = r.get(key, "unknown")
        group_val = normalize_group_value(raw_group_val)

        stats[group_val]["total"] += 1
        if r.get("parsed_answer") is not None:
            stats[group_val]["valid"] += 1
        if r.get("is_correct", False):
            stats[group_val]["correct"] += 1

    result = {}
    for k, v in stats.items():
        total = v["total"]
        result[str(k)] = {
            "total": total,
            "correct": v["correct"],
            "valid": v["valid"],
            "accuracy": v["correct"] / total if total else 0.0,
            "valid_rate": v["valid"] / total if total else 0.0
        }
    return result


def evaluate_predictions(records):
    total = len(records)
    correct = sum(1 for r in records if r.get("is_correct", False))
    valid = sum(1 for r in records if r.get("parsed_answer") is not None)

    pred_option_distribution = defaultdict(int)
    num_options_distribution = defaultdict(int)

    for r in records:
        parsed_answer = r.get("parsed_answer")
        if parsed_answer is not None:
            pred_option_distribution[str(parsed_answer)] += 1

        num_options = r.get("num_options", 0)
        num_options_distribution[str(num_options)] += 1

    summary = {
        "total_samples": total,
        "correct": correct,
        "valid": valid,
        "overall_accuracy": correct / total if total else 0.0,
        "valid_rate": valid / total if total else 0.0,
        "invalid_rate": 1 - (valid / total if total else 0.0),
        "random_guess_baseline": compute_random_baseline(records),
        "pred_option_distribution": dict(pred_option_distribution),
        "num_options_distribution": dict(num_options_distribution),
        "per_task_type": compute_group_metrics(records, "task_type"),
        "per_dataset": compute_group_metrics(records, "dataset"),
        "per_level1_id": compute_group_metrics(records, "level1_id"),
        "per_level2_id": compute_group_metrics(records, "level2_id"),
        "per_level3_id": compute_group_metrics(records, "level3_id")
    }
    return summary