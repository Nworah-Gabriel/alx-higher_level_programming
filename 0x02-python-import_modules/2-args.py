#!/usr/bin/python3

import sys

if __name__ == '__main__':
    j = len(sys.argv) - 1
    i = 1
    if j > 1:
        print("{:d} arguments:".format(j))
    elif j == 0:
        prrint(".")
    elif j == 1:
        print("{:d} argument:".format(j))
    while i != (j + 1):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
