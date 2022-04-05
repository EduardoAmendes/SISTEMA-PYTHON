class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quant):
        if quant > limite:
            self.saldo += quant
            print("Foi Depositado:", quant)
        else:
            print("Erro no deposito")

    def consultar(self):
        return self.saldo

    def sacar(self):
        if self.saldo - quant < limite:
            print("Saldo insuficiente")
        else:
            self.saldo -= quant
            print("Foi Depositado:", quant)