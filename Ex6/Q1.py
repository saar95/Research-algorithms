import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

'''
This function gets 2 functions and a range of X values.
And draws the functions and the points of intersection between them.
'''


def plot_func(x_space, func_1, func_2):
    plt.plot(x_space, func_1(x_space), x_space, func_2(x_space))
    plt.grid()
    plt.show()


def plotIntersection(x_space, f, g):
    for x0 in x_space:
        check = fsolve(lambda x: f(x) - g(x), x0)
        fTemp = "%.6f" % f(check[0])
        gTemp = "%.6f" % g(check[0])
        if x_space[0] <= check[0] and x_space[-1] >= check[0] and fTemp == gTemp:
            plt.plot(check[0], f(check[0]), 'ro')

    plot_func(x_space, f, g)


if __name__ == '__main__':
    '''Example 1'''
    f = lambda x: x ** 2
    g = lambda x: x + 10
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    '''Example 2'''
    f = lambda x: np.sin(x)
    g = lambda x: 0.2 * x
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    '''Example 3'''
    f = lambda x: x * 2 - 5
    g = lambda x: np.cos(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    '''Example 4'''
    f = lambda x: np.sin(x)
    g = lambda x: np.cos(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)
