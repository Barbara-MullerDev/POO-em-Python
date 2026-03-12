'''
Classe: conta

Atributos: titular, saldo

Métodos:
mostrar_saldo()
depositar_valor()
sacar_valor()
'''
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        return f"{self.titular} seu saldo é {self.saldo}"

    def depositar_valor(self, aumentar):
        self.saldo += aumentar

    def sacar_valor(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente"
        
        self.saldo -= valor

titular1 = Conta("Barbara", 700)
print(titular1.mostrar_saldo())

titular1.depositar_valor(550)
print(titular1.mostrar_saldo())

titular1.sacar_valor(20)
print(titular1.mostrar_saldo())
