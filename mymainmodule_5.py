def add(*a):
    return sum(a)

def mul(*a):
    p = 1
    for i in a:
        p *= i
    return p

def test():
    print('I am inside the mainpymodule')