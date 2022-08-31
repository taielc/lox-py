"""Token Object definition."""
from dataclasses import dataclass

from token_type import TokenType


@dataclass
class Token:  # pylint: disable=too-few-public-methods
    """Token Object definition."""

    type: TokenType
    lexeme: str
    literal: str
    line: int
    pos: int

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"
