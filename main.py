def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Could not read the file.")

# Run the function
read_and_modify_file()

