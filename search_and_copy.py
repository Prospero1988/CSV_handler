# The script is used to search a specified location (including subfolders) using a list saved in a CSV file.
# The list contains strings that the script will search for in file names in the specified location.
# The script also opens and searches files in RAR and ZIP archives.
# All found files are copied to a newly defined folder.

import os
import csv
import shutil
import zipfile
import rarfile
from tqdm import tqdm

def search_files(location, phrases, destination_folder):
    num_files_found = 0
    num_files_processed = 0

    for root, dirs, files in os.walk(location):
        for file in tqdm(files, desc="Searching files", unit="file"):
            num_files_processed += 1
            file_name = os.path.basename(file)
            if file_name.endswith('.zip'):
                archive_path = os.path.join(root, file)
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    for zip_file_name in zip_ref.namelist():
                        for phrase in phrases:
                            if phrase in zip_file_name:
                                extracted_file_path = zip_ref.extract(zip_file_name, destination_folder)
                                num_files_found += 1
                                print(f"Found and copied file from ZIP archive: {extracted_file_path}")
            elif file_name.endswith('.rar'):
                archive_path = os.path.join(root, file)
                with rarfile.RarFile(archive_path, 'r') as rar_ref:
                    for rar_file_name in rar_ref.namelist():
                        for phrase in phrases:
                            if phrase in rar_file_name:
                                extracted_file_path = rar_ref.extract(rar_file_name, destination_folder)
                                num_files_found += 1
                                print(f"Found and copied file from RAR archive: {extracted_file_path}")
            else:
                for phrase in phrases:
                    if phrase in file_name:
                        source_path = os.path.join(root, file)
                        destination_path = os.path.join(destination_folder, file)
                        shutil.copy(source_path, destination_path)
                        num_files_found += 1
                        print(f"Found and copied file: {source_path} -> {destination_path}")

    print("Search completed.")
    print(f"Number of files found: {num_files_found}")
    print(f"Number of files processed: {num_files_processed}")


# Path to the folder you want to search
location = input("Enter the path to the folder: ")

# Path to the CSV file with search phrases
csv_path = input("Enter the path to the CSV file: ")

# Path to the destination folder where the found files should be copied
destination_folder = input("Enter the path to the destination folder: ")

# Load phrases from the CSV file
phrases = []
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        phrases.extend(row)

# Call the function to search for files and copy them to the destination folder
search_files(location, phrases, destination_folder)
