import inspect
import doctest



"""
Functions for example
"""
def slice(string:str, start: int, end: int) -> str:
    return string[start:end]

def sum(x: int, y: int, z: float, t: int) ->float:
    return x * y - z + t


def float_sum(x:float,y:float,z:float) ->float:
    return x + y + z

def connecting_strings(s1:str, s2: str, s3: str) -> str:
    return s1+s2+s3





"""
The function accepts another function with arguments and activates the function 
only if the arguments are appropriate
return F result.
"""


def safe_call(f, *args,**kwargs):
    """
    >>> safe_call(connecting_strings,"saar",s2=" barel",s3=" hagever")
    saar barel hagever
    ----------------slice test----------------
    >>> safe_call(slice,"abcdefg",1,3)
    bc
    >>> safe_call(slice,"Saar Barel",5,10)
    Barel
    >>> safe_call(slice,"Research algorithms",0,8)
    Research
    >>> safe_call(slice,"1234567",3,5)
    45
    >>> safe_call(slice,5,1,3)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(slice,"abcdef","1",3)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(slice,3.5,1,3)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(slice,"abcdefg",1,"8")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations


    ----------------num_sum test----------------
    >>> safe_call(sum,1,3,3.5,0)
    -0.5
    >>> safe_call(sum,1,3,9.5,5)
    -1.5
    >>> safe_call(sum,1,3,2*2.5,7)
    5.0
    >>> safe_call(sum,1-3,3,3.5,0)
    -9.5
    >>> safe_call(sum,1,"a",3.5,1)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(sum,1,"fff",3.5,"qq")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(sum,1,"2",3.5,"7")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(sum,'1',2,3.5,7)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations

    ----------------float_sum----------------
    >>> safe_call(float_sum,1.5,3.7,2.5)
    7.7
    >>> safe_call(float_sum,1-3.8,3.7,8.0)
    8.9
    >>> safe_call(float_sum,1,"a",3.5,1)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(float_sum,1,"fff",3.5,"qq")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(float_sum,1,"2",3.5,"7")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(float_sum,1,2,3.5,7)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(float_sum,1,2,3,7)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(float_sum,1,2.8,3.5,7.4)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations

    ----------------connecting_strings----------------

    >>> safe_call(connecting_strings,"1-3.8","3.7","78")
    1-3.83.778
    >>> safe_call(connecting_strings,1,"a",3.5,1)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(connecting_strings,1,"fff",3.5,"qq")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(connecting_strings,1,"2",3.5,"7")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations


    """
    annotations = []
    f_inf = inspect.getfullargspec(f)
    f_args = f_inf.args
    for j in range(len(f_args)):
        if f_args[j] in f_inf.annotations:
            annotations.append(f_inf.annotations.get(f_args[j]))
        else:
            annotations.append(None)

    for j in range(len(args)):
        if annotations[j] is not None:
            if type(args[j]) != annotations[j]:
                raise Exception("The argument type doesn't fit the function annotations")
                continue
    return(f(*args,**kwargs))


if __name__ == '__main__':
     (failures, tests) = doctest.testmod(report=True)
     print("{} failures, {} tests".format(failures, tests))
