#!/usr/bin/python3


if __name__ == '__main__':
    from sys import argv
    j = len(argv) - 1
    i = 1
    if j > 1:
        print("{:d} arguments:".format(j))
    elif j == 0:
        print("{} arguments.".format(j))
    elif j == 1:
        print("{:d} argument:".format(j))
    for arg in argv:
        print("{}: {}".format(i, arg))
        i += 1
