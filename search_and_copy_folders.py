import os
import csv
import shutil
import zipfile
import rarfile
from tqdm import tqdm

def search_folders(location, phrases, destination_folder):
    num_folders_found = 0
    num_folders_processed = 0

    for root, dirs, files in os.walk(location):
        for folder in tqdm(dirs, desc="Searching folders", unit="folder"):
            num_folders_processed += 1
            if folder.endswith('.fid'):
                folder_name = os.path.basename(folder)
                for phrase in phrases:
                    if phrase in folder_name:
                        source_folder = os.path.join(root, folder)
                        destination_path = os.path.join(destination_folder, folder_name)
                        if not os.path.exists(destination_path):
                            shutil.copytree(source_folder, destination_path)
                            num_folders_found += 1
                            print(f"Copied folder: {source_folder} -> {destination_path}")
                        else:
                            print(f"Folder already exists, skipping: {source_folder} -> {destination_path}")

    print("Search completed.")
    print(f"Number of folders found: {num_folders_found}")
    print(f"Number of folders processed: {num_folders_processed}")


# Path to the folder you want to search
location = input("Enter the path to the folder: ")

# Path to the CSV file with search phrases
csv_path = input("Enter the path to the CSV file: ")

# Path to the destination folder where the found folders should be copied
destination_folder = input("Enter the path to the destination folder: ")

# Load phrases from the CSV file
phrases = []
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        phrases.extend(row)

# Call the function to search for folders and copy them to the destination folder
search_folders(location, phrases, destination_folder)
