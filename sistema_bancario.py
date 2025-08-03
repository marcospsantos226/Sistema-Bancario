import datetime

# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500.00
AGENCIA = "0001"

# Estado do sistema
usuarios = []
contas = []

def menu():
    print("\n===== SISTEMA BANCÁRIO =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Criar usuário")
    print("[5] Criar conta")
    print("[6] Listar contas")
    print("[0] Sair")
    return input("Escolha uma opção: ")

# ----> Funções principais

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Valor inválido. Só é possível depositar valores positivos.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("❌ Limite diário de saques atingido.")
    elif valor <= 0:
        print("❌ Valor inválido. Digite um valor positivo.")
    elif valor > limite:
        print(f"❌ Valor excede o limite por saque de R$ {limite:.2f}.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque:    R$ {valor:.2f}")
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO BANCÁRIO =====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print("---------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("============================")

# ----> Funções auxiliares

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf):
        print("❌ CPF já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("❌ Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": [],
        "saques_diarios": 0
    })
    print(f"✅ Conta criada com sucesso. Número: {numero_conta}")

def listar_contas():
    if not contas:
        print("⚠️ Nenhuma conta cadastrada.")
        return

    for conta in contas:
        usuario = conta["usuario"]
        print(f"""
Agência: {conta['agencia']}
Número da Conta: {conta['numero_conta']}
Titular: {usuario['nome']}
CPF: {usuario['cpf']}
""")

# ----> Loop principal

while True:
    opcao = menu()

    if opcao == "1":
        numero = int(input("Informe o número da conta: "))
        conta = next((c for c in contas if c["numero_conta"] == numero), None)

        if conta:
            valor = float(input("Digite o valor do depósito: R$ "))
            conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "2":
        numero = int(input("Informe o número da conta: "))
        conta = next((c for c in contas if c["numero_conta"] == numero), None)

        if conta:
            valor = float(input("Digite o valor do saque: R$ "))
            conta["saldo"], conta["extrato"], conta["saques_diarios"] = sacar(
                saldo=conta["saldo"],
                valor=valor,
                extrato=conta["extrato"],
                limite=LIMITE_SAQUE_VALOR,
                numero_saques=conta["saques_diarios"],
                limite_saques=LIMITE_SAQUES
            )
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "3":
        numero = int(input("Informe o número da conta: "))
        conta = next((c for c in contas if c["numero_conta"] == numero), None)

        if conta:
            exibir_extrato(conta["saldo"], extrato=conta["extrato"])
        else:
            print("❌ Conta não encontrada.")

    elif opcao == "4":
        criar_usuario()

    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        listar_contas()

    elif opcao == "0":
        print("👋 Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
