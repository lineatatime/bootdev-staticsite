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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_text(self):
        node = TextNode("This is a italic text node", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.INLINE_CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_text(self):
        node = TextNode("This is a link", TextType.LINK, "https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": node.url})

    def test_img_text(self):
        node = TextNode("This is an image embed", TextType.IMG_EMBED, "https://imgurl.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": node.url, "alt": node.text})



if __name__ == "__main__":
    unittest.main()