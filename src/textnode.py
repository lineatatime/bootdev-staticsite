from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    INLINE_CODE = "code"
    LINK = "link"
    IMG_EMBED = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type.value == "plain":
            return LeafNode(None, self.text)
        if self.text_type.value == "bold":
            return LeafNode("b", self.text)
        if self.text_type.value == "italic":
            return LeafNode("i", self.text)
        if self.text_type.value == "code":
            return LeafNode("code", self.text)
        if self.text_type.value == "link":
            return LeafNode("a", self.text, props={"href": self.url})
        if self.text_type.value == "image":
            return LeafNode("img", None, props={"src": self.url, "alt": self.text})
        raise Exception("Undefined Text Type")

