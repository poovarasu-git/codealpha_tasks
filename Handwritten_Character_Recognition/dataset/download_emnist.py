
import os
import requests
import zipfile

# EMNIST letters dataset URL from NIST
url = "http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip"
dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)
zip_path = os.path.join(dataset_dir, "emnist.zip")

print("Downloading EMNIST dataset...")
response = requests.get(url)
with open(zip_path, "wb") as f:
    f.write(response.content)

print("Extracting files...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(dataset_dir)

print("Done. EMNIST dataset extracted to:", dataset_dir)
