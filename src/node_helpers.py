from textnode import TextNode, TextType
from htmlnode import HTMLNode
from node_converter import text_node_to_html_node

'''
Function Index

==========
split_nodes_delimiter(old_nodes, delimiter, text_type)
----------
splits nodes based on the delimiter and texttype
==========

==========
find_all_chars(string, char)
----------
provide indexes of delimiters for split_nodes_delimiter. provides support for multicharacter delimiters
==========

==========
extract_markdown_images(text)
----------
extracts the data for use in markdown image tags ![text](link)
=========


==========
extract_markdown_links(text)
----------
extracts the data for use in markdown link tags [text](link)
==========

==========
split_nodes_image(old_nodes)
----------
uses the data from the extract_markdown_images function to create a TextNode image object
==========

==========
split_nodes_link(old_nodes)
----------
uses the data from the extract_markdown_links function to create a TextNode link object
==========

==========
text_to_textnodes(text)
----------
splits a full string into all the TextNode needed to represent it
==========

==========
markdown_to_blocks(markdown)
----------
separates provided markdown text into blocks that wer separated with a blank line
==========

==========
block_to_block_type(block)
----------
returns a string value that represents what type of markdown block the block is
==========

==========
is_correct_ordered_list(ordered_list)
----------
a helper function for block_to_block_type that performs the loop to determine if ordered lists are sequentially numbered
==========

==========
----------
==========
'''

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''splits nodes based on the delimiter and texttype'''
    text = ""
    ret_nodes = []
    for node in old_nodes:
        text = node.text
        strings =[]
        delimiter_indexes = find_all_chars(text, delimiter)

        #edge cases
        if len(delimiter_indexes) == 0:
            ret_nodes.append(node)
            continue
        if len(delimiter_indexes) % 2 != 0:
            raise Exception(f"unmatched delimiter at {delimiter_indexes[-1]}")
        if node.text_type != TextType.NORMAL:
            ret_nodes .append(node)
            continue

        strings.append(text[:delimiter_indexes[0]])
        for i in range(0, len(delimiter_indexes)-1, 1):
            strings.append(text[delimiter_indexes[i]+len(delimiter):delimiter_indexes[i+1]])
        strings.append(text[delimiter_indexes[-1]+len(delimiter):])
        for i in range(len(strings)):
            if i % 2 == 0 and strings[i] != "":
                ret_nodes.append(TextNode(strings[i], node.text_type))
            if i % 2 != 0 and strings[i] != "":
                ret_nodes.append(TextNode(strings[i], text_type))
    return ret_nodes

def find_all_chars(string, char):
    '''provide indexes of delimiters for split_nodes_delimiter. provides support for multicharacter delimiters'''
    char_indexes = set()
    pos = 0
    while True:
        if string.find(char, pos) == -1:
            break
        char_indexes.add(string.find(char, pos))
        if string.find(char, pos) == len(string)-1:
            break
        pos = string.find(char, pos) + len(char)
    return sorted(list(char_indexes))

def extract_markdown_images(text):
    # examples of markdown images: ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
    import re
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    #examples of markdown links: [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) 
    import re 
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    import re
    if old_nodes == []:
        return []
    new_nodes = []
    for node in old_nodes:
        text = node.text

        #edge cases
        if node.text in (None, ""):
            continue
        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
            continue

        matches = re.finditer(r"!\[(.*?)\]\((.*?)\)", text)
        last_position = 0
        for match in matches:
            if match.start() > last_position:
                new_nodes.append(TextNode(text[last_position:match.start()], TextType.NORMAL))
            new_nodes.append(TextNode(match[1], TextType.IMAGE, match[2]))
            last_position = match.end()
        if last_position < len(text):
            new_nodes.append(TextNode(text[last_position:], TextType.NORMAL))

    return new_nodes

def split_nodes_link(old_nodes):
    import re
    if old_nodes == []:
        return []
    new_nodes = []
    for node in old_nodes:
        text = node.text

        #edge cases
        if node.text in (None, ""):
            continue
        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
            continue
        
        matches = re.finditer(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
        last_position = 0
        for match in matches:
            if match.start() > last_position:
                new_nodes.append(TextNode(text[last_position:match.start()], TextType.NORMAL))
            new_nodes.append(TextNode(match[1], TextType.LINK, match[2]))
            last_position = match.end()
        if last_position < len(text):
            new_nodes.append(TextNode(text[last_position:], TextType.NORMAL))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    delimiter_types = {
        split_nodes_link: TextType.LINK,
        split_nodes_image: TextType.IMAGE,
        "**": TextType.BOLD,
        "*": TextType.ITALIC,
        "`": TextType.CODE
    }
    
    for delimiter_type in delimiter_types:
        new_nodes = []
        if callable(delimiter_type):
            new_nodes = delimiter_type(nodes)
        else:
            new_nodes = split_nodes_delimiter(nodes, delimiter_type, delimiter_types[delimiter_type])
        nodes = new_nodes
    
    return nodes

def markdown_to_blocks(markdown):
    return list(filter(lambda x: x != "", map(str.strip, markdown.split("\n\n"))))

def block_to_block_type(block):
    import re

    heading = re.compile("^#{1,6}\s+.*")
    code = re.compile("^```[\s\S]*```$")
    quote = re.compile("^(>(.*)?\n?)+$")
    unordered_list = re.compile("^([*-] .*?\n?)+$")
    ordered_list = re.compile("^(\d+\. .*?\n?)+$")

    if heading.match(block):
        return "heading"
    elif code.match(block):
        return "code"
    elif quote.match(block):
        return "quote"
    elif unordered_list.match(block):
        return "unordered list"
    elif ordered_list.match(block) and is_correct_ordered_list(block):
        return "ordered list"
    else:
        return "paragraph"

def is_correct_ordered_list(ordered_list):
    lines = ordered_list.split("\n")
    for i in range(1, len(lines)+1):
        if lines[i-1].split(".")[0] != str(i):
            return False
    return True

def markdown_to_html_node(markdown):
    parent = HTMLNode("div", None, [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:

        if block_to_block_type(block) == "heading":
            block_parts = block.split()
            tag = block_parts[0]
            val = " ".join(block_parts[1:])
            children = text_to_children(val)
            node = HTMLNode(f"h{len(tag)}", None, children)
            parent.children.append(node)

        elif block_to_block_type(block) == "code":
            val = block.strip("```").strip("\n")
            children = text_to_children(val)
            node = HTMLNode("code", None, children)
            parent.children.append(node)

        elif block_to_block_type(block) == "unordered list":
            list_items = []
            for line in block.split("\n"):
                val = line[2:]
                list_items.append(HTMLNode("li", None, text_to_children(val)))
            node = HTMLNode("ul", None, list_items)
            parent.children.append(node)
            
        elif block_to_block_type(block) == "ordered list":
            list_items = []
            for line in block.split("\n"):
                num = line.split()[0]
                val = line[len(num)+1:]
                list_items.append(HTMLNode("li", None, text_to_children(val)))
            node = HTMLNode("ol", None, list_items)
            parent.children.append(node)

        elif block_to_block_type(block) == "quote":
            val = "\n".join(map(lambda x: x.lstrip("> "), block.split("\n")))
            children = text_to_children(val)
            node = HTMLNode("blockquote", None, children)
            parent.children.append(node)

        else:
            children = text_to_children(block)
            node = HTMLNode("p", None, children)
            parent.children.append(node)

    return parent

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    ret_nodes = []
    for node in textnodes:
        ret_nodes.append(text_node_to_html_node(node))
    return ret_nodes
