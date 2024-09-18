#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    # Print the dictionary with keys sorted
    for k in sorted(my_dict.keys()):
        print("{}: {}".format(k, my_dict[k]))
