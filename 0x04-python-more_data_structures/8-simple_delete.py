#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    # Delete a key from the dictionary if it exists
    my_dict.pop(key, None)
    return my_dict
