#!/usr/bin/python3
def multiply_by_2(my_dict):
    # Multiply all values in the dictionary by 2
    return {key: val * 2 for key, val in my_dict.items()}
