#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0
    for idx in range(len(my_list)):
        temp = my_list[idx]
        occ = 0
        for idxx in range(len(my_list)):
            if idx == idxx: 
                continue
            else:
                if my_list[idxx] == temp:
                    occ += 1
        if occ > 0:
            continue
        else:
            total_sum += my_list[idx]
    return total_sum
