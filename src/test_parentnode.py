import unittest

from htmlnode import LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_missing_tag(self):
        child_node = LeafNode("i", "child node")
        parent_node = ParentNode(None, [child_node]) # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_missing_children(self):
        child_node = LeafNode("i", "child node")
        parent_node = ParentNode("p", None) # pyright: ignore[reportArgumentType]
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_props_and_grandchildren(self):
        grandchild_node1 = LeafNode("b", "Click me!", {"class": "term"})
        grandchild_node2 = LeafNode("i", "Please.")
        child_node = ParentNode("a", [grandchild_node1, grandchild_node2], {"href": "https://www.google.com"})
        parent_node = ParentNode("p", [child_node])
        str1 = parent_node.to_html()
        str2 = '<p><a href="https://www.google.com"><b class="term">Click me!</b><i>Please.</i></a></p>'
        self.assertEqual(str1, str2)

    def test_to_html_empty_children(self):
        parent_node = ParentNode("p", [])
        str1 = parent_node.to_html()
        str2 = '<p></p>'
        self.assertEqual(str1, str2)

if __name__ == "__main__":
    unittest.main()