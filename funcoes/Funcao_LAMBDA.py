"""
Funções anônimas - nao define ela

é como se fosse uma função def

"""

# * Calculando imposto com função normal

preco = 1000

def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(preco))


# * Calculando imposto com função LAMBDA
# * Ela recebe o que está antes dos : como informação para ela funcionar e dps dos : ela diz o que te da como resposta


preco2 = 500

calcular_imposto2 = lambda x: x * 0.3  # * Recebe uma informação para funcionar e te da como resposta aquela informação recebida * 0.3

print(calcular_imposto2(preco2))  # o (x) é o (preco)


# * Aplicando funcao lamda dentro de outros métodos, que é onde mais há vantagem
# * Usa uma função como parametro para uma outra função
# * (map)   =   Pega uma lista de informações e aplica sobre cada um dos valores desta lista uma função


precos = [100, 500, 10, 25]  # cada um desses numeros serao multipliocados por 0.3 pois eles sao o (x)

                  #      funcao    , lista de informações
impostos = list(map(lambda x: x*0.3, precos))  # A lista de informações(precos) recebe um valor(precos) e da como resposta esse valor * 0.3
print(impostos)
