import unittest

from textnode import TextNode, TextType
from node_helpers import split_nodes_image, split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_basic_image_node(self):
        node = TextNode("this ![cat](http://catpics.com/cat.png) is so cool", TextType.NORMAL)
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("cat", TextType.IMAGE, "http://catpics.com/cat.png"),
                TextNode(" is so cool", TextType.NORMAL)
        ]
        actual = split_nodes_image([node])
        self.assertEqual(expected, actual)
        
    def test_node_with_multiple_images(self):
        node = TextNode("this ![cat](http://catpics.com/cat.png) is so cool. And so is ![dog](http://doggos.dog/collie.png) cutie!", TextType.NORMAL)
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("cat", TextType.IMAGE, "http://catpics.com/cat.png"),
                TextNode(" is so cool. And so is ", TextType.NORMAL),
                TextNode("dog", TextType.IMAGE, "http://doggos.dog/collie.png"),
                TextNode(" cutie!", TextType.NORMAL)
        ]
        actual = split_nodes_image([node])
        self.assertEqual(expected, actual)

    def test_multiple_nodes_with_one_image(self):
        node1 = TextNode("this ![cat](http://catpics.com/cat.png) is so cool", TextType.NORMAL)
        node2 = TextNode("And so is this ![dog](http://doggos.dog/collie.png) cutie!", TextType.NORMAL)
        nodes = [node1, node2]
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("cat", TextType.IMAGE, "http://catpics.com/cat.png"),
                TextNode(" is so cool", TextType.NORMAL),
                TextNode("And so is this ", TextType.NORMAL),
                TextNode("dog", TextType.IMAGE, "http://doggos.dog/collie.png"),
                TextNode(" cutie!", TextType.NORMAL)
        ]
        actual = split_nodes_image(nodes)
        self.assertEqual(expected, actual)

    def test_left_edge_image(self):
        node = TextNode("![this cat](http://catpics.com/cat.png)! It's so cool!", TextType.NORMAL)
        expected = [
                TextNode("this cat", TextType.IMAGE, "http://catpics.com/cat.png"),
                TextNode("! It's so cool!", TextType.NORMAL)
        ]
        actual = split_nodes_image([node])
        self.assertEqual(expected, actual)

    def test_right_edge_image(self):
        node = TextNode("Look at this cool ![cat](http://catpics.com/cat.png)", TextType.NORMAL)
        expected = [
                TextNode("Look at this cool ", TextType.NORMAL),
                TextNode("cat", TextType.IMAGE, "http://catpics.com/cat.png")
        ]
        actual = split_nodes_image([node])
        self.assertEqual(expected, actual)

    def test_basic_link_node(self):
        node = TextNode("this [site](http://internet.com/) is so cool", TextType.NORMAL)
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("site", TextType.LINK, "http://internet.com/"),
                TextNode(" is so cool", TextType.NORMAL)
        ]
        actual = split_nodes_link([node])
        self.assertEqual(expected, actual)
        
    def test_node_with_multiple_links(self):
        node = TextNode("this [site](http://internet.com/) is so cool. And so is [other site](http://superinternet.new/) Yeah!", TextType.NORMAL)
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("site", TextType.LINK, "http://internet.com/"),
                TextNode(" is so cool. And so is ", TextType.NORMAL),
                TextNode("other site", TextType.LINK, "http://superinternet.new/"),
                TextNode(" Yeah!", TextType.NORMAL)
        ]
        actual = split_nodes_link([node])
        self.assertEqual(expected, actual)

    def test_multiple_nodes_with_one_link(self):
        node1 = TextNode("this [site](http://internet.com/) is so cool", TextType.NORMAL)
        node2 = TextNode("And so is this [other site](http://superinternet.new/) Yeah!", TextType.NORMAL)
        nodes = [node1, node2]
        expected = [
                TextNode("this ", TextType.NORMAL),
                TextNode("site", TextType.LINK, "http://internet.com/"),
                TextNode(" is so cool", TextType.NORMAL),
                TextNode("And so is this ", TextType.NORMAL),
                TextNode("other site", TextType.LINK, "http://superinternet.new/"),
                TextNode(" Yeah!", TextType.NORMAL)
        ]
        actual = split_nodes_link(nodes)
        self.assertEqual(expected, actual)

    def test_left_edge_link(self):
        node = TextNode("[this site](http://internet.com/)! It's so cool!", TextType.NORMAL)
        expected = [
                TextNode("this site", TextType.LINK, "http://internet.com/"),
                TextNode("! It's so cool!", TextType.NORMAL)
        ]
        actual = split_nodes_link([node])
        self.assertEqual(expected, actual)

    def test_right_edge_link(self):
        node = TextNode("Look at this cool [this site](http://internet.com/)", TextType.NORMAL)
        expected = [
                TextNode("Look at this cool ", TextType.NORMAL),
                TextNode("this site", TextType.LINK, "http://internet.com/")
        ]
        actual = split_nodes_link([node])
        self.assertEqual(expected, actual)
