def main():
    usuarios = []
    contas = []
    AGENCIA = "0001"
    saldo = 0.0
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n=== SISTEMA BANCÁRIO v7 ===")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Extrato")
        print("4. Novo Usuário")
        print("5. Nova Conta")
        print("6. Listar Contas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor_str = input("Valor do saque: ").replace(',', '.')
                valor = float(valor_str)
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
                # Atualiza contador se saque válido
                if valor > 0 and valor <= limite and numero_saques < LIMITE_SAQUES and saldo >= valor:
                    numero_saques += 1
            except ValueError:
                print("\n⚠️ Valor inválido! Use números com até duas casas decimais.")
        
        elif opcao == "2":
            try:
                valor_str = input("Valor do depósito: ").replace(',', '.')
                valor = float(valor_str)
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("\n⚠️ Valor inválido! Use números com até duas casas decimais.")
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios=usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(
                agencia=AGENCIA,
                numero_conta=numero_conta,
                usuarios=usuarios
            )
            if conta:
                contas.append(conta)
                print(f"\n✔️ Conta {numero_conta} criada para {conta['usuario']['nome']}!")
        
        elif opcao == "6":
            listar_contas(contas=contas)
        
        elif opcao == "7":
            print("\n✅ Obrigado por usar nosso sistema!")
            break
        
        else:
            print("\n⚠️ Opção inválida!")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saques = numero_saques >= limite_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    
    if excedeu_saques:
        print("\n⚠️ Você já realizou 3 saques hoje!")
    elif excedeu_saldo:
        print("\n⚠️ Saldo insuficiente para o saque!")
    elif excedeu_limite:
        print(f"\n⚠️ O valor excede o limite de R$ {limite:.2f} por saque!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"➖ Saque: R$ {valor:.2f}")
        print("\n✔️ Saque realizado com sucesso!")
    else:
        print("\n⚠️ O valor do saque deve ser positivo!")
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"➕ Depósito: R$ {valor:.2f}")
        print("\n✔️ Depósito realizado com sucesso!")
    else:
        print("\n⚠️ O valor do depósito deve ser positivo!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n═════════ EXTRATO ═════════")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print("\n".join(extrato))
    print(f"\nSaldo atual: R$ {saldo:.2f}".replace('.', ','))
    print("════════════════════════════")

def criar_usuario(*, usuarios):
    print("\n═══ CADASTRO DE USUÁRIO ════")
    
    # Validação CPF
    while True:
        cpf = input("CPF (apenas números): ").strip()
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            print("⚠️ CPF deve ter 11 dígitos!")
            continue
            
        if any(u['cpf'] == cpf for u in usuarios):
            print("⚠️ CPF já cadastrado!")
            return
        break
    
    # Validação Endereço
    print("\nInforme o endereço:")
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    
    while True:
        estado = input("UF (2 letras): ").strip().upper()
        if len(estado) == 2 and estado.isalpha():
            break
        print("⚠️ UF deve ter 2 letras!")
    
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    
    # Demais dados
    nome = input("\nNome completo: ").title().strip()
    
    while True:
        data_nasc = input("Data de nascimento (dd-mm-aaaa): ").strip()
        partes = data_nasc.split('-')
        if len(partes) == 3 and all(p.isdigit() for p in partes):
            break
        print("⚠️ Formato inválido! Use dd-mm-aaaa")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })
    print(f"\n✔️ Usuário {nome} cadastrado com sucesso!")

def criar_conta_corrente(*, agencia, numero_conta, usuarios):
    print("\n═══ NOVA CONTA CORRENTE ════")
    cpf = input("CPF do titular (apenas números): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Busca usuário pelo CPF
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if not usuario:
        print("\n⚠️ CPF não cadastrado! Use a opção 4 primeiro.")
        return None
    
    return {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

def listar_contas(*, contas):
    print("\n════════ CONTAS CADASTRADAS ════════")
    if not contas:
        print("Nenhuma conta encontrada.")
    else:
        for conta in contas:
            print(f"""
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            CPF:\t\t{conta['usuario']['cpf']}
            Endereço:\t{conta['usuario']['endereco']}
            """.expandtabs(14))
    print("══════════════════════════════════════════")

if __name__ == "__main__":
    main()