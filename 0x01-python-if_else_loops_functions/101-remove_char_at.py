#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        new_str += str[i]
    print(f"{new_str}")