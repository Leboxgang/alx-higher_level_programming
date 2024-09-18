#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Return a new matrix with each element squared
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
        return squared
