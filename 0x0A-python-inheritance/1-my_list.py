#!/usr/bin/python3

class MyList(list):
    """
     MyList class that inherits from list class
    """
    def print_sorted(self):
        """
        Public method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
