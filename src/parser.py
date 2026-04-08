# import re

# def parse_mcq_answer(raw_text, valid_letters):
#     """
#     从模型输出中尽量稳定提取选项字母
#     """
#     if raw_text is None:
#         return None

#     valid_letters = [x.upper() for x in valid_letters]
#     text = raw_text.strip().upper()

#     # 1) 纯字母
#     if text in valid_letters:
#         return text

#     # 2) 常见格式
#     patterns = [
#         r"^([A-Z])[\.\)]?$",                  # A / A. / A)
#         r"ANSWER\s*[:：]?\s*([A-Z])",
#         r"OPTION\s*[:：]?\s*([A-Z])",
#         r"CHOICE\s*[:：]?\s*([A-Z])",
#         r"THE ANSWER IS\s*([A-Z])",
#         r"FINAL ANSWER\s*[:：]?\s*([A-Z])",
#         r"\(([A-Z])\)",
#         r"\b([A-Z])\b"
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, text)
#         if match:
#             cand = match.group(1).upper()
#             if cand in valid_letters:
#                 return cand

#     return None

import re

def parse_mcq_answer(raw_text, valid_letters):
    """
    鲁棒提取 MCQ 答案字母，支持多格式、防误匹配、位置优先
    """
    if raw_text is None:
        return None

    valid_set = set(x.upper() for x in valid_letters)
    text = raw_text.strip().upper()

    # 1. 快速路径：整串就是有效字母
    if text in valid_set:
        return text

    # 2. 构建安全字母匹配模式（防止 Concrete → C）
    letters_pattern = ''.join(sorted(valid_set))
    safe_letter_pattern = f"(?<![A-Za-z0-9])([{letters_pattern}])(?![A-Za-z0-9])"

    # 3. 所有匹配模式（含安全字母模式）
    patterns = [
        r"^([A-Z])[\.\)]?$",                  # A / A. / A)
        r"ANSWER\s*[:：]?\s*([A-Z])",
        r"OPTION\s*[:：]?\s*([A-Z])",
        r"CHOICE\s*[:：]?\s*([A-Z])",
        r"THE ANSWER IS\s*([A-Z])",
        r"FINAL ANSWER\s*[:：]?\s*([A-Z])",
        r"\(([A-Z])\)",
        safe_letter_pattern                    # ← 替换原来的 \b([A-Z])\b
    ]

    # 4. 收集所有有效匹配（位置 + 候选）
    matches = []
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            cand = match.group(1).upper()
            if cand in valid_set:
                matches.append((match.start(), cand))

    if not matches:
        return None

    # 5. 去重检查：多个不同答案 → 拒绝
    unique_cands = set(cand for _, cand in matches)
    if len(unique_cands) > 1:
        return None  # 模糊输出

    # 6. 返回最早出现的答案
    matches.sort(key=lambda x: x[0])
    return matches[0][1]