import doctest

"""
The function recives a list of integers and returns all the <= sum subsets of the list from the given num.
for every loop she generate a subset that <= from the given num.
*this func find all subsets only in depth of 2
"""


def bounded_subset(list: list, num: int):
    """
    >>> for i in bounded_subset([3, 1, 2,],4): print(i)
    [0, 3, 1, 2, [1, 3], [1, 2]]
    >>> for i in bounded_subset([4, 1, 2, 3,7,9,1,2], 8): print(i)
    [0, 4, 1, 2, 3, 7, [1, 4], [2, 4], [1, 2], [3, 4], [1, 3], [2, 3], [1, 7], [1, 1], [2, 2]]
    >>> for i in bounded_subset([10,20,4,87,21,54], 100): print(i)
    [0, 10, 20, 4, 87, 21, 54, [10, 20], [4, 10], [4, 20], [10, 87], [4, 87], [10, 21], [20, 21], [4, 21], [10, 54], [20, 54], [4, 54], [21, 54]]
    >>> for i in bounded_subset([1,1,1,1,1,1],2): print(i)
    [0, 1, [1, 1]]
    >>> for i in bounded_subset([10,20,30,40,50],5): print(i)
    [0]

    """
    subsets = [0]
    for i in list:
        if i not in subsets and i<num:
            subsets.append(i)

    differences = {}

    for number in list:
        candidate = []

        for diff in differences:

            if number - diff <= 0:
                temp_subset = [number] + differences[diff]
                temp_subset.sort()
                if temp_subset not in subsets:
                    subsets.append(temp_subset)

        for candidate in candidate:
            temp_diff = num - sum(differences[candidate[1]]) - candidate[0]
            differences[temp_diff] = differences[candidate[1]] + [candidate[0]]
        differences[num - number] = [number]
    yield subsets


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
