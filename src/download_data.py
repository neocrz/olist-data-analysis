import kagglehub
import os
import shutil

path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

print("Path to dataset files:", path)

target_data_raw_dir = "./data/raw"

if not os.path.exists(target_data_raw_dir):
    os.makedirs(target_data_raw_dir)
    print(f"Created directory: {target_data_raw_dir}")

for item_name in os.listdir(path):
    source_item_path = os.path.join(path, item_name)
    destination_item_path = os.path.join(target_data_raw_dir, item_name)

    if os.path.isdir(source_item_path):
        # If it's a directory, copy the entire directory
        shutil.copytree(source_item_path, destination_item_path, dirs_exist_ok=True)
    else:
        # If it's a file, copy the file
        shutil.copy2(source_item_path, destination_item_path)

print(f"Successfully copied contents from '{path}' to '{target_data_raw_dir}'")