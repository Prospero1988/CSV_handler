import os
import csv
import shutil
import patoolib
import zipfile
import rarfile

def search_folders(location, phrases, destination_folder):
    num_folders_found = 0

    for root, dirs, files in os.walk(location):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if any(phrase in folder for phrase in phrases):
                destination_path = os.path.join(destination_folder, os.path.basename(folder_path))
                if not os.path.exists(destination_path):
                    shutil.copytree(folder_path, destination_path)
                    num_folders_found += 1
                    print(f"Found and copied folder: {folder_path} -> {destination_path}")
                else:
                    print(f"Folder already exists, skipping: {folder_path} -> {destination_path}")

        for file in files:
            file_name = os.path.basename(file)
            if file_name.endswith('.zip'):
                archive_path = os.path.join(root, file)
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    for name in zip_ref.namelist():
                        if name.endswith('/'):
                            continue  # pomijamy foldery wewnątrz archiwum
                        source_folder = os.path.split(name)[-2]
                        if any(phrase in source_folder for phrase in phrases):
                            destination_path = os.path.join(destination_folder, os.path.basename(source_folder))
                            if not os.path.exists(destination_path):
                                os.makedirs(destination_path)
                            zip_ref.extract(name, destination_path)
                            num_folders_found += 1
                            print(f"Found and copied folder: {source_folder} -> {destination_path}")
            elif file_name.endswith('.rar'):
                archive_path = os.path.join(root, file)
                with rarfile.RarFile(archive_path, 'r') as rar_ref:
                    for name in rar_ref.namelist():
                        if name.endswith('/'):
                            continue  # pomijamy foldery wewnątrz archiwum
                        source_folder = os.path.split(name)[-2]
                        if any(phrase in source_folder for phrase in phrases):
                            destination_path = os.path.join(destination_folder, os.path.basename(source_folder))
                            if not os.path.exists(destination_path):
                                os.makedirs(destination_path)
                            rar_ref.extract(name, destination_path)
                            num_folders_found += 1
                            print(f"Found and copied folder: {source_folder} -> {destination_path}")

    print(f"\nTotal folders found and copied: {num_folders_found}")

# wczytaj ścieżki i frazy z pliku CSV
def load_csv_data(csv_path):
    data = []
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # pomiń nagłówek
        for row in reader:
            data.append(row[0])  # załóż, że ścieżki znajdują się w pierwszej kolumnie
    return data

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    csv_path = input("Enter the path to the CSV file: ")
    destination_folder = input("Enter the path to the destination folder: ")

    phrases = load_csv_data(csv_path)

    print("\nSearching folders...")
    search_folders(folder_path, phrases, destination_folder)
