#  Program to check if a file exists and then read its contents
import os


def main():
    # Define the file path
    file_path = '/path/to/your/file.txt'

    # Check if the file exists
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")

        # Read content from the file
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    else:
        print(f"The file '{file_path}' does not exist.")


if __name__ == "__main__":
    main()
