import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_eq_2_arg(self):
        node1 = HTMLNode("a", "google", None, {"href": "google.com", "target": "_blank"})
        str1 = node1.props_to_html()
        str2 = f' href="google.com" target="_blank"'
        self.assertEqual(str1, str2)

    def test_props_to_html_eq_1_arg(self):
        node1 = HTMLNode("a", "google", None, {"href": "google.com"})
        str1 = node1.props_to_html()
        str2 = f' href="google.com"'
        self.assertEqual(str1, str2)

    def test_props_to_html_eq_0_arg(self):
        node1 = HTMLNode("p", "this is a paragraph")
        str1 = node1.props_to_html()
        str2 = f''
        self.assertEqual(str1, str2)

    def test_eq_str_p(self):
        node1 = HTMLNode("p", "this is a paragraph")
        str1 = str(node1)
        str2 = f"HTMLNode(p, this is a paragraph, None, None)"
        self.assertEqual(str1, str2)

    def test_eq_str_a(self):
        node1 = HTMLNode("a", "google", None, {"href": "google.com", "target": "_blank"})
        str1 = str(node1)
        str2 = "HTMLNode(a, google, None, {'href': 'google.com', 'target': '_blank'})"
        self.assertEqual(str1, str2)

if __name__ == "__main__":
    unittest.main()