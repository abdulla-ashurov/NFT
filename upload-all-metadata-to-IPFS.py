import requests
import os
from os import listdir
from os.path import join

metadata_directory_path = "Metadata" #Replace with your path

files = [f for f in listdir(metadata_directory_path) if str(join(metadata_directory_path, f)).endswith('.json')]
metadata_files = []

for metadata in files:
    metadata_files.append(
        ("metadata_files", open(os.path.join(metadata_directory_path, metadata), "rb")))

response = requests.post(
        "https://api.nftport.xyz/v0/metadata/directory",
        headers={"Authorization": "d580c132-0b1c-488d-8e25-ee5c49543315"},
        files=metadata_files
    )
print(response.json())