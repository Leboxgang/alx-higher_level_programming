#!/usr/bin/python3
# Function to print a matrix of integers
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for item in row:
                endspace = ' ' if item != row[-1] else ''
                print("{:d}".format(item), end=endspace)
            print()
