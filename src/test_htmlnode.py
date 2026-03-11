import unittest

from htmlnode import HTMLNode, LeafNode

props_test = {
    "href": "https://example.com",
    "target": "_blank"
}

# {"href": "https://example.com", "target": "_blank"}

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "Anchor Text", props=props_test)
        node2 = HTMLNode("<a>", "More Anchor Text", props=props_test)
        node_prop_string = node.props_to_html()
        node2_prop_string = node2.props_to_html()
        self.assertEqual(node_prop_string, node2_prop_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", props_test)
        self.assertEqual(node.to_html(), "<a href='https://example.com' target='_blank'>Hello, world!</a>")
    
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

if __name__ == "__main__":
    unittest.main()