from enum import Enum, auto


class TagType(Enum):
    P = auto()
    A = auto()
    H1 = auto()


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        #defaults to None
        # node without tag will render as raw text.
        # node without value will be assumed to have children.
        # node without children will be assumed to have value.
        # node without props simply wont have any attributes.
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return_string = ""
        if not self.props:
            return return_string
        for key, value in sorted(self.props.items()):
            return_string += f' {key}="{value}"'
        return return_string
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        