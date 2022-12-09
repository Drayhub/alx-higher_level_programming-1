#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
def multiply_by_2(a_dictionary):
    dict = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        dict.update({key: new_value})
    return dict
