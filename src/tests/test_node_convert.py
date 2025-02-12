import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from node_converter import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_normal_eq(self):
        text_node = TextNode("this is text", TextType.NORMAL)
        leaf_node = LeafNode("this is text")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)

    def test_bold_eq(self):
        text_node = TextNode("this is text", TextType.BOLD)
        leaf_node = LeafNode("this is text", "b")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)
    
    def test_italic_eq(self):
        text_node = TextNode("this is text", TextType.ITALIC)
        leaf_node = LeafNode("this is text", "i")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)

    def test_code_eq(self):
        text_node = TextNode("this is text", TextType.CODE)
        leaf_node = LeafNode("this is text", "code")
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)

    def test_link_eq(self):
        url = "http://localhost"
        props = {"href": url}
        text_node = TextNode("this is text", TextType.LINK, url)
        leaf_node = LeafNode("this is text", "a", props)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)

    def test_image_eq(self):
        url = "http://localhost/foo.png"
        props = {"src": url}
        text_node = TextNode("this is text", TextType.IMAGE, url)
        leaf_node = LeafNode("this is text", "img", props)
        converted_node = text_node_to_html_node(text_node)
        self.assertEqual(converted_node, leaf_node)
    
    def test_normal_to_html(self):
        text_node = TextNode("this is text", TextType.NORMAL)
        converted_node = text_node_to_html_node(text_node)
        expected = "this is text"
        self.assertEqual(expected, converted_node.to_html())

    def test_bold_to_html(self):
        text_node = TextNode("this is text", TextType.BOLD)
        converted_node = text_node_to_html_node(text_node)
        expected = "<b>this is text</b>"
        self.assertEqual(expected, converted_node.to_html())

    def test_italic_to_html(self):
        text_node = TextNode("this is text", TextType.ITALIC)
        converted_node = text_node_to_html_node(text_node)
        expected = "<i>this is text</i>"
        self.assertEqual(expected, converted_node.to_html())

    def test_code_to_html(self):
        text_node = TextNode("this is text", TextType.CODE)
        converted_node = text_node_to_html_node(text_node)
        expected = "<code>this is text</code>"
        self.assertEqual(expected, converted_node.to_html())

    def test_link_to_html(self):
        url = "http://localhost"
        props = {"href": url}
        text_node = TextNode("this is text", TextType.LINK, url)
        converted_node = text_node_to_html_node(text_node)
        expected = '<a href="http://localhost">this is text</a>'
        self.assertEqual(expected, converted_node.to_html())

    def test_image_to_html(self):
        url = "http://localhost/foo.png"
        props = {"src": url}
        text_node = TextNode("this is text", TextType.IMAGE, url)
        converted_node = text_node_to_html_node(text_node)
        expected = '<img src="http://localhost/foo.png">this is text</img>'
        self.assertEqual(expected, converted_node.to_html())
