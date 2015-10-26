#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import factorial
from functools import reduce
from random import choice


def loops(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def funcional(n):
    if n < 1:
        return None if n < 0 else 1

    return reduce(lambda x, y: x * y, range(1, n + 1))


def funcional2(n):
    if n < 1:
        return None if n < 0 else 1

    return reduce(int.__mul__, range(1, n + 1))


def recursivo(n):
    if n < 1:
        return None if n < 0 else 1

    return n * recursivo(n - 1)


if __name__ == '__main__':
    functions = [factorial, loops, funcional, funcional2, recursivo]

    for i in range(20):
        func = choice(functions)
        print('{0:2d} {1:15s} {2:18d}'.format(i, func.__name__, func(i)))
