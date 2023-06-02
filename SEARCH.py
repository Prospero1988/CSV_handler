import subprocess
import os

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Generate message
    print()
    print()
    print("         |--------------------------------------|")
    print("         |------------SEARCH script-------------|")
    print("         |----for NMR data sets in CSV files----|")
    print("         |--------------------------------------|")
    print("         |-by Arkadiusz Leniak -----------------|")
    print("         |-arek.kein@gmail.com -----------------|")
    print("         |--------------------------------------|")
    print()
    print()
    print()
    print(" >> 1. Search for FILES in the defined location based on the keyword list from ")
    print("       the .csv file and then copy them to the defined folder on the drive.")
    print()
    print(" >> 2. Search for FOLDERS in the defined location based on the keyword list from ")
    print("       the .csv file. The names of the searched folders end in '.fid' suffix.")
    print("       The script then copies the found folders to the defined location on the drive.")
    print()
    print(" >> 3. Like option 2, but it also searches for folders packed in .rar and .zip archives.")
    print()
    print(" >> 4. Remove from the defined folder all files that contain the ")
    print("       specified keywords in their names.")
    print()
    print(" >> 5. Group all files in a folder by the identical first 10 characters ")
    print("       in their names.")
    print()
    print(" >> 6. Group all FOLDERS in a directory by the identical first 10 characters ")
    print("       in their names.")
    print()
    print(" >> 0. Exit")

    print()
    choice = input("Choose what you want to do: ")
    print()

    if choice == '1':
        subprocess.call(['python', 'search_and_copy.py'])
    elif choice == '2':
        subprocess.call(['python', 'search_and_copy_folders.py'])
    elif choice == '3':
        subprocess.call(['python', 'search_and_copy_folders_also_in_archives.py'])
    elif choice == '4':
        subprocess.call(['python', 'search_and_destroy.py'])
    elif choice == '5':
        subprocess.call(['python', 'search_duplicates_files.py'])
    elif choice == '6':
        subprocess.call(['python', 'search_duplicates_dirs.py'])
    elif choice == '0':
        print()
        print("Exit selected. End of program.")
        print()
        break  # Przerwanie pętli while
    else:
        print()
        print("Incorrect selection. Try again.")
        print()
