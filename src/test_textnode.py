import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("node", TextType.TEXT)
        node2 = TextNode("node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_link_not_eq(self):
        node1 = TextNode("same text", TextType.LINK, "https://example1.org")
        node2 = TextNode("same text", TextType.LINK, "http://notexample2.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("same text", TextType.TEXT)
        self.assertEqual(node1.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="https://example.org">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://example.org/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.to_html(), '<img src="https://example.org/image.png" alt="This is an image node"></img>')

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")


if __name__ == "__main__":
    unittest.main()