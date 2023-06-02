import os
from collections import defaultdict

# Get the folder path
folder_path = input("Enter the path to the folder you want to work with: ")
print()

# Dictionary to store folder groups
folder_groups = defaultdict(list)

# Traverse the folder and group the folders
for folder_name in os.listdir(folder_path):
    folder_dir = os.path.join(folder_path, folder_name)
    if os.path.isdir(folder_dir):
        group_key = folder_name[:10]  # First 10 characters as the group key
        folder_groups[group_key].append(folder_name)

# Display information about groups and folders
group_count = 0
for group_key, folder_names in folder_groups.items():
    group_count += 1
    print(f"Duplicate Folder Group {group_count}:")
    for folder_name in folder_names:
        print(folder_name)
    print()
