#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for i in my_list:
            if i > max_int:
                max_int = i
        return max_int
list = [1, 90, 2, 13, 34, -13, 5, 3]
print(max_integer(list))