""" Misc processing functions """
import re


def is_digit(char: str) -> bool:
    """
    Check if character is a digit.
    """
    return bool(re.match(r"\d", char))


def is_alpha(char: str) -> bool:
    """
    Check if character is a letter.
    """
    return bool(re.match(r"[a-zA-Z_]", char))


def is_alphanumeric(char: str) -> bool:
    """
    Check if character is a letter or digit.
    """
    return bool(re.match(r"[a-zA-Z0-9_]", char))
