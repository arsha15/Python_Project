import os
os.path.exists("guests.txt")
file_path = os.path.abspath("guests.txt")
print("Absolute file path:", file_path)
file_size = os.path.getsize("guests.txt")
print("File size in bytes:", file_size)