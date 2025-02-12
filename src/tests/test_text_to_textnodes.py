import unittest

from textnode import TextNode, TextType
from node_helpers import text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_bold(self):
        text = "This is **bold text** for testing!"
        expected = [
                TextNode("This is ", TextType.NORMAL),
                TextNode("bold text", TextType.BOLD),
                TextNode(" for testing!", TextType.NORMAL)
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)

    def test_all_texttypes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)
