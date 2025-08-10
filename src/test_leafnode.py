import unittest

from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a_1_arg(self):
        node = LeafNode("a", "google", {"href": "https://www.google.com"})
        str1 = node.to_html()
        str2 = '<a href="https://www.google.com">google</a>'
        self.assertEqual(str1, str2)

    def test_leaf_invalid(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"}) # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "raw text")
        str1 = node.to_html()
        str2 = "raw text"
        self.assertEqual(str1, str2)

    def test_leaf_to_html_a_2_arg(self):
        node = LeafNode("a", "google", {"href": "https://www.google.com", "target": "_blank"})
        str1 = node.to_html()
        str2 = '<a href="https://www.google.com" target="_blank">google</a>'
        self.assertEqual(str1, str2)

if __name__ == "__main__":
    unittest.main()