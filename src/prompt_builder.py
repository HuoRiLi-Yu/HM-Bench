def build_mcq_prompt(sample, report_content=None):
    question = sample["question"]
    options = sample["options"]
    valid_letters = sorted(options.keys())
    option_lines = "\n".join([f"{k}. {options[k]}" for k in valid_letters])
    
    # 动态生成合法选项字符串，例如 "A, B, C, D"
    valid_options_str = ", ".join(valid_letters)

    if report_content is not None:
        # 文本报告模式
        prompt = (
            "The provided input is a spectral analysis report generated from hyperspectral remote sensing data. "
            "This report contains quantitative or qualitative descriptions of the material's spectral signature, "
            "such as reflectance characteristics, classification scores, or matching confidence against standard libraries.\n\n"
            "Answer the multiple-choice question strictly based on the evidence presented in this report. "
            "you MUST select the most plausible answer from the given options based on available evidence.\n"
            "Use your knowledge of material spectral signatures to interpret the report.\n"
            "Do not make assumptions beyond what is explicitly stated.\n\n"
            f"Report Content:\n{report_content}\n\n"
            f"Question:\n{question}\n\n"
            f"Options:\n{option_lines}\n\n"
            f"You MUST choose your answer ONLY from the available options: {{{valid_options_str}}}.\n"
            "DO NOT select any letter that is not listed above.\n"
            "Output exactly one uppercase option letter only.\n"
            "Do not explain. Do not output anything else.\n\n"
            "Answer:"
        )
    else:
        # 图像模式
        prompt = (
            "The provided image is a grayscale visualization derived from the first 12 PCA components "
            "of hyperspectral remote sensing data. The image preserves important spectral-spatial patterns "
            "such as texture, contrast, boundaries, and regional structure.\n\n"
            "Answer the multiple-choice question strictly based on visual evidence from this image. "
            "Carefully inspect the grayscale patterns before selecting an answer.\n\n"
            "you MUST select the most plausible answer from the given options based on available evidence.\n"
            f"Question:\n{question}\n\n"
            f"Options:\n{option_lines}\n\n"
            f"You MUST choose your answer ONLY from the available options: {{{valid_options_str}}}.\n"
            "DO NOT select any letter that is not listed above.\n"
            "Output exactly one uppercase option letter only.\n"
            "Do not explain.\n\n"
            "Answer:"
        )
    return prompt, valid_letters