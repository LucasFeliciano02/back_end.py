"""
list = converte um objeto iteravel em uma lista
objetos iteraveis sao aqueles que se pode iterar sobre cada elemento dele, com laço while, for


"""

l1 = list(range(1, 10))  # print(l2) = [1, 2 ,3 ,4 , 5 ,6 ,7 ,8 ,9]


for valor in l1:  # um de baixo do outro
    print(valor)


l2 = ['Clóvis', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}\n')


# GAME DE ADIVINHAR QUAL É A PALAVRA;


print('\nBem-vindo ao jogo da forca\nDICA: É cheiroso e quando se usa não há a necessidade de banhos!\n')

# a cada rodada do laço a pessoa digita uma letra pra tentar advinhar a palavra completa
secreto = 'perfume'
digitadas = []  # lista vazia
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhh isso nao vale, digite apenas uma letra.')
        continue  # nao sai do laço, vai pra proxima execução do laço

    digitadas.append(letra)

    if letra in secreto:  # se a letra que o usuario digitou, fizer parte da string criada =
        print(f'UHUUULLLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NAO EXISTE na palavra secreta.')
        digitadas.pop()
        

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:      # se a letra_secreta estiver dentro das letras que a pessoa digitou, ele vai
            # add nessse secreto_temporio a letra_secreta (add a letra)
            secreto_temporario += letra_secreta
        else:
            # é a palavra que ainda nao tem todo significado ex: **r**** = perfume
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCE GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta asim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')
    print()
