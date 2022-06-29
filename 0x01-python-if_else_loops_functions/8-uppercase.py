#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(65, 81):
            continue
        elif ord(i) not in range(65, 91):
            char = ord(i) - 32
            print("{}".format(chr(char)), end="")
    print("\n", end="")
