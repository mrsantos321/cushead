#!/usr/bin/env python3
"""
Main script thats run the CLI feature.
"""
import sys

from src.console import console
from src.console import logs


def main() -> None:
    """
    Handle the CLI feature.
    """
    logs.show_presentation()
    console.parse_args(args=sys.argv[1:])


if __name__ == "__main__":
    main()
