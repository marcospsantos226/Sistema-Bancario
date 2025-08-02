import datetime

# Variáveis principais
saldo = 0.0
limite_saque = 500.00
extrato = []
saques_diarios = 0
LIMITE_SAQUES = 3

def menu():
    print("\n===== SISTEMA BANCÁRIO =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    return input("Escolha uma opção: ")

def depositar():
    global saldo, extrato
    valor = float(input("Digite o valor do depósito: R$ "))
    
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido. Só é possível depositar valores positivos.")

def sacar():
    global saldo, extrato, saques_diarios

    if saques_diarios >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
        return

    valor = float(input("Digite o valor do saque: R$ "))
    
    if valor <= 0:
        print("Valor inválido. Digite um valor positivo.")
    elif valor > limite_saque:
        print(f"Valor excede o limite por saque de R$ {limite_saque:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        saques_diarios += 1
        print("Saque realizado com sucesso.")

def ver_extrato():
    print("\n===== EXTRATO BANCÁRIO =====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
        print("---------------------------")
        print(f"Saldo atual: R$ {saldo:.2f}")
    print("============================")

# Loop principal
while True:
    opcao = menu()
    
    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        ver_extrato()
    elif opcao == "0":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
