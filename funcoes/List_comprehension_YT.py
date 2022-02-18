"""
Video do youtube

List comprehension  =  Forma de construir uma lista no python de forma mais rápida em 1 linha de codigo

1º  =   Colocar o valor que vc quer que esteja na sua lista   
"""

# *  ---  (CASO 1): Dobrar preço de um produto  ---


# * (MODO NORMAL)

lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(f'\nDUPLICADOR, MODO NORMAL: {nova_lista_precos}')


# * (MODO COM LIST COMPREHENSION)

lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos2 = [preco * 2 for preco in lista_precos]  # (for) Pra cada um dos itens (in) dentro da lista de preços, adicionar preço x 2 dentro da nova_lista_precos
print(f'DUPLICADOR, MODO COM LIST COMPREHENSION: {nova_lista_precos}\n')



# *  --- (CASO 2): Todos os produtos que custarem aceima de 1000 dólares, impost de 50% sobre o valor final  ---


# * (MODO NORMAL)

lista_precos = [500, 1500, 2000, 100, 25]

imposto = []
for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco * 0.5)
print(f'IMPOSTO DE 50%, MODO NORMAL: {imposto}')


# * (MODO COM LIST COMPREHENSION)

imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(f'IMPOSTO DE 50%, MODO COM LIST COMPREHENSION: {imposto2}\n')
