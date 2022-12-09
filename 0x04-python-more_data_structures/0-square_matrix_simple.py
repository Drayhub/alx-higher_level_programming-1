#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    ridx = 0
    for row in new_matrix:
        cidx = 0
        for num in row:
            matrix[ridx][cidx] = num ** 2
            cidx += 1
        ridx += 1
    return new_matrix
