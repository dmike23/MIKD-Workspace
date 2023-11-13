import os
import re

def find_string_in_file(file_path, search_string):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for row_number, line in enumerate(file, 1):
            if re.search(search_string, line):
                results.append(row_number)
    return results

def search_for_string_in_files(folder_path, search_string, extensions=['.ktr', '.kjb']):
    found_occurrences = {}
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(tuple(extensions)):
                file_path = os.path.join(root, file_name)
                occurrences = find_string_in_file(file_path, search_string)
                if occurrences:
                    found_occurrences[file_path] = occurrences
    return found_occurrences

if __name__ == "__main__":
    folder_to_search = "MIKD_CivilCommon_N"  # Change this to the folder you want to search in
    search_string = r"\bOutputFile\b"    # string to search for

    results = search_for_string_in_files(folder_to_search, search_string)

    if results:
        print("Occurrences found in the following files:")
        for file_path, occurrences in results.items():
            print(f"File: {file_path}")
            print(f"Row Numbers: {', '.join(map(str, occurrences))}\n")
    else:
        print("No occurrences found in the files.")
