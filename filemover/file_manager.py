import hashlib
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
    
    # Function to create hash
    def create_hash(self, file):
        afile = open(os.path.join(self.dir_path, file), 'rb')
        
        hasher = hashlib.md5()
        blocksize=65536
        buffer = afile.read(blocksize)

        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = afile.read(blocksize)
    
        afile.close()
    
        return hasher.hexdigest()
    
    def remove_file(self):
        print('remove')

    def get_weigth_and_compare(self, file_names: list):
        sizes: list = []
        same_file = True
        for file in file_names:
            full_path = os.path.join(self.dir_path,file)
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
