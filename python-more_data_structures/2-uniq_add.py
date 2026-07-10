#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0
    for i in my_list:
        if my_list.count(i) == 1:
            total_sum += i
    return total_sum
