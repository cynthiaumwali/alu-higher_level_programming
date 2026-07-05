#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx < 0:
            print("None")
        elif idx > len(my_list): 
            print("None")
        else:
            print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
