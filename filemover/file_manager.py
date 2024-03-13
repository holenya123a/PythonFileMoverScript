import shutil
import os


class FileHandler:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def list_dirs(self):
        return os.listdir(self.dir_path)

    def move_file(self, destination_path):
        shutil.move(self.dir_path, destination_path)

    def delete_file(self):
        os.remove(self.dir_path)

    def search_duplicates(self, files_list):
        print(type(files_list))

    def remove_duplicates(self):
        print('hello')


file_handler = FileHandler(os.environ['DIR_PATH'])
print(file_handler.dir_path)
dir_path = file_handler.dir_path
list_of_files = file_handler.list_dirs()
print(list_of_files)