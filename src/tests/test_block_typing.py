import unittest
from node_helpers import block_to_block_type

class BlockTypeTest(unittest.TestCase):
    def test_header(self):
        markdown = "# header text"
        expected = "heading"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_header_multiple_hashs(self):
        markdown = "###### header text"
        expected = "heading"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_code(self):
        markdown = "```code text```"
        expected = "code"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_code_multiple_lines(self):
        markdown = "```\ncode text\n```"
        expected = "code"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_quote(self):
        markdown = ">quote text"
        expected = "quote"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_quote_multiple_lines(self):
        markdown = ">quote\n>text"
        expected = "quote"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_invalid_quote(self):
        markdown = ">invalid\nquote\n>text"
        expected = "paragraph"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_asterisk(self):
        markdown = "* unordered\n* list"
        expected = "unordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_hyphen(self):
        markdown = "- unordered\n- list"
        expected = "unordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_mixed(self):
        markdown = "* unordered\n- list"
        expected = "unordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_more_lines(self):
        markdown = "* unordered\n- list\n* more\n- lines"
        expected = "unordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_invalid_unordered_list(self):
        markdown = "* unordered\nlist\n* more"
        expected = "paragraph"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_ordered_list_one_line(self):
        markdown = "1. only one line"
        expected = "ordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_ordered_list_three_lines(self):
        markdown = "1. first\n2. second\n3. third"
        expected = "ordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_ordered_list_eleven_lines(self):
        markdown = "1. first\n2. second\n3. third\n4. fourth\n5. fifth\n6. sixth\n7. seventh\n8. eighth\n9. ninth\n10. tenth\n11. eleventh"
        expected = "ordered list"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_invalid_ordered_list(self):
        markdown = "1. first\n3. second\n2. third"
        expected = "paragraph"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_paragraph(self):
        markdown = "just a paragraph"
        expected = "paragraph"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)

    def test_paragraph_more_lines(self):
        markdown = "just a paragraph\nbut with more lines"
        expected = "paragraph"
        actual = block_to_block_type(markdown)
        self.assertEqual(expected, actual)
