import doctest

func_memory = {} #memory dict for all the functions {key:func name, val: func result}

"""
The function receives a function with one parameter and checks whether the current input is the same as the previous input.
 If so - it writes another appropriate message - it runs the function as usual
"""
def lastcall(func):
    """
    >>> sum(2)
    4
    >>> sum(2)
    You have already activated the function on (2,) and I have told you the answer is: 4
    >>> sum(4)
    8
    >>> power(2)
    4
    >>> power(4)
    16
    >>> sum(8)
    16
    >>> power(4)
    You have already activated the function on (4,) and I have told you the answer is: 16
    >>> concatenation("abc")
    'abcabc'
    >>> concatenation("aa")
    'aaaa'
    >>> concatenation("abc")
    You have already activated the function on ('abc',) and I have told you the answer is: abcabc
    >>> slice("saarbarel",0,4)
    'saar'
    >>> slice("saarbarel",0,4)
    You have already activated the function on ('saarbarel', 0, 4) and I have told you the answer is: saar
    >>> slice("saarbarel",0,5)
    'saarb'
    >>> subtraction_by_1(10)
    9
    >>> subtraction_by_1(100)
    99
    >>> subtraction_by_1(1)
    0
    >>> subtraction_by_1(10)
    You have already activated the function on (10,) and I have told you the answer is: 9
    """

    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if func.__name__ not in func_memory:
            func_memory[func.__name__]=[]
            func_memory[func.__name__].append(value)
            return value
        elif value not in func_memory[func.__name__] and func.__name__ in func_memory :
            func_memory[func.__name__].append(value)
            return value
        else:
            print(f'You have already activated the function on {args} and I have told you the answer is: {value}')

    return wrapper






@lastcall
def sum(x: int):
    return x + x

@lastcall
def power(x: int):
    return x ** 2

@lastcall
def concatenation(x: str):
    return x + x

@lastcall
def subtraction_by_1(x: float):
    return x-1

@lastcall
def slice(string:str, start: int, end: int) -> str:
    return string[start:end]


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
