#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list) - 1):
            j = i + 1
            max = my_list[i] if my_list[i] > my_list[j] else my_list[j]
        return max
