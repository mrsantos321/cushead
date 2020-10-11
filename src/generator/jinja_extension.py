"""
Module used to group jinja extensions.
"""
from __future__ import annotations

from typing import Any

from jinja2 import ext
from jinja2 import nodes
from jinja2 import parser as jinja2_parser
from jinja2 import runtime


class OneLineExtension(ext.Extension):
    """
    Removes whitespace between HTML tags at compile time, including tab and newline characters.

    It does not remove whitespace between Jinja2 tags or variables. Neither does it remove whitespace between tags.
    """

    # A tuple of names that trigger the extension.
    tags = {"oneline"}

    def parse(self, parser: jinja2_parser.Parser) -> Any:
        """
        This method is called when any of tags is recognized.

        The method apply transformation to the blocks inside the start and the end of the block.
        This transformation is the text without new lines and spaces between.
        The return is a node class initialized with this transformated text.
        The nodes are the elements that are used by the Abstract Syntax Tree of Jinja2 to represent the template.

        Args:
            parser: parser processor gived from jinja.

        Returns:
            The call block.
        """
        # We need actual line number to append the final result to this line number.
        # The first token is the token that started the tag, so, don't need it.
        next(parser.stream)
        lineno = parser.stream.current.lineno

        # Get the content inside the extension tag, with the second parameter as True,
        # we dont get, as final token, the end block of the extension tag, because we don't need it.
        body = parser.parse_statements(tuple(f"name:end{tagname}" for tagname in self.tags), True)

        method = self.call_method("strip_spaces")
        call_block = nodes.CallBlock(method, [], [], body)
        call_block.set_lineno(lineno)
        return call_block

    @staticmethod
    def strip_spaces(caller: runtime.Macro) -> str:
        """
        Clean all the spaces and new lines of a content.

        Args:
            caller: an anonymous Macro class, generated by CallBlock node.
                This class is callable and return a parsed version (variable replacement) of the content
                gived to the CallBlock.

        Returns:
            return the cleaned content of the macro.
        """
        return "".join(caller().split())
