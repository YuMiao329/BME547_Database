def sqrt(n):
    if n <= 0:
        raise ValueError("Sqrt cannot receive a negative number. You sent {}".format(n))

    x = n
    y = 1
    e = 0.000001
    while(x - y > e):
        x = (x+y)/2
        y = n/x
    return x

def add_posinteger(a,b):
    if a < 0 or b < 0:
        raise ValueError("cannot add negatives")
    if type(a) is not int or type(b) is not int:
        raise TypeError("cannot add non ints")
    return a+b
