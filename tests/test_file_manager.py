import unittest
from filemover.file_manager import FileHandler


class TestFileHandler(unittest.TestCase):
    def set_up(self):
        dir_path = 'tests/test_files'
        file_handler = FileHandler(dir_path)
        return dir_path, file_handler

    def test_list_files(self):
        dir_path, file_handler = self.set_up()
        files = file_handler.list_files()
        self.assertIsInstance(files, list)
        self.assertEqual(len(files), 3)

    def test_create_hash(self):
        dir_path, file_handler = self.set_up()
        files = file_handler.list_files()
        file_hash_1 = file_handler.create_hash(files[0])
        file_hash_2 = file_handler.create_hash(files[1])
        file_hash_3 = file_handler.create_hash(files[2])
        self.assertEqual(file_hash_2, file_hash_3)
        self.assertNotEqual(file_hash_1, file_hash_3)
        self.assertNotEqual(file_hash_1, file_hash_2)
