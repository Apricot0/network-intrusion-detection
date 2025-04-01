import requests
import os
from tqdm import tqdm


os.makedirs("datasets", exist_ok=True)


def download_dataset(dataset_name, dataset_url):
    save_path = os.path.join("datasets", os.path.basename(dataset_name) + ".zip")
    
    if os.path.exists(save_path):
        print(f"Dataset {dataset_name} already exists. Skipping download.")
        return
    
    print(f"Downloading dataset from {dataset_url}...")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(dataset_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1KB

    with open(save_path, "wb") as file, tqdm(
        desc=f"Downloading {os.path.basename(save_path)}", total=total_size, unit="B", unit_scale=True
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))

    print(f"Dataset saved to: {save_path}")

dataset_list = {"edgeiiotset":"https://www.kaggle.com/api/v1/datasets/download/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot","xiiotid":"https://www.kaggle.com/api/v1/datasets/download/munaalhawawreh/xiiotid-iiot-intrusion-dataset","mattset": "https://www.kaggle.com/api/v1/datasets/download/cnrieiit/mqttset","wustl_iiot_2021": "https://www.cse.wustl.edu/~jain/iiot2/ftp/wustl_iiot_2021.zip"}

for dataset_name, dataset_url in dataset_list.items():
    download_dataset(dataset_name, dataset_url)