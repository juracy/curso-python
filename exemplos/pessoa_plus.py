#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pessoa import Pessoa


class PessoaPlus(Pessoa):
    Count = 0

    def __init__(self, nome, idade=None):
        super(PessoaPlus, self).__init__(nome, idade)
        PessoaPlus.Count += 1

    # Uso básico do decorator @property criar propriedades read-only
    @property
    def isAndrogynous(self):
        # Avaliação dinâmica da existência de attributos
        return not hasattr(self, 'sexo')


if __name__ == '__main__':
    joao = PessoaPlus('João')
    maria = PessoaPlus('Maria', 17)
    pedro = PessoaPlus('Pedro')
    pedro.idade = 23

    # É possível criar atributos dinâmicos
    pedro.sexo = 'M'

    for o in [joao, maria, pedro]:
        print(o, 'Adulto' if o.isAdult() else '')
        if not o.isAndrogynous:
            print('{0} é {1}'.format(o.nome, {'M': 'Homem', 'F': 'Mulher'}[o.sexo]))

    print("Foram criadas {0} objetos do tipo Pessoa".format(PessoaPlus.Count))
