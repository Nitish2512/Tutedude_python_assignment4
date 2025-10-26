#Task2:

try:
    # Try to write in the file in write mode
    input_text = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(input_text + "\n")

    print("Data successfully written to output.txt .\n")

    input_append = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(input_append + "\n")
    
    print("Data successfully appended .\n")

    with open("output.txt", "r") as file:
        print("Final content of output.txt :\n")
        # Read and print each line one by one
        for line in file:
             print(line.strip())

except FileNotFoundError:
    # Handle the case when file is not found
    print("Error: The file 'sample.txt' was not found.")