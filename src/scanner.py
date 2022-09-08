"""
Lox Scanner/Lexer.
"""
from typing import List

from token_ import Token
from token_type import KEYWORD_TOKENS, TokenType
from utils import is_alpha, is_alphanumeric, is_digit


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
            case TokenType.STAR.value:
                self.add_token(TokenType.STAR)
            # One or two character tokens
            case TokenType.BANG.value:
                self.add_token(
                    TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
                )
            case TokenType.EQUAL.value:
                self.add_token(
                    TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
                )
            case TokenType.LESS.value:
                self.add_token(
                    TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
                )
            case TokenType.GREATER.value:
                self.add_token(
                    TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
                )
            # Slash & Comments
            case TokenType.SLASH.value:
                if self.match("/"):
                    self.comment()
                else:
                    self.add_token(TokenType.SLASH)
            # Whitespace
            case TokenType.SPACE.value:
                self.add_token(TokenType.SPACE)
            case TokenType.TAB.value:
                self.add_token(TokenType.TAB)
            case TokenType.CARRIAGE_RETURN.value:
                self.add_token(TokenType.CARRIAGE_RETURN)
            case TokenType.NEWLINE.value:
                self.line += 1
                self.add_token(TokenType.NEWLINE)
            # Literals
            case '"':
                print("String start")
                self.string()
            case _ if is_digit(char):
                self.number()
            # Identifiers and keywords
            case _ if is_alpha(char):
                self.identifier_or_keyword()
            case _:
                raise Exception(f"Unexpected character: {char}")

    def identifier_or_keyword(self):
        """
        Scan an identifier or keyword.
        """
        while is_alphanumeric(self.peek()):
            self.advance()

        text = self.source[self.start : self.current]
        token_type = KEYWORD_TOKENS.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    def number(self):
        """
        Scan a number from source.
        """
        while is_digit(self.peek()):
            self.advance()
        # Look for a fractional part.
        if self.peek() == "." and is_digit(self.peek_next()):
            # Consume the "."
            self.advance()
            while is_digit(self.peek()):
                self.advance()
        self.add_token(TokenType.NUMBER, float(self.source[self.start : self.current]))

    def string(self):
        """
        Scan a string from source.
        """
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()
        if self.is_at_end():
            raise Exception("Unterminated string.")
        # The closing "
        self.advance()
        # Skip the initial and ending "
        string = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, value=string)

    def comment(self):
        """
        Save the comment.
        """
        end_char = "\n"
        while self.peek() != end_char and not self.is_at_end():
            self.advance()
        # Skip the '//'
        comment = self.source[self.start + 2 : self.current]
        self.add_token(TokenType.COMMENT, value=comment)

    def peek_next(self) -> str:
        """
        Peek at next character in source.
        """
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def peek(self) -> str:
        """
        Peek at next character in source.
        """
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_prev(self) -> str:
        """
        Peek at previous character in source.
        """
        return self.source[self.current - 1]

    def match(self, expected: str) -> bool:
        """
        Check if next character in source matches expected.
        """
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

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
