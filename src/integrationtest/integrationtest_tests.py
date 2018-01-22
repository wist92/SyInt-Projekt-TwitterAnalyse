import unittest
import os.path
from util import delete_txt_and_png


class TestUtil(unittest.TestCase):
    def test_dir_is_empty_after_delete_method(self):
        delete_txt_and_png()
        self.assertTrue(not item.endswith(".png") and not item.endswith(".txt")for item in os.listdir('.'))


if __name__ == '__main__':
    unittest.main()
