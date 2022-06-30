#!/usr/bin/python3

import calculator_1 as calc

if __name__ == '__main__':
    a = 10
    b = 5
    add = calc.add(a, b)
    sub = calc.sub(a, b)
    mul = calc.mul(a, b)
    div = calc.div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add))
    print("{:d} - {:d} = {:d}".format(a, b, sub))
    print("{:d} * {:d} = {:d}".format(a, b, mul))
    print("{:d} / {:d} = {:d}".format(a, b, div))
