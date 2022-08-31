"""
Lox Interpreter base.
"""
from typing import List


def run(source: str):
    """
    Run Lox source code given.
    """
    print(source)


def run_file(path: str):
    """Run Lox from a given file path."""
    with open(path, mode="r", encoding="utf8") as file:
        run(file.read())


def run_prompt():
    """Run Lox as a prompt line by line."""
    try:
        while True:
            run(input("> "))
    except (EOFError, KeyboardInterrupt):
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
