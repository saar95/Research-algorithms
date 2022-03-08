import doctest


"""
The function accepts different types of data structures and sorts them.
return sorted parameter.
"""
def print_sorted(x):
    """
    >>> print(print_sorted({'c' : {'c' : 1, 'a' : 5, 'b' : 4}, 'a' : (8,4,1), 'b' : [6,1]}))
    {'a': (1, 4, 8), 'b': [1, 6], 'c': {'a': 5, 'b': 4, 'c': 1}}
    >>> print(print_sorted({'c': {'c': 2, 'a': 6, 'b': 3}, 'a': (9, 12, 1), 'b': [8,9,10,11]}))
    {'a': (1, 9, 12), 'b': [8, 9, 10, 11], 'c': {'a': 6, 'b': 3, 'c': 2}}
    >>> print(print_sorted({'z': {'x': 99, 'y': 51, 'b': 44}, 't': (86, 42, 11), 'd': [63, 41]}))
    {'d': [41, 63], 't': (11, 42, 86), 'z': {'b': 44, 'x': 99, 'y': 51}}
    >>> print(print_sorted({'c': {'c': 17, 'a': 52, 'b': 43}, 'a': [85, 54, 1], 'b': [62, 11]}))
    {'a': [1, 54, 85], 'b': [11, 62], 'c': {'a': 52, 'b': 43, 'c': 17}}
    """
    if(type(x) == list):
        temp_list = sorted(x)
        return list(print_sorted(x) for x in temp_list)
    elif(type(x) == set):
        temp_set = sorted(x)
        return set(print_sorted(x) for x in temp_set[0])
    elif(type(x) == dict):
        temp_dict={k: print_sorted(v) for k, v in sorted(x.items(), key=lambda i: i[0])}
        return temp_dict
    elif(type(x) == tuple):
        t = sorted(x)
        return tuple(print_sorted(i) for i in t)
    return x

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))