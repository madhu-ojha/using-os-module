# Program to get metadata of files
import os


def get_file_info(filename):
    info = os.stat(filename)
    return {
        'Size': info.st_size,
        'Permissions': oct(info.st_mode & 0o777),
        'Last Accessed': info.st_atime,
        'Last Modified': info.st_mtime,
    }


# Example usage:
file_to_check = input("Enter path of file:")
file_info = get_file_info(file_to_check)
print("File Information:")
for key, value in file_info.items():
    print(f"{key}: {value}")
