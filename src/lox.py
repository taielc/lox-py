"""
Lox Interpreter base.
"""
from typing import List

from scanner import ParsingError, Scanner
from token_ import Token


def run(source: str, file_path=None):
    """
    Run Lox source code given.
    """
    scanner = Scanner(source, file_path)
    tokens: List[Token] = scanner.scan_tokens()
    print(tokens)


def run_file(path: str):
    """Run Lox from a given file path."""
    with open(path, mode="r", encoding="utf8") as file:
        run(file.read(), path)


def run_prompt():
    """Run Lox as a prompt line by line."""
    while True:
        try:
            run(input("> "))
        except KeyboardInterrupt:
            print("")
        except ParsingError as error:
            print(error)
        except EOFError:
            print("")
            return


def main(args: List[str]):
    """Main function"""
    if len(args) == 2:
        run_file(args[1])
    else:
        run_prompt()


if __name__ == "__main__":
    from sys import argv

    main(argv)
