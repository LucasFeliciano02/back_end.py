while True:
    usuario = input('Nome do Usuário: ')
    senha = input('Senha do Usuário: ')
    usuario_bd = 'xxx'
    senha_bd = '123456'

    if usuario == usuario_bd and senha == senha_bd:
        print('Entrando')
        break
    else:
        print('Usuário ou senha invalidos\nTente novamente ')
        continue
