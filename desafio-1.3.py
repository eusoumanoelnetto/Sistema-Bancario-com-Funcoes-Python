# Funções existentes
def depositar(saldo, valor, extrato, /):
    """Realiza a operação de depósito, recebendo argumentos apenas por posição."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza a operação de saque, recebendo argumentos somente por nome."""
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

def exibir_extrato(saldo, *, extrato):
    """Exibe o extrato da conta."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    """Cria um novo usuário para o sistema."""
    cpf = input("Informe o CPF (somente números): ").strip()
    if not cpf.isdigit():
        print("CPF inválido! Certifique-se de digitar apenas números.")
        return
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com este CPF!")
            return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro : bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, contas, cpf, usuarios):
    """Cria uma nova conta corrente vinculada a um usuário."""
    usuario_encontrado = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if not usuario_encontrado:
        print("Usuário não encontrado! Cadastre o usuário antes de criar uma conta.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    })
    print(f"Conta corrente criada com sucesso! Agência: {agencia} | Conta: {numero_conta}")

def listar_contas(contas):
    """Exibe todas as contas cadastradas no sistema."""
    print("\n================ CONTAS ================")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']}")
    print("========================================")

def tratar_valor(valor):
    """Converte valores que utilizam vírgula como separador decimal para o formato correto (com ponto)."""
    valor = valor.replace(",", ".")
    try:
        return float(valor)
    except ValueError:
        print("Valor inválido! Certifique-se de que está informando um número válido.")
        return None

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
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
            valor = input("Informe o valor do depósito: ")
            valor = tratar_valor(valor)
            if valor is not None:
                saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = input("Informe o valor do saque: ")
            valor = tratar_valor(valor)
            if valor is not None:
                saldo, extrato = sacar(
                    saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                    numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
                )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            cpf = input("Informe o CPF do usuário: ").strip()
            criar_conta_corrente(AGENCIA, contas, cpf, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário! Até mais.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()# Funções existentes
def depositar(saldo, valor, extrato, /):
    """Realiza a operação de depósito, recebendo argumentos apenas por posição."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza a operação de saque, recebendo argumentos somente por nome."""
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

def exibir_extrato(saldo, *, extrato):
    """Exibe o extrato da conta."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    """Cria um novo usuário para o sistema."""
    cpf = input("Informe o CPF (somente números): ").strip()
    if not cpf.isdigit():
        print("CPF inválido! Certifique-se de digitar apenas números.")
        return
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com este CPF!")
            return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro : bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, contas, cpf, usuarios):
    """Cria uma nova conta corrente vinculada a um usuário."""
    usuario_encontrado = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if not usuario_encontrado:
        print("Usuário não encontrado! Cadastre o usuário antes de criar uma conta.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    })
    print(f"Conta corrente criada com sucesso! Agência: {agencia} | Conta: {numero_conta}")

def listar_contas(contas):
    """Exibe todas as contas cadastradas no sistema."""
    print("\n================ CONTAS ================")
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']}")
    print("========================================")

def tratar_valor(valor):
    """Converte valores que utilizam vírgula como separador decimal para o formato correto (com ponto)."""
    valor = valor.replace(",", ".")
    try:
        return float(valor)
    except ValueError:
        print("Valor inválido! Certifique-se de que está informando um número válido.")
        return None

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
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
            valor = input("Informe o valor do depósito: ")
            valor = tratar_valor(valor)
            if valor is not None:
                saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = input("Informe o valor do saque: ")
            valor = tratar_valor(valor)
            if valor is not None:
                saldo, extrato = sacar(
                    saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                    numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
                )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            cpf = input("Informe o CPF do usuário: ").strip()
            criar_conta_corrente(AGENCIA, contas, cpf, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário! Até mais.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()