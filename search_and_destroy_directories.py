import os
import shutil

# Entering the path to the working directory
folder_path = input("Enter the path to the working directory: ")

# Entering keywords
keywords = input("Enter keywords, separated by space: ")
keywords = keywords.split()

# Variable to store the number of deleted directories
deleted_dirs_count = 0

# Searching folders and deleting directories
for dirname in os.listdir(folder_path):
    dir_path = os.path.join(folder_path, dirname)
    if os.path.isdir(dir_path):
        for keyword in keywords:
            if keyword in dirname:
                shutil.rmtree(dir_path)
                deleted_dirs_count += 1
                break

# Displaying information about the end of work
print("Process finished")
print("Number of deleted directories:", deleted_dirs_count)
print()
input("Press ENTER to finish: ")
exit()
