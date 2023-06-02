# -*- coding: cp1250 -*-

# Skrypt porównuje dwa pliki .csv pod katem pierwszej kolumny i
# generuje trzeci plik, ktory zawiera tylko wiersze, ktore nie sa 
# wspolne dla pierwszych kolumn obu pierwotnych plikow .csv

import csv

def compare_csv_files(file1, file2):
    rows_file1 = set()
    rows_file2 = set()

    with open(file1, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows_file1.add(row[0])

    with open(file2, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows_file2.add(row[0])

    unique_rows = rows_file1.symmetric_difference(rows_file2)

    return unique_rows

def write_output_file(output_file, rows):
    with open(output_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow([row])

# Get file paths from the user
file1_path = input("Enter the path to the first CSV file: ")
file2_path = input("Enter the path to the second CSV file: ")

# Compare the files
unique_rows = compare_csv_files(file1_path, file2_path)

# Save the results to the output file
output_file_path = input("Enter a name for the output file (without extension): ") + ".csv"
write_output_file(output_file_path, unique_rows)

print("The file", output_file_path, "has been generated with the list of unique rows.")
