""" Misc processing functions """
import re


def is_digit(char: str) -> bool:
    """
    Check if character is a digit.
    """
    return bool(re.match(r"\d", char))
