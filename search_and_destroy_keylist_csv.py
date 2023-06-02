import os
import csv
import shutil

def remove_directories_and_files(directory_path, keywords_file):
    # Load keywords from CSV file
    with open(keywords_file, 'r') as file:
        reader = csv.reader(file)
        keywords = set(row[0].strip().lower() for row in reader)

    removed_directories = 0
    removed_files = 0

    # Iterate over all directories and files in the specified directory
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for directory in dirs:
            directory_path = os.path.join(root, directory)
            directory_name = os.path.basename(directory_path)

            # Check if any keyword is present in the directory name
            if any(keyword in directory_name.lower() for keyword in keywords):
                # Remove the directory and all its contents
                shutil.rmtree(directory_path)
                removed_directories += 1

        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if any keyword is present in the file name
            if any(keyword in file_name.lower() for keyword in keywords):
                # Remove the file
                os.remove(file_path)
                removed_files += 1

    # Print the summary
    print("Finished.")
    print("Removed directories:", removed_directories)
    print("Removed files:", removed_files)

# Prompt the user for directory and keywords file paths
directory_path = input("Enter the directory path: ")
keywords_file = input("Enter the keywords CSV file path: ")

# Call the function to remove directories and files
remove_directories_and_files(directory_path, keywords_file)
