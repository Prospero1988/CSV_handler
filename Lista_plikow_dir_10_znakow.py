# -*- coding: cp1250 -*-

# Skrypt tworzy liste wszystkich plikow w danym katalogu i zapisuje ją 
# do pliku csv jako jedna kolumne. Skrypt kopiuje tylko pierwsze 10 znakow
# z nazwy kazdego pliku.

import os
import csv

# Step 1: Prompt for the working directory
directory = input("Enter the working directory: ")

# Step 2: Get a list of all files in the specified directory
file_list = os.listdir(directory)

# Step 3: Prompt for the output CSV file name
output_file = input("Enter the name of the output CSV file: ")

# Step 4: Write the list of files to the CSV file, saving only the first 10 characters of each file name
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for file_name in file_list:
        short_name = file_name[:10]
        writer.writerow([short_name])

print("CSV file created successfully!")
