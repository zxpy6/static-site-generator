import unittest

from textnode import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_extract_images_no_images(self):
        text = "There are no images here"
        solution = []
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_images_1_link(self):
        text = "There are no images here, but there is a link to [google](google.com)"
        solution = []
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_images_1_image(self):
        text = "There is an image here ![pacman](pictures.com/pacman.png)"
        solution = [("pacman", "pictures.com/pacman.png")]
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_images_1_image_1_link(self):
        text = "There is an image here ![pacman](pictures.com/pacman.png) and also a link to [google](google.com)"
        solution = [("pacman", "pictures.com/pacman.png")]
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_images_2_images_1_link(self):
        text = "![evil](evil.png)[oh god](help.me)![diabolical](why.jpeg)"
        solution = [("evil", "evil.png"), ("diabolical", "why.jpeg")]
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_images_2_images(self):
        text = "![evil](evil.png)![diabolical](why.jpeg)"
        solution = [("evil", "evil.png"), ("diabolical", "why.jpeg")]
        matches = extract_markdown_images(text)
        self.assertEqual(matches, solution)

    def test_extract_links_no_links(self):
        text = "There are no links here"
        solution = []
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)

    def test_extract_links_1_image(self):
        text = "There are no images here, but there is an image of ![google](google.com)"
        solution = []
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)

    def test_extract_links_1_link(self):
        text = "There is a link to [pacman](pictures.com/pacman.png)"
        solution = [("pacman", "pictures.com/pacman.png")]
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)

    def test_extract_links_1_image_1_link(self):
        text = "There is an image here [pacman](pictures.com/pacman.png) and also a link to ![google](google.com)"
        solution = [("pacman", "pictures.com/pacman.png")]
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)

    def test_extract_links_2_links_1_image(self):
        text = "[evil](evil.png)![oh god](help.me)[diabolical](why.jpeg)"
        solution = [("evil", "evil.png"), ("diabolical", "why.jpeg")]
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)

    def test_extract_links_2_links(self):
        text = "[evil](evil.png)[diabolical](why.jpeg)"
        solution = [("evil", "evil.png"), ("diabolical", "why.jpeg")]
        matches = extract_markdown_links(text)
        self.assertEqual(matches, solution)


if __name__ == "__main__":
    unittest.main()