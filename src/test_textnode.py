import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()