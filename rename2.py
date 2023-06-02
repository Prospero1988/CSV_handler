# Skrypt pracuj¹c w danym katalogu zmienia nazwy wszystkich plików. Zostawia 
# tylko pierwsze 10 znaków i nastepnie dodaje do nazwy suffix '-1_norm.jdf'

import os

# 1. Ask for the working directory
directory = input("Please enter the directory: ")

# 2. Rename files
count = 0  # Counter for renamed files

for filename in os.listdir(directory):
    if len(filename) > 10:
        new_filename = filename[:10] + "-1_norm.jdf"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        count += 1

# 3. Display the number of renamed files
print("Number of files renamed: ", count)
