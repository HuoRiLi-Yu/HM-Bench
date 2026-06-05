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
| <img src="case%20study/case_1.png" width="300"> | <img src="case%20study/case_2.png" width="300"> | <img src="case%20study/case_3.png" width="300"> |

| Case 4 | Case 5 | Case 6 |
|:---:|:---:|:---:|
| <img src="case%20study/case_4.png" width="300"> | <img src="case%20study/case_5.png" width="300"> | <img src="case%20study/case_6.png" width="300"> |

| Case 7 | Case 8 | Case 9 |
|:---:|:---:|:---:|
| <img src="case%20study/case_7.png" width="300"> | <img src="case%20study/case_8.png" width="300"> | <img src="case%20study/case_9.png" width="300"> |

| Case 10 | Case 11 | Case 12 |
|:---:|:---:|:---:|
| <img src="case%20study/case_10.png" width="300"> | <img src="case%20study/case_11.png" width="300"> | <img src="case%20study/case_12.png" width="300"> |

</div>

## Additional Results for Rebuttal

This section provides the additional experiments and analyses requested during rebuttal, including PCA ablations, explained variance statistics, repeated-run results, human baseline, annotation quality control, and open-ended evaluation.


## Additional Results for Rebuttal

This section provides the additional experiments and analyses requested during rebuttal, including PCA ablations, explained variance statistics, repeated-run results, human baseline, annotation quality control, and open-ended evaluation.

- [1. PCA Ablation on the Number of Principal Components](#1-pca-ablation-on-the-number-of-principal-components)
- [2. PCA Explained Variance Across Datasets](#2-pca-explained-variance-across-datasets)
- [3. Re-run Results for Claude and Representative Open-source Models](#3-re-run-results-for-claude-and-representative-open-source-models)
- [4. Human Baseline](#4-human-baseline)
- [5. QA Quality Control Statistics](#5-qa-quality-control-statistics)
- [6. Open-ended Evaluation](#6-open-ended-evaluation)


---

### 1. PCA Ablation on the Number of Principal Components

**Take-away.** Across three representative MLLMs, using **12 principal components (PCs)** provides the best overall trade-off.


| Model | 6 PCs | 12 PCs | 24 PCs |
|---|---:|---:|---:|
| Qwen3-VL | 40.57 | **40.96** | 40.34 |
| InternVL2 | 36.08 | **36.17** | 36.10 |
| LLaVA-1.5 | 31.19 | **33.98** | 31.14 |


**Note.** These results support our use of 12 PCs as a practical default setting.

---

### 2. PCA Explained Variance Across Datasets

**Take-away.** PCA retains a high proportion of spectral variance on most datasets with a small number of components, while some datasets (notably **KSC**) remain substantially more challenging.

#### 2.1 Full explained-variance table


| Dataset | #Bands | EV@1 | EV@3 | EV@6 | EV@12 | EV@24 | #PCs for 90% EV | #PCs for 95% EV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| santaBarbara_2013 | 224 | 80.99 | 94.45 | 96.39 | 98.09 | 99.38 | 2 | 4 |
| output_Nilifossae | 425 | 84.03 | 98.71 | 99.62 | 99.86 | 99.94 | 2 | 3 |
| urban | 162 | 68.84 | 98.68 | 99.66 | 99.87 | 99.94 | 2 | 2 |
| BayArea_2015 | 224 | 54.10 | 99.44 | 99.81 | 99.93 | 99.96 | 2 | 2 |
| Houston_13 | 48 | 59.15 | 99.66 | 99.94 | 99.98 | 99.99 | 2 | 2 |
| paviac | 102 | 75.03 | 99.31 | 99.78 | 99.93 | 99.97 | 2 | 2 |
| new_output_HanChuan | 274 | 92.21 | 99.45 | 99.67 | 99.74 | 99.81 | 1 | 2 |
| new_output_HongHu | 270 | 61.95 | 96.90 | 98.11 | 98.78 | 99.25 | 2 | 2 |
| new_output_LongKou | 270 | 95.47 | 99.85 | 99.93 | 99.96 | 99.97 | 1 | 1 |
| Washington_blocks | 191 | 83.44 | 99.49 | 99.87 | 99.96 | 99.98 | 2 | 2 |
| ksc | 176 | 26.18 | 41.79 | 56.49 | 70.26 | 86.21 | 29 | 37 |
| Hermiston_2004 | 242 | 76.77 | 93.59 | 96.67 | 97.99 | 98.97 | 3 | 4 |
| Indianpines | 200 | 58.49 | 90.94 | 93.99 | 96.93 | 98.74 | 3 | 8 |
| Hermiston_2007 | 242 | 73.11 | 90.17 | 95.29 | 97.19 | 98.56 | 3 | 6 |
| santaBarbara_2014 | 224 | 82.94 | 96.50 | 97.65 | 98.65 | 99.61 | 2 | 2 |
| BayArea_2013 | 224 | 82.52 | 99.81 | 99.96 | 99.99 | 99.99 | 2 | 2 |
| output_holden | 440 | 95.61 | 98.89 | 99.56 | 99.76 | 99.88 | 1 | 1 |
| output_xiongan_blocks | 256 | 60.56 | 99.34 | 99.70 | 99.75 | 99.77 | 2 | 2 |
| botswana | 145 | 94.62 | 99.40 | 99.67 | 99.78 | 99.87 | 1 | 2 |
| output_Salinas | 204 | 87.89 | 99.59 | 99.85 | 99.94 | 99.96 | 2 | 2 |
| output_utopia | 432 | 70.64 | 96.78 | 98.15 | 99.02 | 99.47 | 2 | 3 |
| paviau | 103 | 48.65 | 98.42 | 99.35 | 99.81 | 99.94 | 2 | 2 |
| Houston_18 | 48 | 74.62 | 99.65 | 99.93 | 99.98 | 99.99 | 2 | 2 |


#### 2.2 Explained-variance curves

> Please place the PCA explained-variance curve figure below.

![PCA Explained Variance Curves](./assets/pca_explained_variance_curves.png)

**Note.** The figure path above can be replaced with the actual file location in the repository.

---

### 3. Re-run Results for Claude and Representative Open-source Models

**Take-away.** The originally anomalous Claude result becomes normal after re-running, and repeated runs on representative open-source models show consistent trends.

#### 3.1 Overall rerun results


| Model | Modality | Overall |
|---|---|---:|
| Claude-sonnet-4-6 | Image | 39.48 |
| Claude-sonnet-4-6 | Report | 36.57 |
| Qwen3-vl-4B | Image | 39.38 |
| Qwen3-vl-4B | Report | 35.52 |
| InternVL2-8B | Image | 37.66 |
| InternVL2-8B | Report | 36.58 |
| LLaVA-1.5-7B | Image | 31.21 |
| LLaVA-1.5-7B | Report | 30.44 |


#### 3.2 Fine-grained rerun breakdown


| Model | Input | FR (SFR / LCC) | TQ (PD / CS) | SL (OLR / RD) | CI (SAD / SU) | SA (VH / EPSA) | CD (BCI / CAL / CSA) | Overall |
|---|---|---|---|---|---|---|---|---:|
| **Claude-sonnet-4-6** | Image | 58.20 / 42.17 | 50.07 / 26.73 | 29.02 / 43.77 | 32.05 / 42.65 | 49.26 / 56.48 | 38.08 / 14.80 / 30.00 | 39.48 |
|  | Report | 41.54 / 23.39 | 39.80 / 34.57 | 30.38 / 47.30 | 39.58 / 39.62 | 48.58 / 45.37 | 30.36 / 21.60 / 33.33 | 36.57 |
| **Qwen3-vl-4B** | Image | 47.81 / 30.45 | 34.61 / 33.94 | 27.50 / 29.05 | 66.06 / 41.76 | 41.96 / 64.89 | 42.21 / 10.03 / 41.67 | 39.38 |
|  | Report | 33.63 / 19.34 | 23.70 / 44.16 | 27.08 / 23.49 | 59.74 / 36.44 | 55.44 / 59.03 | 28.76 / 15.14 / 35.83 | 35.52 |
| **InternVL2-8B** | Image | 40.03 / 27.93 | 41.89 / 37.23 | 27.61 / 31.46 | 42.89 / 42.87 | 39.69 / 66.36 | 38.08 / 11.05 / 42.50 | 37.66 |
|  | Report | 36.98 / 20.63 | 28.82 / 40.31 | 26.51 / 28.04 | 63.28 / 38.14 | 41.73 / 62.89 | 33.29 / 14.97 / 40.00 | 36.58 |
| **LLaVA-1.5-7B** | Image | 39.18 / 44.51 | 63.97 / 37.72 | 23.99 / 27.07 | 21.97 / 28.09 | 30.63 / 17.75 | 30.76 / 10.03 / 30.00 | 31.21 |
|  | Report | 37.50 / 43.28 | 62.02 / 36.88 | 23.47 / 27.02 | 20.39 / 27.79 | 30.63 / 16.51 | 30.23 / 10.03 / 30.00 | 30.44 |


**Abbreviation note.**  
- **FR**: Feature Recognition  
- **TQ**: Target Quantification  
- **SL**: Spatial Localization  
- **CI**: Category Identification  
- **SA**: Scene Analysis  
- **CD**: Change Detection  

Sub-dimension abbreviations follow the benchmark task taxonomy used in the paper.

---

### 4. Human Baseline

**Take-away.** HM-Bench is challenging even for domain experts under zero-shot, no-software conditions.


| Evaluator | PCA Image | Report |
|---|---:|---:|
| Domain experts (without analytical software) | 26.57 | 31.12 |


**Note.** Experts answered using only the provided benchmark inputs, without traditional hyperspectral analysis tools.

---

### 5. QA Quality Control Statistics

**Take-away.** All MLLM-assisted QA pairs were audited by remote-sensing experts, with an overall rejection rate of **18.1%**.

#### 5.1 Overall filtering statistics


| Stage | Count |
|---|---:|
| Initial MLLM-generated drafts | 7,979 |
| Rejected drafts | 1,445 |
| Retained verified pairs | 6,534 |
| ├─ MCQs | 5,535 |
| └─ Open-ended QA pairs | 999 |


#### 5.2 Rejection breakdown


| Error Category | Count | Ratio | Typical causes |
|---|---:|---:|---|
| Hallucination | 502 | 34.7% | Fabricated percentages, unverified pixel counts |
| Trivial | 478 | 33.1% | Lacked evaluation depth (e.g., answers ≤ 3 words) |
| Format issues | 414 | 28.7% | Structured key-values, comparative single-image format, etc. |
| Other | 51 | 3.5% | Miscellaneous phrasing or number errors |


**Note.** This expert filtering pipeline was used to reduce potential evaluation bias in MLLM-assisted QA generation.

---

### 6. Open-ended Evaluation

**Take-away.** We evaluate open-ended answers using semantic alignment rather than exact-match accuracy. Compared with BGE-M3, **BGE-Reranker-v2-m3** provides more discriminative results.


| Model | Modality | BGE-M3 (Avg) | Reranker (Avg) | Reranker >= 0.5 |
|---|---|---:|---:|---:|
| InternVL3-14B | Image | 0.827 | 0.508 | 52.92% |
| InternVL3-14B | Report | 0.809 | 0.417 | 40.89% |
| LLaVA-13B | Image | 0.843 | 0.474 | 50.06% |
| LLaVA-13B | Report | 0.837 | 0.453 | 45.82% |


**Protocol.** We evaluated 873 open-ended QA pairs. Since open-ended VQA lacks a universally accepted evaluation protocol, we use semantic alignment between generated and reference answers as a scalable proxy for answer quality.

**Observation.** BGE-M3 tends to yield inflated similarities due to shared domain vocabulary, whereas the cross-encoder reranker is more discriminative.

---
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

