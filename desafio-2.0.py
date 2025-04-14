def main():
    usuarios = []
    contas = []
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Extrato")
        print("4. Novo Usuário")
        print("5. Nova Conta")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            # Atualiza o contador apenas se o saque foi válido
            if valor > 0 and valor <= limite and numero_saques < LIMITE_SAQUES:
                numero_saques += 1
        
        elif opcao == "2":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(valor=valor, saldo=saldo, extrato=extrato)
        
        elif opcao == "3":
            exibir_extrato(saldo=saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios=usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(agencia=AGENCIA, numero_conta=numero_conta, usuarios=usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            break
        
        else:
            print("Opção inválida, tente novamente.")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\n⚠️ Limite diário de saques atingido!")
    elif valor > saldo:
        print("\n⚠️ Saldo insuficiente!")
    elif valor > limite:
        print(f"\n⚠️ Valor excede o limite máximo por saque de R$ {limite:.2f}!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"➖ Saque: R$ {valor:.2f}")
        print("\n✔️ Saque realizado com sucesso!")
    else:
        print("\n⚠️ Valor inválido para saque!")
    return saldo, extrato

def depositar(*, valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"➕ Depósito: R$ {valor:.2f}")
        print("\n✔️ Depósito realizado com sucesso!")
    else:
        print("\n⚠️ Valor inválido para depósito!")
    return saldo, extrato

def exibir_extrato(*, saldo, extrato):
    print("\n═════════ EXTRATO ═════════")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("════════════════════════════")

def criar_usuario(*, usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n⚠️ Já existe usuário com este CPF!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/UF): ")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("\n✔️ Usuário cadastrado com sucesso!")

def criar_conta_corrente(*, agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if not usuario:
        print("\n⚠️ Usuário não encontrado!")
        return None
    
    print("\n✔️ Conta criada com sucesso!")
    return {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

if __name__ == "__main__":
    main()
