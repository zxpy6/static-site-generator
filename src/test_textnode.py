import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_text_type(self):
        node1 = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.LINK, "google.com")
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_missing(self):
        node1 = TextNode("This is a google link", TextType.LINK, "google.com")
        node2 = TextNode("This is a google link", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_not_eq_text(self):
        node1 = TextNode("Different text", TextType.ITALIC)
        node2 = TextNode(" text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_link_image(self):
        node1 = TextNode("google", TextType.LINK, "google.com")
        node2 = TextNode("google", TextType.IMAGE, "google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_str_link(self):
        node1 = str(TextNode("google", TextType.LINK, "google.com"))
        node2 = f"TextNode(google, link, google.com)"
        self.assertEqual(node1, node2)
    
    def test_eq_str_no_link(self):
        node1 = str(TextNode("google", TextType.CODE))
        node2 = f"TextNode(google, code, None)"
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()