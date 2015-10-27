#!/usr/bin/python3
# -*- coding: utf-8 -*-

class MyStr(str):
    def __div__(self, divisor):
        if not isinstance(divisor, str):
            raise TypeError('Divisor deve ser uma string')

        return self.split(divisor)


if __name__ == '__main__':
    dados = MyStr('14,18,45')
    print(dados / ',')
    print(dados / 2)
