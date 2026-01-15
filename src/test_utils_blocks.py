import unittest

from utils_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)


class TestUtilsBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        self.assertEqual(
            block_to_block_type("### Heading"),
            BlockType.HEADING,
        )

    def test_block_to_block_type_unordered(self):
        self.assertEqual(
            block_to_block_type("- item one\n- item two\n"),
            BlockType.UNORDERED_LIST,
        )

    def test_block_to_block_type_ordered(self):
        self.assertEqual(
            block_to_block_type("1. first\n2. second"),
            BlockType.ORDERED_LIST,
        )

    def test_block_to_block_type_code(self):
        self.assertEqual(
            block_to_block_type("```\nprint('hello')\n```"),
            BlockType.CODE,
        )

    def test_block_to_block_type_quote(self):
        self.assertEqual(
            block_to_block_type("> quoted text"),
            BlockType.QUOTE,
        )

if __name__ == "__main__":
    unittest.main()
