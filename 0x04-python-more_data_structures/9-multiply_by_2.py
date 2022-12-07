#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = {}
    for key, value in a_dictionary.items():
        new_value = value * 2
        dict.update({key: new_value})
    return dict

dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}
new_dict = multiply_by_2(dict)
print(new_dict)
