# Reads the contents of a file and prints them

import os


file_path = 'guests.txt'  # Change this to your file path

try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

    dir_name = os.getcwd()
    print(f"Current directory: {dir_name}")
    