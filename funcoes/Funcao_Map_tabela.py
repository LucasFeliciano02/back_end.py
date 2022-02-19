"""
Aplica uma função em cada item de uma lista de itens

Função map pede 2 informações

- map(função que seja aplicada nos itens, lista de itens)
   - map(adicionar_imposto, precos)


Agora o map vai pegar essa função def, e vai automaticamente aplicar em cada item de precos, essa função
vai pegar 100/1500... e aplicar a função

"""

precos = [100, 1500, 1250, 2500]

def adicionar_imposto(preco):  # tem que receber um item como parametro
    return preco * 1.1  # 10 %


# com map()                         
                         #  função def/lambda  ,  lista
precos_com_imposto = list(map(adicionar_imposto, precos))

print(precos_com_imposto)



# * NA PRÁTICA, APLICANDO IMPOSTOS EM UMA BASE DE DADOS DO EXCEL

from IPython.display import display
import pandas as pd


tabela = pd.read_excel('Base_Vendas.xlsx')
display(tabela)


# * Pegando a coluna 'Preco Unitario' e aplicar o preco composto e criar uma nova coluna com esse nome, a função def aplica na lista

tabela['preco com Imposto'] = list(map(adicionar_imposto, tabela['Preco Unitario']))
display(tabela)


tabela.to_excel('Base_Vendas_Atualizadas.xlsx')
