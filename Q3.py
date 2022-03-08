import doctest

"""
The function receives an actual function and two numbers and finds its root 
at the end defined by the numbers according to the Newton-Raphson method
return the root.
"""

def find_root(f, x1, x2) -> float:
    """
    >>> (find_root(lambda x: x ** 2 - 4, 2, 3))
    2
    >>> (find_root(lambda x: x ** 2 - 4, 2, 5))
    2
    >>> (find_root(lambda x: x ** 2 - 4, 7, 3))
    5
    >>> (find_root(lambda x: x ** 3 - 4, 2, 3))
    1
    >>> (find_root(lambda x: x ** 4 - 4*x+5, 20, 30))
    18
    >>> (find_root(lambda x: x ** 2 - 5*x+2, 15, 3))
    9
    >>> (find_root(lambda x: x ** 2, 14, 8))
    11
    """
    EPS = 0.0001
    root = (x1 + x2) / 2
    my_eps = eps_calc(f,root)
    while my_eps >= EPS and x1 <= root <= x2:
        root = root - my_eps
        my_eps = eps_calc(f,root)

    print((int)(root))

def f1(f,x):
    h = 0.0001
    return float((f(x + h) - f(x)) / h)

def eps_calc(f,root):
    return float(f(root) / f1(f,root))

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
