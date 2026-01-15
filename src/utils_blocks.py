from enum import Enum
import re
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from utils_inline import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split('\n\n')
    list_of_blocks = [x.strip() for x in list_of_blocks if x != '']


    return list_of_blocks

def block_to_block_type(block):
    '''
    takes a single block of md-text and return blocktype.
    '''
    lines = [x for x in block.split('\n') if x.strip()]

    if re.match(r'^(#{1,6})\s', block):
        return BlockType.HEADING
    elif re.match(r'^`{3,}.*\r?\n', block):
        return BlockType.CODE
    elif re.match(r'^>\s?', block):
        return BlockType.QUOTE
    elif lines and all(re.match(r'^-\s', x) for x in lines):
        return BlockType.UNORDERED_LIST
    elif lines and all(x.startswith(f"{i+1}. ") for i, x in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    '''
    works for all block types. It takes a string of text.
    returns a list of HTMLNodes that represent the inline markdown.
    using previously created functions.
    Note: codeblock should not use this func, manually make a TextNode
          and use text_node_to_html_node instead.
    '''
    nodes = text_to_textnodes(text)
    output = []
    for node in nodes:
        output.append(text_node_to_html_node(node))
    return output

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def markdown_to_html_node(markdown):
    '''
    this will have to use a lot of helper functions (8)
    '''
    #split markdown to blocks
    blocks = markdown_to_blocks(markdown)
    children = []

    #loop over each block
    for block in blocks:
        #determine type of block
        block_type = block_to_block_type(block)

        #create HTMLNode with proper data
        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
        elif block_type == BlockType.HEADING:
            children.append(heading_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))
        elif block_type == BlockType.CODE:
            children.append(code_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(ulist_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(olist_to_html_node(block))
        else:
            raise ValueError("invalid BlockType")


    #make all the block nodes children under single parent HTML (just a div)
    parent = ParentNode("div", children, None)
    

    return parent
