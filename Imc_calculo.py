print('bem vindo ao calculo de indice de massas corporal')


def valida_input(descri):
    while True:
        try:
            valor = float(input(descri).replace(',', '.'))
            return valor
        except Exception as ex:
            print(f'erro ao converter valor informado: {ex}')


while True:
    idade = valida_input('escreva sua idade: ')
    peso = valida_input('escreva seu peso: ')
    altura = valida_input('escreva sua altura em m: ')
    imc = peso / (altura ** 2)
    print(f'seu imc é: {imc:.2f}')

    if imc <= 18.5:
        print('você está abaixo do peso')
    elif 18.5 <= imc <= 24.9:
        print('Seu peso está normal')
    elif 25 <= imc <= 29.9:
        print('Você está com sobrepeso')
    elif 30 <= imc <= 34.9:
        print('Obesidade Grau 1')
    elif 35 <= imc <= 39.9:
        print('Obesidade grau 2')
    elif imc >= 40:
        print('Obesidade morbida')

    if input('Digite s para sair ou c para continuar: ') == 's':
        print('saindo')
        break

