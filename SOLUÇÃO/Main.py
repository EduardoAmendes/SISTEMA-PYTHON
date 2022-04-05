from cliente import Cliente
from conta import Conta

print("============CONTA============")
nome = input('Seu nome: ')
cpf = input('Seu CPF: ')
idade = input('Sua idade: ')
cliente1 = Cliente(nome, cpf, idade)
conta = Conta(cliente1, 100.18, 1000)
print("============CONTA============")

print("")
print("========================")
print("Consultar Saldo: Digite 1")
print("Sacar: Digite 2")
print("Depositar: Digite 3")
print("========================")
print("")

print("")
menu = input("")
print("")

for menu in menu:
    if menu == '1':
        print('Seu Saldo é de: ',conta.saldo)
    elif menu == '2':
        conta.saque = float(input("Digite o valor que irá sacar: "))
        conta.saque -= conta.saldo
        print("Seu saldo é de: ", conta.saque)
    elif menu == '3':
        conta.depositar = float(input('Digite o valor do deposito: '))
        print("Foi depositado o valor de:", conta.depositar)
        conta.depositar += conta.saldo
        print("Seu Saldo é de: ", conta.depositar)

    else:
        print("Digite de 1 a 3")


print("")
print("========================")
print("AÇÕES FINALIZADAS")
print("========================")
print("")