from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, rodas, marca, tanque):
        Veiculo.__init__(self, cor, rodas, marca, tanque)
        
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Tanque atingiu sua capacidade maxima de 50 L')
        else:
            self.tanque += litros
            print(f'Reabasteceu: {litros} L')
            