#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Multiply all elements in the list by a number using map
    return list(map(lambda n: n * number, my_list))
