import hashlib
import shutil
import os


class FileHandler:
    '''
    A class to handle files in a directory.
    Attributes:
    dir_path (str): The path to the directory where files are handled.
    '''

    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def list_files(self):
        '''
        List all files in the directory.
        Returns:
        list: A list of filenames in the directory.
        '''
        return os.listdir(self.dir_path)

    def move_file(self, destination_path):
        '''
        Move the files in the directory to a specified destination.
        Parameters:
        destination_path (str): The path to move the files to.
        '''
        shutil.move(self.dir_path, destination_path)

    # Function to create hash
    def create_hash(self, file: str):
        '''
        Create the MD5 hash of a file.
        Parameters:
        file (str): The name of the file for which to create the hash.
        Returns:
        str: The MD5 hash of the file.
        '''
        # Open the file in binary mode
        with open(os.path.join(self.dir_path, file), 'rb') as afile:
            # Initialize the MD5 hasher
            hasher = hashlib.md5()
            # Set the blocksize for reading the file
            blocksize = 65536
            # Read the file in chunks and update the hasher
            buffer = afile.read(blocksize)
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = afile.read(blocksize)

        # Close the file
        afile.close()

        # Return the hexadecimal digest of the hash
        return hasher.hexdigest()

    def delete_file(self, file_name: str):
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
        '''
        Compare the sizes of files given their filenames.

        Parameters:
        file_names (list): A list of filenames to compare.

        Returns:
        bool: True if all files have the same size, False otherwise.
        '''
        # Initialize an empty list to store file sizes
        sizes: list = []

        # Flag to indicate if all files have the same size
        same_file = True

        # Iterate through each file name
        for file in file_names:
            # Construct the full path to the file
            full_path = os.path.join(self.dir_path, file)

            try:
                # Get the size of the file
                size = os.path.getsize(full_path)
            # If there's an error obtaining the file size
            except OSError:
                # print a message and continue
                print('Can\'t obtain the weight of the file')
                continue

            # Check if sizes list is not empty
            if len(sizes) > 0:
                # Check if the size is already in the sizes list
                if size in sizes:
                    sizes.append(size)
                # If the size is not in the sizes list
                else:
                    # set the same_file flag to False and return
                    same_file = False
                    return same_file
            # If sizes list is empty
            else:
                # add the size to the list
                sizes.append(size)

        # Return the same_file flag
        return same_file
