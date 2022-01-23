#   def abastecer(self, litros): 
#       self.tanque += litros


class Veiculo:
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    def abastecer(self, litros):
        if self.tanque + litros > 500:
            print('Tanque atingiu sua capacidade maxima de 500 L')    
        else:
            self.tanque += litros
            print(f'Reabasteceu: {litros} L')
         