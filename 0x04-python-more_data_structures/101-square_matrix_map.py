#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # Return a new matrix with each element squared using map
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
