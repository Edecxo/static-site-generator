import unittest
from node_helpers import text_to_children, markdown_to_html_node
from htmlnode import HTMLNode, LeafNode

class TextToChildren(unittest.TestCase):
    def test_all_plain(self):
        markdown = "Hello world"
        expected = [
                LeafNode("Hello world")
        ]
        actual = text_to_children(markdown)
        self.assertEqual(expected, actual)

    def test_all_bold(self):
        markdown = "**Hello world**"
        expected = [
                LeafNode("Hello world", "b")
        ]
        actual = text_to_children(markdown)
        self.assertEqual(expected, actual)

    def test_mix_plain_bold(self):
        markdown = "Hello **world**"
        expected = [
                LeafNode("Hello "),
                LeafNode("world", "b")
        ]
        actual = text_to_children(markdown)
        self.assertEqual(expected, actual)

    def test_mix_plain_italic_image(self):
        markdown = "Here's *me*: ![click pick](http://pic.me/catfish.jpg)"
        expected = [
                LeafNode("Here's "),
                LeafNode("me", "i"),
                LeafNode(": "),
                LeafNode("click pick", "img", {"src": "http://pic.me/catfish.jpg"})
        ]
        actual = text_to_children(markdown)
        self.assertEqual(expected, actual)

    def test_mix_code_link(self):
        markdown = "`Code I wrote`, and here's the [link](http://code.me/repo)"
        expected = [
                LeafNode("Code I wrote", "code"),
                LeafNode(", and here's the "),
                LeafNode("link", "a", {"href": "http://code.me/repo"})
        ]
        actual = text_to_children(markdown)
        self.assertEqual(expected, actual)

class MarkdownToHTMLNode(unittest.TestCase):
    def test_heading_h1(self):
        markdown = "# small heading"
        leaf_nodes = [
                LeafNode("small heading")
        ]
        heading_node = HTMLNode("h1", None, leaf_nodes)
        expected = HTMLNode("div", None, [heading_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_heading_h6(self):
        markdown = "###### big heading"
        leaf_nodes = [
                LeafNode("big heading")
        ]
        heading_node = HTMLNode("h6", None, leaf_nodes)
        expected = HTMLNode("div", None, [heading_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_heading_inline_bold(self):
        markdown = "# **small** heading"
        leaf_nodes = [
                LeafNode("small", "b"),
                LeafNode(" heading")
        ]
        heading_node = HTMLNode("h1", None, leaf_nodes)
        expected = HTMLNode("div", None, [heading_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_code_one_line(self):
        markdown = "```code```"
        leaf_nodes = [
                LeafNode("code")
        ]
        code_node = HTMLNode("code", None, leaf_nodes)
        expected = HTMLNode("div", None, [code_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_code_multiple_lines(self):
        markdown = "```\ncode\n```"
        leaf_nodes = [
                LeafNode("code")
        ]
        code_node = HTMLNode("code", None, leaf_nodes)
        expected = HTMLNode("div", None, [code_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_code_inline_bold(self):
        markdown = "```\ncode\n**bold code**```"
        leaf_nodes = [
                LeafNode("code\n"),
                LeafNode("bold code", "b")
        ]
        code_node = HTMLNode("code", None, leaf_nodes)
        expected = HTMLNode("div", None, [code_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_one_item(self):
        markdown = "* unordered list"
        leaf_nodes = [
                LeafNode("unordered list")
        ]
        list_items = [
                HTMLNode("li", None, leaf_nodes)
        ]
        unordered_list_node = HTMLNode("ul", None, list_items)
        expected = HTMLNode("div", None, [unordered_list_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_one_item_inline_bold_and_italic(self):
        markdown = "* *unordered* **list**"
        leaf_nodes = [
                LeafNode("unordered", "i"),
                LeafNode(" "),
                LeafNode("list", "b")
        ]
        list_items = [
                HTMLNode("li", None, leaf_nodes)
        ]
        unordered_list_node = HTMLNode("ul", None, list_items)
        expected = HTMLNode("div", None, [unordered_list_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_unordered_list_three_items(self):
        markdown = "- big **ol**\n* `unordered`\n* *list*"
        first_leaf_nodes = [
                LeafNode("big "),
                LeafNode("ol", "b")
        ]
        second_leaf_nodes = [
                LeafNode("unordered", "code")
        ]
        third_leaf_nodes = [
                LeafNode("list", "i")
        ]
        list_items = [
                HTMLNode("li", None, first_leaf_nodes),
                HTMLNode("li", None, second_leaf_nodes),
                HTMLNode("li", None, third_leaf_nodes)
        ]
        unordered_list_node = HTMLNode("ul", None, list_items)
        expected = HTMLNode("div", None, [unordered_list_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_ordered_list_one_item(self):
        markdown = "1. unordered list"
        leaf_nodes = [
                LeafNode("unordered list")
        ]
        list_items = [
                HTMLNode("li", None, leaf_nodes)
        ]
        unordered_list_node = HTMLNode("ol", None, list_items)
        expected = HTMLNode("div", None, [unordered_list_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_ordered_list_three_items(self):
        markdown = "1. big **ol**\n2. ordered\n3. list"
        first_leaf_nodes = [
                LeafNode("big "),
                LeafNode("ol", "b")
        ]
        second_leaf_nodes = [
                LeafNode("ordered")
        ]
        third_leaf_nodes = [
                LeafNode("list")
        ]
        list_items = [
                HTMLNode("li", None, first_leaf_nodes),
                HTMLNode("li", None, second_leaf_nodes),
                HTMLNode("li", None, third_leaf_nodes)
        ]
        ordered_list_node = HTMLNode("ol", None, list_items)
        expected = HTMLNode("div", None, [ordered_list_node])
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_quote_one_line(self):
        markdown = ">quoted line"
        leaf_nodes = [
                LeafNode("quoted line")
        ]
        quote_nodes = [
                HTMLNode("q", None, leaf_nodes)
        ]
        expected = HTMLNode("div", None, quote_nodes)
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_quote_three_lines(self):
        markdown = ">big\n>*quote*\n>block"
        leaf_nodes = [
                LeafNode("big\n"),
                LeafNode("quote", "i"),
                LeafNode("\nblock")
        ]
        quote_nodes = [
                HTMLNode("q", None, leaf_nodes)
        ]
        expected = HTMLNode("div", None, quote_nodes)
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_paragraph_one_line(self):
        markdown = "this is a paragraph"
        leaves = [
                LeafNode("this is a paragraph")
        ]
        nodes = [
                HTMLNode("p", None, leaves)
        ]
        expected = HTMLNode("div", None, nodes)
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_paragraph_three_line(self):
        markdown = "this\nis a\nparagraph"
        leaves = [
                LeafNode("this\nis a\nparagraph")
        ]
        nodes = [
                HTMLNode("p", None, leaves)
        ]
        expected = HTMLNode("div", None, nodes)
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_paragraph_inline_bold_italic(self):
        markdown = "**this** paragraph has\n*so* much"
        leaves = [
                LeafNode("this", "b"),
                LeafNode(" paragraph has\n"),
                LeafNode("so", "i"),
                LeafNode(" much")
        ]
        nodes = [
                HTMLNode("p", None, leaves)
        ]
        expected = HTMLNode("div", None, nodes)
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)
