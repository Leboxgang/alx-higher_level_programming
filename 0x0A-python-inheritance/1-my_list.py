#!/usr/bin/python3
"""Module that contains a class MyList that inherits from list."""

class MyList(list):
    """A custom class that inherits from the built-in list class."""
    
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
