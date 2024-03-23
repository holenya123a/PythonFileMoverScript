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
        self.assertEqual(len(files), 2)
