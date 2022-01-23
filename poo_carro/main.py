from veiculo import Veiculo
from carro import Carro

caminhao = Veiculo('red', '8', 'Ford', 300)

print('\nCAMINHAO: ')
print('\nCor: ', caminhao.cor, '\nMarca: ', caminhao.marca, '\nrodas: ', 
      caminhao.rodas, '\nL no tanque:', caminhao.tanque)
caminhao.abastecer(200)
print(f'L no Tanque com reabastecimento: {caminhao.tanque}')

carro = Carro('Blue', '4', 'Ford', 20)

print('\nCARRO: ')
print('\nCor: ', carro.cor, '\nMarca: ', carro.marca, '\nrodas: ', 
      carro.rodas, '\nL no tanque:', carro.tanque)
carro.abastecer(20)
print(f'L no Tanque com reabastecimento: {carro.tanque}')
