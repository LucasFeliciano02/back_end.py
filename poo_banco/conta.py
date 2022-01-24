class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite
        
    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print(f'Foi depositado: {quant}$ Reais')
        else:
            print('Erro no deposito ')
    
    def consulta_saldo(self):
        return f'Saldo atual: {self.saldo}$ Reais'
    
    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            print('Saldo insuficiente')
        else:
            self.saldo -= quant
            print(f'Foi sacado {quant}$ Reais')
    