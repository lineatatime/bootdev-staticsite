import unittest

from htmlnode import HTMLNode

props_test = {
    "href": "https://example.com",
    "target": "_blank"
}

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "Anchor Text", props=props_test)
        node2 = HTMLNode("<a>", "More Anchor Text", props=props_test)
        node_prop_string = node.props_to_html()
        node2_prop_string = node2.props_to_html()
        self.assertEqual(node_prop_string, node2_prop_string)

if __name__ == "__main__":
    unittest.main()