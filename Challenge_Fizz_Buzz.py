# FIZZ BUZZ

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'Fizz Buzz, {n} é inteiramente divisivel por 3 e 5'
    if n % 5 == 0:
        return f'Buzz, {n} é inteiramente divisivel por 5'
    if n % 3 == 0:
        return f'Fizz, {n} é inteiramente divisivel por 3'
    return f'{n} não é inteiramente divisivel nem por 3 e nem por 5'


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
