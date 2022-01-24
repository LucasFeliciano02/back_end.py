from cliente import Cliente
from conta import Conta


print()
cliente1 = Cliente(f'Lucas', '312.321.312-01', 19)
print(cliente1)
print()

conta_lucas = Conta(cliente1, 150, 1000)
print(conta_lucas.cliente.nome, conta_lucas.consulta_saldo())

conta_lucas.depositar(1000.50)
print(conta_lucas.consulta_saldo())

conta_lucas.sacar(500)
print(conta_lucas.consulta_saldo())

conta_lucas.sacar(800)
print(conta_lucas.consulta_saldo())
