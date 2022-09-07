"""
Lox Scanner/Lexer.
"""
from typing import List

from token_ import Token
from token_type import TokenType


class Scanner:
    """
    Scanner for Lox.
    """

    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        """
        Scan tokens from source.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        return self.tokens

    def scan_token(self):
        """
        Scan a token from source.
        """
        char: str = self.advance()
        # type: ignore
        match char:
            # Single-character tokens
            case TokenType.LEFT_PAREN.value:
                self.add_token(TokenType.LEFT_PAREN)
            case TokenType.RIGHT_PAREN.value:
                self.add_token(TokenType.RIGHT_PAREN)
            case TokenType.LEFT_BRACE.value:
                self.add_token(TokenType.LEFT_BRACE)
            case TokenType.RIGHT_BRACE.value:
                self.add_token(TokenType.RIGHT_BRACE)
            case TokenType.COMMA.value:
                self.add_token(TokenType.COMMA)
            case TokenType.DOT.value:
                self.add_token(TokenType.DOT)
            case TokenType.MINUS.value:
                self.add_token(TokenType.MINUS)
            case TokenType.PLUS.value:
                self.add_token(TokenType.PLUS)
            case TokenType.SEMICOLON.value:
                self.add_token(TokenType.SEMICOLON)
            case TokenType.SLASH.value:
                self.add_token(TokenType.SLASH)
            case TokenType.STAR.value:
                self.add_token(TokenType.STAR)
            case _:
                raise Exception(f"Unexpected character: {char}")

    def add_token(self, token_type: TokenType, value: str = None):
        """
        Add token to tokens.
        """
        if value is None:
            value = token_type.value
        lexeme = self.source[self.start : self.current]
        token = Token(token_type, lexeme, value, self.line, self.start)
        self.tokens.append(token)

    def post_increment_current(self) -> int:
        """
        Post-increment current position in source.
        """
        self.current += 1
        return self.current - 1

    def advance(self) -> str:
        """
        Advance current position in source.
        """
        return self.source[self.post_increment_current()]

    def is_at_end(self):
        """
        Check if at end of source.
        """
        return self.current >= len(self.source)
