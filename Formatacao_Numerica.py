
"""
:  =  quer dizer que vc vai fazer um padrao formatação apos os :
,  =  separador de milhar
.  =  quer colocar casas decimais

:.2f / :,.2f  =  numero float com duas casas decimais


"""

faturamento = 1580
custo = 500
lucro = faturamento - custo
print(f'\nO lucro foi de R${lucro:,.2f}')  # Deixa com (,) tudo menos as casas decimais que ficam com (.) 
                      #  f'R${lucro:,.2f}'  =  R$1,080.00
                      #  f'R${lucro:.2f}'   =  R$1080.00


# * Colocar margem em porcentagem De: (0.68..) Para (68 %)

margem = lucro / faturamento
print(f'A margem foi de {margem:.1%}\n')  # (.1%)  =  1 casa decimal  ==  (68.4%)   |   (.0%)  =  nenhuma casa decimal  == (68%)


# * Formato Brasileiro, trocando ponto por virgula

texto_lucro = f'R${lucro:_.2f}'
texto_lucro = texto_lucro.replace('.', ',').replace('_', '.')
print(f'O lucro foi de {texto_lucro}\n')
