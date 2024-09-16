#!/usr/bin/python3
# Function to remove all occurrences of 'c' and 'C' from a string
def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string
