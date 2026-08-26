import io
import os
import urllib.request
import zipfile

DATASETS = [
    ("ppb00x/eeg-neuroheadset", "data"),
    ("rihabkaci99/fatigue-dataset", "data/fatigue-dataset"),
    ("ellimaaac/gpus-specs-from-1986-to-2026", "data"),
    ("ranaghulamnabi/penguins", "data"),
    ("shakhnoza12/programming-languages-dataset", "data"),
    ("ayeshaseherr/winter-fashoin-trends", "data"),
]

def download_and_extract():
    os.makedirs("data", exist_ok=True)
    print("Downloading datasets into 'data/' folder...")

    headers = {"User-Agent": "Mozilla/5.0"}
    for slug, target_dir in DATASETS:
        os.makedirs(target_dir, exist_ok=True)
        url = f"https://www.kaggle.com/api/v1/datasets/download/{slug}"
        print(f"Fetching {slug}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                zip_data = response.read()
            with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
                z.extractall(target_dir)
            print(f"  Successfully extracted to '{target_dir}'")
        except Exception as e:
            print(f"  Failed to download {slug}: {e}")

if __name__ == "__main__":
    download_and_extract()
