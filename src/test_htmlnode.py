import unittest

from htmlnode import HTMLNode, TagType

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(TagType.P, "a value")
        node2 = HTMLNode(TagType.P, "a value")
        self.assertEqual(node1, node2)

    def test_props_to_html_empty(self):
        node = HTMLNode(TagType.P, "a value", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode(TagType.P, "a value", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_no_child(self):
        node = HTMLNode(TagType.P, "a value")
        self.assertEqual(node.children, None)