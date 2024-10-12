#!/usr/bin/python3
"""Defines a function to indent text."""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If the text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
