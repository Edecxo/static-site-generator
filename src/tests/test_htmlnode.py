import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", ["children"], {"props": 1})
        node2 = HTMLNode("tag", "value", ["children"], {"props": 1})
        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = HTMLNode("this is a tag",
                        "this is a value",
                        "these are children".split(),
                        {"these": "are", "some": "props"})
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("this is a tag",
                        "this is a value",
                        "these are children".split(),
                        {"these": "are", "some": "props"})
        expected = "tag: this is a tag\nvalue: this is a value\nchildren: ['these', 'are', 'children']\nprops: {'these': 'are', 'some': 'props'}"
        self.assertEqual(expected, node.__repr__())

    def test_props_to_html(self):
        node = HTMLNode(props={"href":"http://localhost", "target": "_blank"})
        expected = ' href="http://localhost" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
