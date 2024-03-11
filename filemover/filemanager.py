import shutil
import os

class FileHandler:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def move_file(self, destination_path):
        shutil.move(self.file_path, destination_path)

    def delete_file(self):
        os.remove(self.file_path)
    
    