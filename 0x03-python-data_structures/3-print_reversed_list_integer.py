#!/usr/bin/python3
# Function to print the elements of a list in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for elm in my_list[::-1]:
            print("{:d}".format(elm))
