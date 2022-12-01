#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(count))
        for i in range(1, (count + 1)):
            print("{}: {}".format(i, argv[i]))
