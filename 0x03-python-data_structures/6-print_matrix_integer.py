#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for elem in matrix:
            for num in range(len(elem)):
                if num is not elem[len(elem) - 1]:
                    print("{:d}".format(num), end=" ")
                else:
                    print("{:d}".format(num), end="")
