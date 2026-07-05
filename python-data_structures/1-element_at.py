#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx < 0:
            print("None")
        elif idx > 0: 
            print("None")
        else:
            print("{:d}".format(my_list[idx]))
