#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    print("[", end="")
    for row in matrix:
        print("[", end="")
        print(", ".join("{:d}".format(i) for i in row, end=""))
        print("]", end="")
    print("]", end="")
