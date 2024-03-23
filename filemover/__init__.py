from file_manager import FileHandler
import argparse
import os


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


def print_options():
    print('\n   ---------OPTIONS----------')
    print('\n   1. DELETE DUPLICATES')
    print('\n   2. MOVE DUPLICATES')
    print('\n   3. EXIT')


def print_duplicates(files_info: dict):
    value: str = ''
    print('\n   -----DUPLICATED FILES-----')
    for key in files_info:
        for name in files_info[key]:
            value += f'{name}, '
            value = value[:-2]
            print(f'\n   {value}')
            value = ''
    print('\n   --------------------------')


args = parser.parse_args()
dir_path = args.path
main(dir_path)
