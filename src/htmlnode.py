class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #html tag (e.g. "p", "a", "h1", etc.)
        self.value = value #str for value of a tag (e.g. the text in a paragraph
        self.children = children #list of HTMLNode object representing this node's children
        self.props = props #dict representing attribute of the html tag (e.x. <a> might have {"href": "https://google.com"}
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = "".join([f' {k}="{self.props[k]}"' for k in self.props])
        return html_string
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, value=None, tag=None, props=None):
        if value == None:
            raise ValueError("'value' must be provided")
        self.value = value
        self.tag = tag
        self.props = props

    def to_html(self):
        open_tag = ""
        close_tag = ""
        if self.tag != None:
            open_tag = f"<{self.tag}>"
            close_tag = f"</{self.tag}>"
        return f"{open_tag}{self.value}{close_tag}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nprops: {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag == None:
            raise ValueError("'tag' must be provided")
        if children in (None, []):
            raise ValueError("'children' must be provided")
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        inner = ""
        for child in self.children:
            inner += child.to_html()
        return f"<{self.tag}>{inner}</{self.tag}>"


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

