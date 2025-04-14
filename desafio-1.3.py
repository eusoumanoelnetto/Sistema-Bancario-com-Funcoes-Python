# Funções existentes
def depositar(saldo, extrato, valor):
    """Função para depósito, recebe o saldo, o extrato e o valor do depósito."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque, recebendo argumentos somente por nome.

    Argumentos:
    saldo (float): O saldo atual da conta.
    valor (float): O valor do saque.
    extrato (str): O histórico de movimentações da conta.
    limite (float): O limite máximo permitido para saque.
    numero_saques (int): O número atual de saques realizados.
    limite_saques (int): O limite máximo de saques permitidos.

    Retorno:
    saldo (float): O saldo atualizado após o saque.
    extrato (str): O extrato atualizado após o saque.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    """Função para exibir o extrato."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    """Função para criar um novo usuário."""
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    if cpf in usuarios:
        print("Já existe um usuário com este CPF!")
    else:
        usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
        print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, contas, cpf, usuarios):
    """Função para criar uma nova conta corrente vinculada a um usuário."""
    if cpf not in usuarios:
        print("Usuário não encontrado! Cadastre o usuário antes de criar uma conta.")
        return

    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf})
    print(f"Conta corrente criada com sucesso! Agência: {agencia} | Conta: {numero_conta}")

def listar_contas(contas, usuarios):
    """Função para exibir todas as contas cadastradas."""
    print("\n================ CONTAS ================")
    for conta in contas:
        usuario = usuarios[conta["cpf"]]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']}")
    print("========================================")

# Programa principal
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = {}
    contas = []

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar usuário
    [cc] Criar conta corrente
    [lc] Listar contas
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(AGENCIA, contas, cpf, usuarios)

        elif opcao == "lc":
            listar_contas(contas, usuarios)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário! Até mais.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executa o programa
main()
