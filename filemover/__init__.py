import argparse
from file_manager import FileHandler
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
            print("The environment variable 'DIR_PATH' is not defined.")
            return

    file_handler = FileHandler(path)
    files = file_handler.list_files()


args = parser.parse_args()
dir_path = args.path
print(dir_path, '<____ dir path')
main(dir_path)
