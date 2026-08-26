# Kaggle Notebooks & Data Experiments

## Overview

Welcome to this repository. It contains a collection of Jupyter Notebooks derived from various Kaggle datasets. The primary goal here was to practice data manipulation, visualization, and linear regression.

## 📂 Repository Structure

Here is the current state of the chaos:

| File | Description |
| :--- | :--- |
| **`winter-fashion.ipynb`** | Analysis of winter fashion trends dataset |
| **`penguins.ipynb`** | Palmer Archipelago penguin dataset analysis |
| **`gpu-specs.ipynb`** | Historical GPU specifications from 1986 to 2026 |
| **`fatique-dataset.ipynb`** | Image classification dataset for fatigue detection |
| **`eeg.ipynb`** | EEG headset signal visualization and analysis |
| **`programming-languages.ipynb`** | Programming languages popularity dataset |
| **`download_datasets.py`** | Script to download all Kaggle datasets into `data/` |

## 📥 Data Setup

Datasets are downloaded and stored locally in the `data/` directory. All notebooks load datasets directly from `data/` instead of `/kaggle/input`.

To download or refresh all datasets locally:
```bash
python download_datasets.py
```


