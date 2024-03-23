import hashlib
import shutil
import os


class FileHandler:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def list_files(self):
        return os.listdir(self.dir_path)

    def move_file(self, destination_path):
        shutil.move(self.dir_path, destination_path)

    def delete_file(self):
        os.remove(self.dir_path)

    # Function to create hash
    def create_hash(self, file: str):

        afile = open(os.path.join(self.dir_path, file), 'rb')
        hasher = hashlib.md5()
        blocksize = 65536
        buffer = afile.read(blocksize)

        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = afile.read(blocksize)

        afile.close()

        return hasher.hexdigest()

    def remove_file(self, file_name: str):
        '''
        Removes a file given its filename.
        Parameters:
        file_name (str) -- The name of the file to be removed.
        Returns:
        str -- A message indicating the status of the file deletion.
        '''
        try:
            os.remove(os.path.join(self.dir_path, file_name))
            return f'File({file_name}) deleted successfully.'

        except FileNotFoundError:
            return f'No such file {file_name} exists.'

        except PermissionError:
            return f'You do not have permission to delete file: {file_name}'

    def get_weigth_and_compare(self, file_names: list):
        sizes: list = []
        same_file = True
        for file in file_names:
            full_path = os.path.join(self.dir_path, file)
            try:
                size = os.path.getsize(full_path)
            except OSError:
                print('cant obtain the weigth of the file')
                pass

            if len(sizes) > 0:
                if size in sizes:
                    sizes.append(size)
                else:
                    same_file = False
                    return same_file
            else:
                sizes.append(size)
        return same_file


file_hander = FileHandler(os.environ['DIR_PATH'])
files = file_hander.list_files()
file_hander.create_hash(files[0])
