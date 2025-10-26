# Task 1: Read a File and Handle Errors

try:
    # Try to open the file in read mode
    file = open("C:/Users/91997/Desktop/sample.txt", "r")
    print("Reading file content:\n")
    # Read and print each line one by one
    for line in file:
        print(line.strip())
except FileNotFoundError:
    # Handle the case when file is not found
    print("Error: The file 'sample.txt' was not found.")