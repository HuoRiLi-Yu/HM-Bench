# 🌈 HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing

[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](YOUR_ARXIV_LINK_HERE)
[![Supplementary](https://img.shields.io/badge/Supplementary-Material-green)](YOUR_SUPPLEMENTARY_LINK_HERE)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue)](LICENSE)

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
| **🧊 Raw Hyperspectral Blocks** | Original hyperspectral data cubes preserving full spectral fidelity | [Baidu Drive](https://pan.baidu.com/s/167-4652sJaW1RujtNHGU4w?pwd=31yj)  |
| **🖼️ PCA Composite Images** | Grayscale visualization from first 12 PCA components for direct MLLM input | [Baidu Drive](https://pan.baidu.com/s/1aaGZKu9632mFdUeqwHieGw?pwd=7viu)  |
| **📄 Structured Reports** | Quantitative spectral feature descriptions in structured text format | [Baidu Drive](https://pan.baidu.com/s/1HxTtvBoTqn7F5TJrRID73Q?pwd=3yae)  |

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
├── 📄 case_study　　　　　　　 # case study  
└── 📄 HM_Bench_Appendix.pdf　　　 # Supplementary Material  

### 🔧 Usage Notes

- **QA Pairs:** The `QA_for_image` and `QA_for_report` folders contain **identical question-answer content**; only the data path references differ. This design enables direct comparison of model performance across visual and textual modalities.
  
- **Extensibility:** If your research involves feeding raw hyperspectral data directly to MLLMs, simply modify the `image_path` fields in the JSON files to point to your custom data location.

- **Source Code:** The `src/` directory contains our complete evaluation pipeline, including prompt construction, API connection handlers, and automated scoring scripts. Feel free to adapt these for your specific experimental setup.

---

## 🖼️ Case Studies

Below we present 12 representative case studies illustrating model behaviors across different task categories and input modalities:

<div align="center">

### Perception Tasks

| Feature Recognition | Target Quantification | Spatial Localization |
|:---:|:---:|:---:|
| ![Case 1](casestudy/case01.png) | ![Case 2](casestudy/case02.png) | ![Case 3](casestudy/case03.png) |
| *Case 1: [Description]* | *Case 2: [Description]* | *Case 3: [Description]* |

| Case 4 | Case 5 | Case 6 |
|:---:|:---:|:---:|
| ![Case 4](casestudy/case04.png) | ![Case 5](casestudy/case05.png) | ![Case 6](casestudy/case06.png) |
| *Case 4: [Description]* | *Case 5: [Description]* | *Case 6: [Description]* |

### Reasoning Tasks

| Composition Interpretation | State Assessment | Change Detection |
|:---:|:---:|:---:|
| ![Case 7](casestudy/case07.png) | ![Case 8](casestudy/case08.png) | ![Case 9](casestudy/case09.png) |
| *Case 7: [Description]* | *Case 8: [Description]* | *Case 9: [Description]* |

| Case 10 | Case 11 | Case 12 |
|:---:|:---:|:---:|
| ![Case 10](casestudy/case10.png) | ![Case 11](casestudy/case11.png) | ![Case 12](casestudy/case12.png) |
| *Case 10: [Description]* | *Case 11: [Description]* | *Case 12: [Description]* |

</div>

> 📝 **Note:** Replace `casestudy/caseXX.png` with your actual image paths and update the descriptions to match your specific visualization content.

---

## 📚 Resources

| Resource | Link | Description |
|:---|:---|:---|
| **📄 Paper (arXiv)** | [YOUR_ARXIV_LINK_HERE](YOUR_ARXIV_LINK_HERE) | Full technical paper with methodology and results |
| **📊 Supplementary Material** | [YOUR_SUPPLEMENTARY_LINK_HERE](YOUR_SUPPLEMENTARY_LINK_HERE) | Detailed prompt templates, evaluation scripts, and extended statistical analysis |
| **🏛️ Project Page** | [YOUR_PROJECT_PAGE_HERE](YOUR_PROJECT_PAGE_HERE) | Interactive data explorer and additional visualizations |

---

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
📧 Contact
For questions or feedback regarding the dataset, please open an issue in this repository or contact the authors through the paper submission system.
<div align="center">
⭐ Star this repository if you find it helpful!
</div>
