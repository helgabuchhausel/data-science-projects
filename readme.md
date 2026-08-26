# Kaggle Notebooks & Data Experiments

## Overview

Welcome to this repository. It contains a collection of Jupyter Notebooks derived from various Kaggle datasets. The primary goal here was to practice data manipulation, visualization, and linear regression.

## 📂 Repository Structure

Here is the current state of the chaos:

| File | Description | Algorithms & Plots |
| :--- | :--- | :--- |
| **`winter-fashion.ipynb`** | Analysis of winter fashion trends dataset | Linear Regression, Bar, Box, Scatter plots |
| **`penguins.ipynb`** | Palmer Archipelago penguin dataset analysis | Scatter, Line plots |
| **`gpu-specs.ipynb`** | Historical GPU specifications from 1986 to 2026 | Scatter, Bar, Box, Line plots |
| **`fatique-dataset.ipynb`** | Image classification dataset for fatigue detection | Deep Learning, Line plots |
| **`eeg.ipynb`** | EEG headset signal visualization and analysis | Scatter, Line plots |
| **`programming-languages.ipynb`** | Programming languages popularity dataset | Bar plots |
| **`its-raining-cats.ipynb`** | Analysis of cat breeds dataset | Linear Regression, KMeans, Hist plots |
| **`download_datasets.py`** | Script to download all Kaggle datasets into `data/` | N/A |

## 📥 Data Setup

Datasets are downloaded and stored locally in the `data/` directory. All notebooks load datasets directly from `data/` instead of `/kaggle/input`.

To download or refresh all datasets locally:
```bash
python download_datasets.py
```


