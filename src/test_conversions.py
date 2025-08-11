import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None) # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "This is a text node") # pyright: ignore[reportAttributeAccessIssue]

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "This is a bold node") # pyright: ignore[reportAttributeAccessIssue]

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "This is an italic node") # pyright: ignore[reportAttributeAccessIssue]

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "This is a code node") # pyright: ignore[reportAttributeAccessIssue]

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "This is a link node") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.props, {"href": "google.com"}) # pyright: ignore[reportAttributeAccessIssue]

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.value, "") # pyright: ignore[reportAttributeAccessIssue]
        self.assertEqual(html_node.props, {"src": "google.com", "alt": "This is an image node"}) # pyright: ignore[reportAttributeAccessIssue]


if __name__ == "__main__":
    unittest.main()