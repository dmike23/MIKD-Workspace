import os

# Specify the folder path containing the text files
folder_path = '2018 - 2022 Files'

# Create a dictionary to store extracted values and their corresponding files
extracted_values = {}

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Read the file
    with open(file_path, 'r') as file:
        # Skip the header row
        next(file)

        for line in file:
            # Extract values from spaces 5 and 6
            value1 = line[5]
            value2 = line[6]

            # Create a unique key combining the two values
            key = value1 + value2

            # Check if the key exists in the dictionary
            if key in extracted_values:
                # If the key exists, update the set of filenames
                extracted_values[key].add(filename)
            else:
                # If the key is encountered for the first time, add it to the dictionary
                extracted_values[key] = {filename}

# Print the extracted values and their corresponding files
for key, file_names in extracted_values.items():
    print("Values:", key)
    print("Files:", file_names)
    print()
