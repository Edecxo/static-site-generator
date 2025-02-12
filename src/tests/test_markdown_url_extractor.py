import unittest

from node_helpers import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_basic_image(self):
        string = "![alt text](http://url.com/picture.png)"
        expected = [("alt text", "http://url.com/picture.png")]
        actual = extract_markdown_images(string)
        self.assertEqual(expected, actual)

    def test_basic_link(self):
        string = "[link text](http://url.com/)"
        expected = [("link text", "http://url.com/")]
        actual = extract_markdown_links(string)
        self.assertEqual(expected, actual)

    def test_no_image_found(self):
        string = "nothing here"
        expected = []
        actual = extract_markdown_images(string)
        self.assertEqual(expected, actual)

    def test_no_links_found(self):
        string = "nothing here"
        expected = []
        actual = extract_markdown_links(string)
        self.assertEqual(expected, actual)

    def test_multiple_images(self):
        string = "check out this picture! ![alt text](http://url.com/picture.png), oh and this one too ![other picture](http://pictures.org/cat.jpg)"
        expected = [("alt text", "http://url.com/picture.png"), ("other picture", "http://pictures.org/cat.jpg")]
        actual = extract_markdown_images(string)
        self.assertEqual(expected, actual)

    def test_multiple_links(self):
        string = "check out this page! [link text](http://url.com/), oh and this one too [other link](http://internet.net/)"
        expected = [("link text", "http://url.com/"), ("other link", "http://internet.net/")]
        actual = extract_markdown_links(string)
        self.assertEqual(expected, actual)
