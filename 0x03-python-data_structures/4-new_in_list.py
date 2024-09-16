#!/usr/bin/python3
# Function to create a new list with an element replaced at a specified index
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list
