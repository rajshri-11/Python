# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text.\n")
    file.write("And here is another line.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending a new line to the file.")

# Reading lines from a file
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nFile Lines:")
    for line in lines:
        print(line.strip())

# Using 'with' statement for file I/O automatically closes the file

# Copying content from one file to another
with open("example.txt", "r") as source_file, open("copy.txt", "w") as dest_file:
    dest_file.write(source_file.read())

# Reading binary data from a file
with open("example.jpg", "rb") as binary_file:
    binary_data = binary_file.read()
    print("\nBinary Data Length:", len(binary_data))

# Writing binary data to a new file
with open("copy.jpg", "wb") as new_binary_file:
    new_binary_file.write(binary_data)

# Handling exceptions when working with files
try:
    non_existent_file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("\nFile not found!")

# Using 'try' and 'finally' to ensure file closure
try:
    file_to_close = open("to_close.txt", "w")
    file_to_close.write("This file needs to be closed explicitly.")
finally:
    file_to_close.close()

# Checking if a file exists
import os

if os.path.exists("example.txt"):
    print("\nThe file 'example.txt' exists.")
else:
    print("\nThe file 'example.txt' does not exist.")
