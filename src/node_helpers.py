from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text = ""
    ret_nodes = []
    for node in old_nodes:
        text = node.text
        strings =[]
        delimiter_indexes = find_all_chars(text, delimiter)
        print(delimiter_indexes)

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
    new_nodes = []
    for node in old_nodes:
        text = node.text

        #edge cases
        if node.text in (None, ""):
            continue
        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
            continue
        
        strings = re.split(r"!\[(.*?)\]\((.*?)\)", text)
        for i in range(0, len(strings), 3):
            if strings[i] != "":
                new_nodes.append(TextNode(strings[i], TextType.NORMAL))
            if 0 <= i+2 < len(strings):
                new_nodes.append(TextNode(strings[i+1], TextType.LINK, strings[i+2]))
    return new_nodes

def split_nodes_link(old_nodes):
    import re
    new_nodes = []
    for node in old_nodes:
        text = node.text

        #edge cases
        if node.text in (None, ""):
            continue
        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
            continue
        
        strings = re.split(r"\[(.*?)\]\((.*?)\)", text)
        for i in range(0, len(strings), 3):
            if strings[i] != "":
                new_nodes.append(TextNode(strings[i], TextType.NORMAL))
            if 0 <= i+2 < len(strings):
                new_nodes.append(TextNode(strings[i+1], TextType.LINK, strings[i+2]))
    return new_nodes
