# Skrypt do zmiany nazw plikow w katalogu. Skrypt usuwa pewnia ilosc znakow z poczatku nazwy 
# kazdego pliku w katalogu. SKrypt pyta ile znakow usunac.

import os

# Step 1: Ask for the directory to work in
directory = input("Enter the path to the directory you want to work in: ")

# Step 2: Ask for the number of characters to remove
num_chars = int(input("Enter the number of characters to remove from the beginning of the file names: "))

# Step 3: Rename files in the directory
changed_files = 0

for filename in os.listdir(directory):
    if filename.startswith(".") or os.path.isdir(os.path.join(directory, filename)):
        # Ignore files starting with a dot (e.g., hidden files) and directories
        continue
    
    new_filename = filename[num_chars:]
    if new_filename != filename:
        # Rename the file only if it's different from the original
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        changed_files += 1

# Step 4: Display the number of renamed files
print(f"Number of files whose names were changed: {changed_files}")
