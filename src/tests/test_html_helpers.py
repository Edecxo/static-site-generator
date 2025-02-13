import unittest
from html_helpers import *

class HTMLHelpers(unittest.TestCase):
    def test_basic_title(self):
        markdown = "# This is a title"
        expected = "This is a title"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)
    
    def test_title_multiple_lines(self):
        markdown = "# This is\na title"
        expected = "This is\na title"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)
