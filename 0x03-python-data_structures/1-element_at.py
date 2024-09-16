#!/usr/bin/python3
# Function to get the element at a specific index in a list
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
