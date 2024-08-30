import os

def rename_file():
    # Prompt the user for the necessary inputs
    date = input("Enter the date in YYYYMMDD format: ")
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    assignment_number = input("Enter the assignment number: ")

    # Construct the new file name
    new_file_name = f"{date}_{last_name}{first_name}_Assignment{assignment_number}_TechnicalDocumentation.docx"

    # Get the current working directory
    current_directory = os.getcwd()

    # Find the file in the current directory
    files = os.listdir(current_directory)
    docx_files = [file for file in files if file.endswith('.docx')]

    if not docx_files:
        print("No .docx files found in the current directory.")
        return

    # Assuming there's only one .docx file to rename
    current_file_name = docx_files[0]

    # Rename the file
    os.rename(current_file_name, new_file_name)
    print(f"File has been renamed to: {new_file_name}")

# Call the function
rename_file()
