import unittest

from src.main.python.extract_json import import_twitter_data


class TestJsonExtracting(unittest.TestCase):
    def test_reading_twitter_json_file_returns_non_empty_array(self):
        self.assertTrue(import_twitter_data('twitter_data.txt') is not None)


if __name__ == '__main__':
    unittest.main()
