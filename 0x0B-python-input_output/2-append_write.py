#!/usr/bin/python3

"""
Function that appends a string to a text file and returns the number of characters added.
"""

def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
