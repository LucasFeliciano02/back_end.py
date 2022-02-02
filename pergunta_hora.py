while True:
    try:
        usuario = input('nome de usuario: ')
        horario = float(input(f'escreva qualquer horario, {usuario}: '))

        if 0 <= horario <= 11:
            print(f'Bom dia {usuario}')
        elif 12 <= horario <= 17:
            print(f'Boa tarde {usuario}')
        elif 18 <= horario <= 24:
            print(f'Boa noite {usuario}')
        else:
            print('esse horario nao existe')
    except Exception as ex:
        print('Escreva somente numeros')
