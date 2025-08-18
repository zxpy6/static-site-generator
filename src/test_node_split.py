import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_empty_list(self):
        nodes = []
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [])

    def test_single_split(self):
        nodes = [
            TextNode("This is a **bold** node", TextType.TEXT),
            TextNode("**No splits should occur", TextType.BOLD),
            TextNode("This is an _italic_ node", TextType.TEXT),
            TextNode("_No splits should occcur_", TextType.ITALIC),
            TextNode("This is a `code` node", TextType.TEXT),
            TextNode("`No splits should occur`", TextType.CODE),
        ]
        test1 = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT),
            TextNode("**No splits should occur", TextType.BOLD),
            TextNode("This is an _italic_ node", TextType.TEXT),
            TextNode("_No splits should occcur_", TextType.ITALIC),
            TextNode("This is a `code` node", TextType.TEXT),
            TextNode("`No splits should occur`", TextType.CODE),
        ]
        test2 = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT),
            TextNode("**No splits should occur", TextType.BOLD),
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" node", TextType.TEXT),
            TextNode("_No splits should occcur_", TextType.ITALIC),
            TextNode("This is a `code` node", TextType.TEXT),
            TextNode("`No splits should occur`", TextType.CODE),
        ]
        test3 = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node", TextType.TEXT),
            TextNode("**No splits should occur", TextType.BOLD),
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" node", TextType.TEXT),
            TextNode("_No splits should occcur_", TextType.ITALIC),
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" node", TextType.TEXT),
            TextNode("`No splits should occur`", TextType.CODE),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, test1)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, test2)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, test3)

    def test_multi_split(self):
        nodes = [
            TextNode("scary image", TextType.IMAGE, "place.com/evil.png"),
            TextNode("This has a **bold text block**", TextType.TEXT),
            TextNode("This **ALSO** has a bold text block", TextType.TEXT),
            TextNode("**FINAL** bold block", TextType.TEXT),
            TextNode("google", TextType.LINK, "google.com"),
        ]
        test1 = [
            TextNode("scary image", TextType.IMAGE, "place.com/evil.png"),
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold text block", TextType.BOLD),
            TextNode("This ", TextType.TEXT),
            TextNode("ALSO", TextType.BOLD),
            TextNode(" has a bold text block", TextType.TEXT),
            TextNode("FINAL", TextType.BOLD),
            TextNode(" bold block", TextType.TEXT),
            TextNode("google", TextType.LINK, "google.com"),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, test1)

    def test_no_split(self):
        nodes = [
            TextNode("scary image", TextType.IMAGE, "place.com/evil.png"),
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold text block", TextType.BOLD),
            TextNode("This ", TextType.TEXT),
            TextNode("ALSO", TextType.BOLD),
            TextNode(" has a bold text block", TextType.TEXT),
            TextNode("FINAL", TextType.BOLD),
            TextNode(" bold block", TextType.TEXT),
            TextNode("google", TextType.LINK, "google.com"),
        ]
        test1 = [
            TextNode("scary image", TextType.IMAGE, "place.com/evil.png"),
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold text block", TextType.BOLD),
            TextNode("This ", TextType.TEXT),
            TextNode("ALSO", TextType.BOLD),
            TextNode(" has a bold text block", TextType.TEXT),
            TextNode("FINAL", TextType.BOLD),
            TextNode(" bold block", TextType.TEXT),
            TextNode("google", TextType.LINK, "google.com"),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(nodes, test1)

if __name__ == "__main__":
    unittest.main()