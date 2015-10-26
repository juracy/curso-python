#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import sqrt

def delta(a, b, c):
    return b**2 - (4 * a * c)

def calc(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return (None, None)

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    return (x1, x2)

if __name__ == '__main__':
    print("2x² - 3x + 4 = 0     =>  x' = {0} x'' = {1}".format(*calc(2, -3, 4)))
    print("-2x² + 3x + 4 = 0    =>  x' = {0} x'' = {1}".format(*calc(-2, 3, 4)))
    print("2x² + 12x + 18 = 0     =>  x' = {0} x'' = {1}".format(*calc(2, 12, 18)))
    print("x² + 3x - 10 = 0     =>  x' = {0} x'' = {1}".format(*calc(1, 3, -10)))
