# This script scans the file names in the specified folder and groups them based on
# the first 10 identical characters in the file name. It then displays information
# about the found duplicate groups and the full file names in each group.

import os
from collections import defaultdict

# Get the folder path
folder_path = input("Enter the path to the folder you want to work with: ")
print()

# Dictionary to store file groups
file_groups = defaultdict(list)

# Traverse the folder and group the files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        group_key = filename[:10]  # First 10 characters as the group key
        file_groups[group_key].append(filename)

# Display information about groups and their files
group_count = 0
for group_key, file_names in file_groups.items():
    group_count += 1
    print(f"Duplicate Group {group_count}:")
    for file_name in file_names:
        print(file_name)
    print()
