def parse_valor(input_str):
    """
    Converte o input do usuário para float,
    aceitando tanto vírgula quanto ponto como separador decimal.
    """
    try:
        return float(input_str.replace(",", "."))
    except ValueError:
        print("Valor inválido! Utilize números (ex.: 1.35 ou 1,35).")
        return None

def depositar(*, saldo, extrato, valor):
    """Realiza um depósito válido, atualizando saldo e extrato."""
    if valor is None:
        return saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"➕ Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque se as condições forem satisfeitas:
      - Valor positivo
      - Saldo suficiente
      - Valor não excede o limite do saque
      - Número de saques realizados não excede o limite diário

    Parâmetros (passados por nome):
      saldo (float): Saldo atual.
      valor (float): Valor do saque.
      extrato (list): Lista com o registro das transações.
      limite (float): Limite permitido para um saque.
      numero_saques (int): Quantidade de saques já realizados.
      limite_saques (int): Limite diário de saques.

    Retorno:
      saldo (float) e extrato (list).
      
    Observação: O parâmetro numero_saques é apenas lido; sua atualização deverá ser feita fora da função.
    """
    if valor is None:
        return saldo, extrato
    if valor <= 0:
        print("Valor inválido para saque!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print(f"Valor excede o limite de R$ {limite:.2f} por saque!")
    elif numero_saques >= limite_saques:
        print("Limite diário de saques atingido!")
    else:
        saldo -= valor
        extrato.append(f"➖ Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(*, saldo, extrato):
    """Exibe todas as transações realizadas e o saldo atual."""
    print("\n═════════ EXTRATO ═════════")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("════════════════════════════")

def criar_usuario(*, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Usuário criado com sucesso!")

def criar_conta_corrente(*, agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário para vincular à conta: ")
    if cpf not in usuarios:
        print("Usuário não encontrado. Cadastre o usuário primeiro!")
        return
    numero_conta = len(contas) + 1
    conta = {"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf}
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {agencia} | Conta: {numero_conta}")

def listar_contas(*, contas, usuarios):
    print("\n══════════ CONTAS ══════════")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            cpf = conta["cpf"]
            usuario = usuarios.get(cpf, {})
            nome = usuario.get("nome", "Não cadastrado")
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {nome}")
    print("════════════════════════════")

# Funções para Serviços Adicionais
def pagar_boleto(*, saldo, extrato):
    print("\n--- Pagamento de Boleto ---")
    codigo = input("Informe o código do boleto: ")
    valor_input = input("Informe o valor do boleto: ")
    valor = parse_valor(valor_input)
    if valor is None:
        return saldo, extrato
    if valor > saldo:
        print("Saldo insuficiente para pagar o boleto!")
    else:
        saldo -= valor
        extrato.append(f"💸 Boleto (Código: {codigo}) pago: R$ {valor:.2f}")
        print("Boleto pago com sucesso!")
    return saldo, extrato

def pagar_imposto(servico, *, saldo, extrato):
    print(f"\n--- Pagamento de {servico} ---")
    numero = input(f"Informe o número do {servico}: ")
    valor_input = input(f"Informe o valor do {servico}: ")
    valor = parse_valor(valor_input)
    if valor is None:
        return saldo, extrato
    if valor > saldo:
        print("Saldo insuficiente para realizar o pagamento!")
    else:
        saldo -= valor
        extrato.append(f"💸 {servico} (Número: {numero}) pago: R$ {valor:.2f}")
        print(f"{servico} pago com sucesso!")
    return saldo, extrato

def solicitar_segunda_via_cartao():
    print("\n--- Solicitação de Segunda Via de Cartão ---")
    numero_cartao = input("Informe o número do cartão: ")
    print(f"Segunda via do cartão {numero_cartao} solicitada com sucesso! Verifique seu e-mail para mais detalhes.")

def menu_servicos(saldo, extrato):
    while True:
        print("\n========== SERVIÇOS ==========")
        print("1. Pagar Boleto")
        print("2. Pagar IPTU")
        print("3. Pagar IPVA")
        print("4. Solicitar Segunda Via de Cartão")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção de serviço: ")

        if opcao == "1":
            saldo, extrato = pagar_boleto(saldo=saldo, extrato=extrato)
        elif opcao == "2":
            saldo, extrato = pagar_imposto("IPTU", saldo=saldo, extrato=extrato)
        elif opcao == "3":
            saldo, extrato = pagar_imposto("IPVA", saldo=saldo, extrato=extrato)
        elif opcao == "4":
            solicitar_segunda_via_cartao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")
    return saldo, extrato

def main():
    saldo = 0.0
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = {}      # Dicionário de usuários (chave: CPF)
    contas = []        # Lista de contas

    menu = """
========== SISTEMA BANCÁRIO ==========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Listar Contas
[7] Serviços
[0] Sair
======================================
Escolha uma opção: """

    while True:
        opcao = input(menu)

        if opcao == "1":
            valor_input = input("Informe o valor do depósito: ")
            valor = parse_valor(valor_input)
            saldo, extrato = depositar(saldo=saldo, extrato=extrato, valor=valor)

        elif opcao == "2":
            valor_input = input("Informe o valor do saque: ")
            valor = parse_valor(valor_input)
            saldo_antigo = saldo
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            # Se o saque foi efetuado, deduzimos o número de saques
            if saldo < saldo_antigo:
                numero_saques += 1

        elif opcao == "3":
            exibir_extrato(saldo=saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios=usuarios)

        elif opcao == "5":
            criar_conta_corrente(agencia=AGENCIA, contas=contas, usuarios=usuarios)

        elif opcao == "6":
            listar_contas(contas=contas, usuarios=usuarios)

        elif opcao == "7":
            saldo, extrato = menu_servicos(saldo, extrato)

        elif opcao == "0":
            print("Obrigado por usar o sistema bancário! Até mais.")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()
