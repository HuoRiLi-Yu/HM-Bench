# 🌈 HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing


[![Paper](https://img.shields.io/badge/Paper-PDF-red)]()
[![Dataset](https://img.shields.io/badge/Dataset-Download-blue)]()
[![Supplementary](https://img.shields.io/badge/Supplementary-Material-green)]()


**HM-Bench** is the first comprehensive benchmark designed to evaluate **Multimodal Large Language Models (MLLMs)** in the domain of **Hyperspectral Remote Sensing (HSI)**. We bridge the gap between general-purpose MLLMs and the specialized requirements of spectral-spatial analysis.

---

## 🚀 Highlights

-   **🌍 Diverse Coverage:** Integrates **20 high-fidelity public datasets**, spanning diverse scenarios from precision agriculture and complex urban landscapes to planetary exploration (Mars).
-   **📊 Large-Scale QA Pairs:** Comprises **19,337** high-quality question-answer pairs across **13 distinct task categories**.
-   **🧩 Dual-Modality Evaluation:** Uniquely provides both **PCA Composite Images** and **Structured Text Reports**, enabling a systematic comparison of model reasoning across visual and textual inputs.
-   **🧠 Hierarchical Tasks:** Establishes a three-level task system ranging from basic **Perception** (e.g., feature recognition) to advanced **Reasoning** (e.g., spectral unmixing, vegetation health diagnosis).

---

## 📂 Dataset Overview

HM-Bench is constructed through a rigorous pipeline that transforms raw HSI cubes into MLLM-friendly formats while preserving critical spectral fingerprint information.

### 1. Data Sources
We aggregate **2,178 independent samples** from satellite, airborne, and planetary sensors, covering a spectral range from **0.364μm to 3.8μm**.

### 2. Input Modalities
For each sample, we provide two complementary representations to test the model's adaptability:

| Modality | Description | Focus Area |
| :--- | :--- | :--- |
| **🖼️ Image Input** | Grayscale visualization derived from the first 12 PCA components. | **Visual Inspection:** Focuses on spatial patterns, texture, and boundaries. |
| **📝 Report Input** | Structured text containing quantitative spectral feature descriptions. | **Evidence-Based Reasoning:** Utilizes spectral signatures and domain knowledge for logical deduction. |

### 3. Task Taxonomy
The benchmark evaluates six core capability dimensions:
-   **👁️ Perception:** Feature Recognition (FR), Target Quantification (TQ), Spatial Localization (SL).
-   **🧠 Reasoning:** Composition Interpretation (CI), State Assessment (SA), Change Detection (CD).

---

## 📥 Download & Resources

### Dataset Download
You can access the full HM-Bench dataset via the link below:

> **🔗 Download Link:** [Insert Your Dataset Link Here]

### Supplementary Material
Includes detailed prompt templates, evaluation scripts, and extended statistical analysis:

> **📄 Supplementary Material:** [Insert Your Supplementary Link Here]

### Paper Archive
Access the full paper and technical report here:

> **🏛️ Paper Archive:** [Insert Your Archive/arXiv Link Here]

---

## 📜 Citation

If you use HM-Bench in your research or refer to our benchmark, please cite our work:

```bibtex
@misc{anonymous2026hmbench,
  title={HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing},
  author={Anonymous Authors},
  year={2026},
  eprint={xxxx.xxxxx},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
