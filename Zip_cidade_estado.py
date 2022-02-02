"""
Zip - unindo iteraveis (nao precisa importar nada pra utilizar)
Zip_longest - itertools (precisa importar do modulo itertools ,se usa sem gerador
"""

from itertools import count

indice = count()  # conta o indice das cidades
cidades = ['Curitiba', 'São Paulo', 'Salvador', 'Amapá']
estados = ['PR', 'SP', 'BA', 'AM']

cidades_estado = zip(indice, estados, cidades)  # zip juntou as duas listas em uma unica lista com 2 dados

for indice, estados, cidades in cidades_estado:
    print(indice, estados, cidades)