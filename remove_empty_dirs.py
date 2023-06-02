import os

def remove_empty_directories(directory):
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return

    for root, dirs, files in os.walk(directory, topdown=False):
        for name in dirs:
            path = os.path.join(root, name)
            if not os.listdir(path):
                os.rmdir(path)
                print(f"Removed empty directory: {path}")

def main():
    directory = input("Enter the working directory: ")
    remove_empty_directories(directory)

if __name__ == "__main__":
    main()

