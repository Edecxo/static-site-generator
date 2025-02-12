import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("this is a value")
        node2 = LeafNode("this is a value")
        self.assertEqual(node, node2)

    def test_default_values(self):
        node = LeafNode("this is a value")
        expected = (None, None)
        actual = (node.tag, node.props)
        self.assertEqual(expected, actual)

    def test_ValueError_when_not_providing_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode()
        self.assertTrue("'value' must be provided" in str(context.exception))

    def test_to_html(self):
        node = LeafNode("this is a value", "p")
        expected = f"<p>this is a value</p>"
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_repr(self):
        node = LeafNode("this is a value")
        expected = f"tag: None\nvalue: this is a value\nprops: None"
        self.assertEqual(expected, node.__repr__())
