import unittest

from node_helpers import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_multiple_blank_lines(self):
        markdown = "# This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_leading_whitespace(self):
        markdown = "       # This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_tailing_whitespace(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item       "
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_whitespace_leading_at_center_block(self):
        markdown = "# This is a heading\n\n        This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_whitespace_tailing_at_center_block(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.       \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected = [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)
