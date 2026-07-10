#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print("[", end="")
    for idx, row in enumerate(matrix):
        if idx > 0:
            print(", ", end="")
        print("[", end="")
        print(", ".join("{:d}".format(i**2) for i in row), end="")
        print("]", end="")
    print("]")
