import unittest
import os.path
import mockito
import pandas
from extract_json import import_twitter_data,create_plot


class TestJsonExtracting(unittest.TestCase):
    def test_reading_twitter_json_file_returns_non_empty_array(self):
        self.assertTrue(import_twitter_data('twitter_data.txt') is not None)

    def test_plot_creation_sould_be_successful(self):
        test = pandas.DataFrame()
        test['hashtag'] = ['hallo', 'u', 'suck']
        c = test['hashtag'].value_counts()
        create_plot(c, 'Test', 'hallo_u_suck')
        self.assertTrue(os.path.exists('hallo_u_suck_top_Test.png'))


if __name__ == '__main__':
    unittest.main()
