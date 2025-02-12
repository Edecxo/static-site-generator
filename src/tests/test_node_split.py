import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from node_helpers import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_straightforward_case(self):
        node = TextNode("this is *italic* text", TextType.NORMAL)
        expected = [
                TextNode("this is ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.NORMAL)
        ]
        actual = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_multiple_nodes(self):
        node1 = TextNode("this is `the first` node", TextType.NORMAL)
        node2 = TextNode("this is `the second` node", TextType.NORMAL)
        nodes = [node1, node2]
        expected = [
                TextNode("this is ", TextType.NORMAL),
                TextNode("the first", TextType.CODE),
                TextNode(" node", TextType.NORMAL),
                TextNode("this is ", TextType.NORMAL),
                TextNode("the second", TextType.CODE),
                TextNode(" node", TextType.NORMAL)
        ]
        actual = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_no_delimiters(self):
        node = TextNode("no delimiters", TextType.NORMAL)
        expected = [node]
        actual = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(expected, actual)

    def test_unmatched_delimiters(self):
        node = TextNode("*unmatched* *delimiters", TextType.NORMAL)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_wrong_texttype(self):
        node = TextNode("this is `text`", TextType.ITALIC)
        expected = [node]
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_delimiters_at_beginning(self):
        node = TextNode("`this` is text", TextType.NORMAL)
        expected = [
                TextNode("this", TextType.CODE),
                TextNode(" is text", TextType.NORMAL)
        ]
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_delimiters_at_end(self):
        node = TextNode("this is `text`", TextType.NORMAL)
        expected = [
                TextNode("this is ", TextType.NORMAL),
                TextNode("text", TextType.CODE)
        ]
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_delimiters_in_multiple_places(self):
        node = TextNode("`this` is `text`", TextType.NORMAL)
        expected = [
                TextNode("this", TextType.CODE),
                TextNode(" is ", TextType.NORMAL),
                TextNode("text", TextType.CODE)
        ]
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(expected, actual)

    def test_bold(self):
        node = TextNode("this is **text**", TextType.NORMAL)
        expected = [
                TextNode("this is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD)
        ]
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(expected, actual)

    def test_italic(self):
        node = TextNode("this is *text*", TextType.NORMAL)
        expected = [
                TextNode("this is ", TextType.NORMAL),
                TextNode("text", TextType.ITALIC)
        ]
        actual = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(expected, actual)
