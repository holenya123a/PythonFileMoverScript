import sys
import argparse
import os
from file_manager import FileHandler
from print_options import print_duplicates
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

    files_info = get_duplicates_files(path)
    print_duplicates(files_info)
    print_options()

    choice = input('\nDo you want to (m)ove or (d)elete these files?\n')
    choice = int(choice)

    match choice:
        case 1:
            print('DELETE')
        case 2:
            print('MOVE FILES')
        case 3:
            print('\n   ----------BYE-------------')
            sys.exit()


def get_duplicates_files(path: str):

    files_info: dict = {}
    file_handler: FileHandler = FileHandler(path)
    files: list = file_handler.list_files()
    keys_to_delete: dict = {}

    for file in files:
        file_hash = file_handler.create_hash(file)

        if file_hash not in files_info:
            keys_to_delete[file_hash] = None
            files_info[file_hash] = [file]
        else:
            del keys_to_delete[file_hash]
            files_info[file_hash].append(file)

    for key in keys_to_delete:
        del files_info[key]

    return files_info


args = parser.parse_args()
dir_path = args.path
main(dir_path)
