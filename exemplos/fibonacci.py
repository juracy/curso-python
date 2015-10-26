#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv

def fibo(n):
    result = [0, 1]

    for i in range(2, n):
	result.append(result[-2] + result[-1])

    return result

if __name__ == '__main__':
    print('\n'.join(str(x) for x in fibo(int(argv[1]))))
