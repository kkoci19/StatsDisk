import os
import threading
import psutil

def guess_size(path):
    tot_size = 0
    for directory_path, directory_names, file_names in os.walk(path):
        for file_name in file_names:
            file_path = os.path.join(directory_path, file_name)
            try:
                tot_size += os.path.getsize(file_path)
            except FileNotFoundError:
                pass
    return tot_size

def print_folder_stats(path):
    tot_size = guess_size(path)
    print(f"Folder stats found: path={path}, size={tot_size} bytes")

def find_directory(path):
    for directory_path, directory_names, file_names in os.walk(path):
        for directory_name in directory_names:
            folder_path = os.path.join(directory_path, directory_name)
            t = threading.Thread(target=print_folder_stats, args=(folder_path,))
            t.start()

if __name__ == "__main__":
    directory_path = input("Enter the directory path to find: ")
    if not os.path.isdir(directory_path):
        print("Directory path not found!")
    else:
        print(f"Finding directory: {directory_path}")
        find_directory(directory_path)
