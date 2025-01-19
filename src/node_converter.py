from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            tag = None
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
        case TextType.IMAGE:
            tag = "img"
        case _:
            raise Exception("current text_type not supported")

    props = None
    if text_node.text_type in (TextType.LINK, TextType.IMAGE) and text_node.url:
        props = {}
        if tag == "a":
            props["href"] = text_node.url
        elif tag == "img":
            props["src"] = text_node.url

    return LeafNode(text_node.text, tag, props)
