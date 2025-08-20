import re

from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode | Exception:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url}) # pyright: ignore[reportArgumentType]
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})  # pyright: ignore[reportArgumentType]
        case _:
            raise Exception("Unrecognized node type")
        
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    match text_type:
        case TextType.TEXT:
            return old_nodes
        case TextType.BOLD:
            if delimiter != "**": return old_nodes
        case TextType.ITALIC:
            if delimiter != "_": return old_nodes
        case TextType.CODE:
            if delimiter != "`": return old_nodes
    
    new_nodes = []
    for n in old_nodes:
        if n.text.count(delimiter) < 2 or n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        s1, s2, s3 = n.text.split(delimiter, 2)
        if s1 != "":
            new_nodes.append(TextNode(s1, TextType.TEXT))
        if s2 != "":
            new_nodes.append(TextNode(s2, text_type))
        if s3 != "":
            new_nodes.append(TextNode(s3, TextType.TEXT))
    
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)



# images:!\[(.*?)\]\((.*?)\)            old: links:(?<!!)(\[(.*?)\])\((.*?)\) regex
# links: (?<!!)\[(.*?)\]\((.*?)\)