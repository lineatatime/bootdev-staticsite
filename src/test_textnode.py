import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_missing_url(self):
        node = TextNode("This is a link", TextType.LINK, "example.com")
        node2 = TextNode("This is a link", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("This is a link", TextType.LINK, "example.com")
        node2 = TextNode("This is a link", TextType.IMG_EMBED, "example.com")
        self.assertNotEqual(node, node2)

    def test_diff_anchor(self):
        node = TextNode("This is a link", TextType.LINK, "example.com")
        node2 = TextNode("This is also a link", TextType.LINK, "example.com")
        self.assertNotEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("This is text", TextType.PLAIN_TEXT)
        node2 = TextNode("This is text", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()