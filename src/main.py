from textnode import TextNode, TextType

def main():
    textnode = TextNode("this is text", TextType.BOLD, "http://localhost:8888")
    print(textnode)

main()
