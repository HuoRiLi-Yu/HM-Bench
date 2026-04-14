# 🌈 HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing

<div align="center">
  <a href="https://arxiv.org/abs/2604.08884"><img src="https://img.shields.io/badge/Paper-arXiv-red" alt="Paper"></a>
  &nbsp;&nbsp;
  <a href="HM_Bench_Appendix.pdf"><img src="https://img.shields.io/badge/Supplementary-Material-green" alt="Supplementary"></a>
  &nbsp;&nbsp;
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue" alt="License"></a>
  &nbsp;&nbsp;
  <a href="https://huggingface.co/datasets/Huorili/HM-Bench"><img src="https://img.shields.io/badge/🤗-Hugging%20Face%20Dataset-yellow" alt="Hugging Face Dataset"></a>
</div>

---

## 🎯 Overview

**HM-Bench** is the first comprehensive benchmark specifically designed to evaluate **Multimodal Large Language Models (MLLMs)** in the specialized domain of **Hyperspectral Remote Sensing (HSI)**. We bridge the critical gap between general-purpose vision-language models and the unique demands of spectral-spatial analysis, establishing a rigorous evaluation protocol for next-generation Earth observation AI systems.

---

## 🚀 Key Features

| Feature | Description |
|:---|:---|
| **🌍 Global Coverage** | **20 high-fidelity public datasets** spanning precision agriculture, complex urban landscapes, and planetary exploration (Mars). |
| **📊 Large-Scale Evaluation** | **19,337 expert-curated question-answer pairs** across **13 distinct task categories**. |
| **🧩 Dual-Modality Design** | Unique parallel evaluation using **PCA Composite Images** and **Structured Text Reports** for systematic comparison of visual vs. textual reasoning. |
| **🧠 Hierarchical Tasks** | Three-level cognitive framework from basic **Perception** (feature recognition) to advanced **Reasoning** (spectral unmixing, vegetation health diagnosis). |

---

## 📊 Dataset Statistics

| Component | Details |
|:---|:---|
| **Total Samples** | 2,178 independent hyperspectral cubes |
| **Spectral Range** | 0.364μm – 3.8μm |
| **Data Sources** | Satellite, airborne, and planetary sensors |
| **QA Pairs** | 19,337 high-quality question-answer pairs |
| **Task Categories** | 13 distinct evaluation tasks |
---

## 📥 Dataset Download

The HM-Bench dataset is organized into three complementary components, designed to support diverse research directions:

### 📦 Data Components

| Component | Description | Download |
|:---|:---|:---:|
| **🧊 Raw Hyperspectral Blocks** | Original hyperspectral data cubes preserving full spectral fidelity | [Baidu Drive](https://pan.baidu.com/s/167-4652sJaW1RujtNHGU4w?pwd=31yj) <br> [Google Drive](https://drive.google.com/file/d/1Fhwh0AwEZmGOJZidRhXzR85HckTWH_rJ/view?usp=sharing) |
| **🖼️ PCA Composite Images** | Grayscale visualization from first 12 PCA components for direct MLLM input | [Baidu Drive](https://pan.baidu.com/s/1aaGZKu9632mFdUeqwHieGw?pwd=7viu) <br> [Google Drive](https://drive.google.com/file/d/11-oS8Di_UsrEoUhldiMmN0eSrd-Io7Vv/view?usp=sharing) |
| **📄 Structured Reports** | Quantitative spectral feature descriptions in structured text format | [Baidu Drive](https://pan.baidu.com/s/1HxTtvBoTqn7F5TJrRID73Q?pwd=3yae) <br> [Google Drive](https://drive.google.com/file/d/1jpwuMp0hTRA5Cr_0unjPz3h1gKXEH7Gh/view?usp=sharing) |

---

## 📂 Repository Structure
HM-Bench/  
├── 📁 QA_for_image/　　　　　　# QA pairs with image path references  
│ └── 📁 [13 task folders]/　　　　# task_1, task_2, ..., task_13  
│ └── 📄 mcq_only.json　　　　　# Multiple-choice QA pairs for each task  
│  
├── 📁 QA_for_report/　　　　　　 # QA pairs with report path references  
│ └── 📁 [13 task folders]/　　　　# task_1, task_2, ..., task_13  
│ └── 📄 mcq_only.json　　　　　# Multiple-choice QA pairs for each task  
│  
├── 📁 src/　　　　　　　　　　　# Evaluation toolkit and utilities  
│ ├── 📄 api_client.py　　　　　　 # API client for connecting to various MLLM services  
│ ├── 📄 config.py　　　　　　　 # Configuration settings (API keys, paths, hyperparameters)  
│ ├── 📄 evaluator.py　　　　　　# Evaluation metrics and scoring functions  
│ ├── 📄 io_utils.py　　　　　　　 # Input/output utilities for data loading and saving  
│ ├── 📄 parser.py　　　　　　　 # Response parser for model outputs  
│ ├── 📄 prompt_builder.py　　　 # Prompt construction templates for different tasks  
│ └── 📄 run_eval.py　　　　　　 # Main evaluation pipeline entry point  
│  
├── 📄 case_study　　　　　　　 　# case study  
└── 📄 HM_Bench_Appendix.pdf　 # Supplementary Material  

### 🔧 Usage Notes

- **QA Pairs:** The `QA_for_image` and `QA_for_report` folders contain **identical question-answer content**; only the data path references differ. This design enables direct comparison of model performance across visual and textual modalities.
  
- **Extensibility:** If your research involves feeding raw hyperspectral data directly to MLLMs, simply modify the `image_path` fields in the JSON files to point to your custom data location.

- **Source Code:** The `src/` directory contains our complete evaluation pipeline, including prompt construction, API connection handlers, and automated scoring scripts. Feel free to adapt these for your specific experimental setup.

---

## 🖼️ Case Studies

Below we present 12 representative case studies illustrating model behaviors across different task categories and input modalities:

<div align="center">


| Case 1 | Case 2 | Case 3 |
|:---:|:---:|:---:|
| ![Case 1](case%20study/case_1.png) | ![Case 2](case%20study/case_2.png) | ![Case 3](case%20study/case_3.png) |

| Case 4 | Case 5 | Case 6 |
|:---:|:---:|:---:|
| ![Case 4](case%20study/case_4.png) | ![Case 5](case%20study/case_5.png) | ![Case 6](case%20study/case_6.png) |

| Case 7 | Case 8 | Case 9 |
|:---:|:---:|:---:|
| ![Case 7](case%20study/case_7.png) | ![Case 8](case%20study/case_8.png) | ![Case 9](case%20study/case_9.png) |

| Case 10 | Case 11 | Case 12 |
|:---:|:---:|:---:|
| ![Case 10](case%20study/case_10.png) | ![Case 11](case%20study/case_11.png) | ![Case 12](case%20study/case_12.png) |

</div>

<!--
 ## 📜 Citation

If you use HM-Bench in your research, please cite our work:

```bibtex
@misc{anonymous2026hmbench,
  title={HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing},
  author={Anonymous Authors},
  year={2026},
  eprint={xxxx.xxxxx},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
-->
📧 Contact
For questions or feedback regarding the dataset, please open an issue in this repository or contact the authors through the paper submission system.

