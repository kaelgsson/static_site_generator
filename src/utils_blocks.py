from enum import Enum
import re


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