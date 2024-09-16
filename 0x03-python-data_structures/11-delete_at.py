#!/usr/bin/python3
# Function to delete an element at a specific index in a list
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
