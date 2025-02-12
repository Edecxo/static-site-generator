import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", ["test"])
        node2 = ParentNode("p", ["test"])
        self.assertEqual(node, node2)

    def test_regular_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected, node.to_html())

    def test_nested_parent_nodes(self):
        nested_node = ParentNode(
            "div",
            [
                LeafNode("Code text", "code"),
                LeafNode("Normal text", None),
            ],
        )
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                nested_node,
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<div><code>Code text</code>Normal text</div><i>italic text</i>Normal text</p>"
        self.assertEqual(expected, node.to_html())

    def test_different_errors_for_nonoptional_attributes(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p")
        with self.assertRaises(ValueError) as context2:
            ParentNode(None, ["child"])
        self.assertNotEqual(context.exception, context2.exception)

    def test_no_tag_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, ['child'])
        expected = "'tag' must be provided"
        self.assertEqual(expected, str(context.exception))

    def test_no_children_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p")
        expected = "'children' must be provided"
        self.assertEqual(expected, str(context.exception))
