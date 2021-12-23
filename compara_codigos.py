while True:
    codigo1 = input('Escreva o codigo1: ')
    codigo2 = input('Escreva o codigo2: ')

    if codigo1 == codigo2:
        print('certo')
    else:
        print('errado')

    if input('Digite S para sair ou qualquer outra letra para continuar: ') == 's':
        print('Saindo...')
        break
    else:
        print('continuando...')
        continue
