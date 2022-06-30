#!/usr/bin/python3
if __name__ == '__main__':
    import add_0 as add_module
    a = 1
    b = 2
    add = add_module.add(a, b)
    print("{:d} + {:d} = {:d}\n".format(a, b, add))
