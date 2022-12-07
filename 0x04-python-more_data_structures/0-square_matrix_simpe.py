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

# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# square = square_matrix_simple(lst)
# print("{}".format([i for i in square]))