#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        tmp = -number
        value = tmp % 10
    else:
        value = number % 10
        print(value, end="")
        return value
