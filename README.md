# Tutedude_python_assignment4

Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt. - in this the sample.txt file is stored in different location where program is saved
2.   done using open("C:/Users/91997/Desktop/sample.txt", "r")
3.   Prints its content line by line. - done using
4.    for line in file:
        print(line.strip())
5.   Handles errors gracefully if the file does not exist.- done using
6.   except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.: in this the sample.txt file is stored in same location where program is saved
2.   done using     with open("output.txt", "w") as file:
        file.write(input_text + "\n")
3.   Appends additional data to the same file:
4.       with open("output.txt", "a") as file:
        file.write(input_append + "\n")
5.   Reads and displays the final content of the file.:
6.       with open("output.txt", "r") as file:
        print("Final content of output.txt :\n")
        # Read and print each line one by one
        for line in file:
             print(line.strip())
7. except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
