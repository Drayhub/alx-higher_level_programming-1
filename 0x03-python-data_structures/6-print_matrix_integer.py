#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for elem in matrix:
            for num in range(len(elem)):
                print("{:d}".format(elem[num]), end=" ")
            print()
