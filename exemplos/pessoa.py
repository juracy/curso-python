#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pessoa(object):
    MaiorIdade = 18

    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome

        return "{0} ({1:d} anos)".format(self.nome, self.idade)

    def isAdult(self):
        # Após não encontrar um atributo no objeto, procura-se na classe
        return (self.idade or 0) > self.MaiorIdade


if __name__ == '__main__':
    joao = Pessoa('João')
    maria = Pessoa('Maria', 17)
    pedro = Pessoa('Pedro')
    pedro.idade = 23

    for o in [joao, maria, pedro]:
        print(o, 'Adulto' if o.isAdult() else '')
