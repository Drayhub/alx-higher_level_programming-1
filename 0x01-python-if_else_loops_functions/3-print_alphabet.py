#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i == ord('e') and ord('q'):
        continue
    print("{}".format(chr(i)))