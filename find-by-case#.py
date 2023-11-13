import os

def get_text_file_names(case_number):
    folder_path = '2018 - 2022 Files'  # Specify the folder path containing the text files

    matching_files = []  # List to store the matching file names

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as file:
            for line in file:
                # Extract the case number from position 1 to 15
                file_case_number = line[0:15].strip()

                if file_case_number == case_number:
                    matching_files.append(filename)

    return matching_files


# Example usage
case_number = input("Enter the case number: ")

matching_files = get_text_file_names(case_number)

if len(matching_files) > 0:
    print("Matching Text Files:")
    for file_name in matching_files:
        print(file_name)
else:
    print("No matching text files found.")
