import sys
import argparse
import os
from file_manager import FileHandler
from print_options import print_duplicates, print_exit
from print_options import print_options


parser = argparse.ArgumentParser(
    prog='FileMoverScript',
    description='detect duplicates and move or delete them')

parser.add_argument('-p', '--path', type=str,
                    help='path to the designed directory')


def main(path=None):
    if path is None:
        try:
            path = os.environ['DIR_PATH']
        except KeyError:
            print(
                "The environment variable 'DIR_PATH' is not defined.")
            return

    files_info, file_handler = get_duplicates_files(path)

    if len(files_info) == 0:
        print_exit()
        sys.exit()

    print_duplicates(files_info)
    print_options()

    choice = input('\nDo you want to (m)ove or (d)elete these files?\n')
    choice = int(choice)
    last_files: list = []

    match choice:
        case 1:
            # Iterate through each key in the files_info dictionary
            for key in files_info:
                # Get the value corresponding to the current key
                value = files_info[key]
                # Get the most recent file from the list of files (value)
                last_value = file_handler.get_last_recent(value)
                # Append the most recent file to the last_files list
                last_files.append(last_value)

            for key in files_info:
                value = files_info[key]
                response = file_handler.delete_file(value, last_files)
                print(response)
        case 2:
            print('MOVE FILES')
        case 3:
            print('\n   ----------BYE-------------')
            sys.exit()


def get_duplicates_files(path: str):
    """
        Finds duplicate files within a directory specified by the given path.
        Args:
            path (str): The path to the directory containing the files.
        Returns:
            tuple: A tuple containing:
                - A dictionary containing information about duplicate files,
                where the keys are file hashes and the values are lists of
                file names with the same hash.
                - A FileHandler object initialized with the specified path.
    """

    # Dictionary to store file information
    files_info: dict = {}

    # Initialize file handler
    file_handler: FileHandler = FileHandler(path)

    # Get list of files in the directory
    files: list = file_handler.list_files()

    # Iterate through each file in the directory
    for file in files:
        # Calculate hash for the file
        file_hash = file_handler.create_hash(file)

        # Check if hash already exists in files_info dictionary
        if file_hash not in files_info:
            # If not, add a new entry with the file name as a list
            files_info[file_hash] = [file]
        else:
            # If yes, append the file name to the existing list
            files_info[file_hash].append(file)

    # List to store keys to be deleted from the dictionary
    keys_to_delete: list = []

    # Iterate through the keys in the files_info dictionary
    for key in files_info:
        # Get the value corresponding to the key
        value = files_info[key]

        # If the list contains less than 2 elements (i.e., not duplicates)
        if len(value) < 2:
            # Add the key to the list of keys to delete
            keys_to_delete.append(key)

    # Delete dictionary items corresponding to keys_to_delete
    for key in keys_to_delete:
        del files_info[key]

    # Return the dictionary containing duplicate files information
    # and file handler object
    return files_info, file_handler


args = parser.parse_args()
dir_path = args.path
main(dir_path)
