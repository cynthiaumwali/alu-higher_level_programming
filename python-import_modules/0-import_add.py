#!/usr/bin/python3
add = __import__('0-add').add
a = 1
b = 2
result = add(a, b)
print(f"{:d} + {:d} = {:d}".format(a, b, result))
