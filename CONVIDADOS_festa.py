def valida_input(descri):
    while True:
        try:
            valor = float(input(descri).replace(',', '.'))
            return valor
        except Exception as ex:
            print('erro na digitação, insira novamente')


while True:
    numero = valida_input('insira o numero de participantes: ')
    pessoas = []

    for iteracao in range(int(numero)):
        pessoas.append(input('escreva um nome: '))

    print(f'os convidados sao: {pessoas}')

