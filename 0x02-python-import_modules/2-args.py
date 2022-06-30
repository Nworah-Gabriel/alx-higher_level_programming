#!/usr/bin/python3


if __name__ == '__main__':
    from sys import argv
    j = len(argv) - 1
    i = 1
    if j > 1:
        print("{:d} arguments:".format(j))
    elif j == 0:
        prrint(".")
    elif j == 1:
        print("{:d} argument:".format(j))
    while i != (j + 1):
        print("{}: {}".format(i, argv[i]))
        i += 1
