"""Token Types definition."""

from enum import Enum

# Other tokens.
OTHER_TOKENS = {
    "COMMENT": "//",
    "EOF": "EOF",
}


class _TokenTypeMixIn(Enum):
    """Enum mix-in for token types."""

    def __repr__(self):
        return f"{repr(self.value)}"

    def __str__(self):
        return str(self.value)


TokenType = Enum(  # type: ignore[misc]
    "TokenType",
    {
        # Single-character tokens.
        "LEFT_PAREN": "(",
        "RIGHT_PAREN": ")",
        "LEFT_BRACE": "{",
        "RIGHT_BRACE": "}",
        "COMMA": ",",
        "DOT": ".",
        "MINUS": "-",
        "PLUS": "+",
        "SEMICOLON": ";",
        "SLASH": "/",
        "STAR": "*",
        #
        # One or two character tokens.
        "BANG": "!",
        "BANG_EQUAL": "!=",
        "EQUAL": "=",
        "EQUAL_EQUAL": "==",
        "GREATER": ">",
        "GREATER_EQUAL": ">=",
        "LESS": "<",
        "LESS_EQUAL": "<=",
        **{
            kw: kw.lower()
            for kw in [
                #
                # Keywords.
                "AND",
                "CLASS",
                "ELSE",
                "FALSE",
                "FUN",
                "FOR",
                "IF",
                "NIL",
                "OR",
                "PRINT",
                "RETURN",
                "SUPER",
                "THIS",
                "TRUE",
                "VAR",
                "WHILE",
                #
                # Literals.
                "IDENTIFIER",
                "STRING",
                "NUMBER",
            ]
        },
        # whitespace tokens.
        "SPACE": " ",
        "TAB": "\t",
        "NEWLINE": "\n",
        "CARRIAGE_RETURN": "\r",
        # Other tokens.
        "COMMENT": "//",
        "EOF": "eof",
    },
    type=_TokenTypeMixIn,
)
