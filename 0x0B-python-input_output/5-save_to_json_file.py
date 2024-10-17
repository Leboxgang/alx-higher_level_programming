#!/usr/bin/python3

"""
Module to save an object to a JSON file.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Save an object to a file in JSON format.
    
    Arguments:
        my_obj (obj): The input object to convert to JSON format.
        filename (str): The name of the output file.
    
    Returns:
        The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(json.dumps(my_obj))
