import tkinter as tk
import time
import os

def tela_boas_vindas():
    """
    Cria uma janela de boas-vindas com a mensagem:
    "Bem-vinda ao banco Manoel Coelho pela Dio"
    Essa janela ficará aberta por 3 segundos e depois será fechada.
    """
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Bem-vinda!")
    
    # Define o tamanho da janela (400x200 pixels)
    largura_janela = 400
    altura_janela = 200
    
    # Pega a largura e a altura da tela do usuário
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição para centralizar a janela
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
    
    # Configura a cor de fundo da janela (opcional)
    janela.configure(bg="#f0f0f0")
    
    # Cria um widget Label com a mensagem de boas-vindas
    mensagem = tk.Label(
        janela,
        text="Bem-vinda ao banco\nManoel Coelho pela Dio",
        font=("Helvetica", 16),
        bg="#f0f0f0",
        fg="#333"
    )
    mensagem.pack(expand=True)
    
    # Atualiza a janela para desenhá-la e aguarda 3 segundos
    janela.update()
    time.sleep(3)
    
    # Fecha a janela de boas-vindas
    janela.destroy()

def limpar_tela():
    """Limpa o terminal para melhorar a experiência do usuário."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pede para o usuário pressionar ENTER antes de continuar."""
    input("\nPressione ENTER para continuar...")

def tratar_valor(valor_str):
    """
    Converte valores que podem usar vírgula ou ponto como separador decimal para float.
    Retorna None em caso de erro.
    """
    try:
        return float(valor_str.replace(",", "."))
    except ValueError:
        print("Valor inválido! Certifique-se de informar um número válido (ex.: 1.35 ou 1,35).")
        return None

def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito.
    Recebe os argumentos por posição.
    """
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    
    Parâmetros (passados somente por nome):
      - saldo (float): saldo atual.
      - valor (float): valor do saque.
      - extrato (list): lista de transações.
      - limite (float): limite permitido por saque.
      - numero_saques (int): número de saques já realizados.
      - limite_saques (int): quantidade máxima de saques permitidos.
      
    Retorna: saldo e extrato.
    Nota: O contador (numero_saques) deve ser atualizado no fluxo principal.
    """
    if valor <= 0:
        print("Operação falhou! Valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques atingido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato e o saldo atual, com formatação."""
    limpar_tela()
    print("========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print("\n".join(extrato))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    """
    Cria um novo usuário e o adiciona à lista de usuários.
    Verifica CPF e evita duplicidade.
    """
    cpf = input("Informe o CPF (somente números): ").strip()
    if not cpf.isdigit():
        print("CPF inválido! Digite apenas números.")
        return
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com este CPF!")
            return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta_corrente(agencia, contas, cpf, usuarios):
    """
    Cria uma nova conta corrente vinculada a um usuário identificado pelo CPF.
    """
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
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
    """Exibe todas as contas cadastradas com informações do titular."""
    limpar_tela()
    print("=========== CONTAS CADASTRADAS ===========")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario['nome']}")
    print("===========================================")

# Funções dos Serviços Adicionais
def pagar_boleto(saldo, extrato, /):
    print("\n--- Pagamento de Boleto ---")
    codigo = input("Informe o código do boleto: ")
    valor_input = input("Informe o valor do boleto: ")
    valor = tratar_valor(valor_input)
    if valor is None:
        return saldo, extrato
    if valor > saldo:
        print("Saldo insuficiente para pagar o boleto!")
    else:
        saldo -= valor
        extrato.append(f"Boleto (Código: {codigo}) pago: R$ {valor:.2f}")
        print("Boleto pago com sucesso!")
    return saldo, extrato

def pagar_imposto(servico, saldo, extrato, /):
    print(f"\n--- Pagamento de {servico} ---")
    numero = input(f"Informe o número do {servico}: ")
    valor_input = input(f"Informe o valor do {servico}: ")
    valor = tratar_valor(valor_input)
    if valor is None:
        return saldo, extrato
    if valor > saldo:
        print("Saldo insuficiente para realizar o pagamento!")
    else:
        saldo -= valor
        extrato.append(f"{servico} (Número: {numero}) pago: R$ {valor:.2f}")
        print(f"{servico} pago com sucesso!")
    return saldo, extrato

def solicitar_segunda_via_cartao():
    print("\n--- Solicitação de Segunda Via de Cartão ---")
    numero_cartao = input("Informe o número do cartão: ")
    print(f"Segunda via do cartão {numero_cartao} solicitada com sucesso! Confira seu e-mail para mais detalhes.")

def menu_servicos(saldo, extrato):
    while True:
        limpar_tela()
        print("========== MENU DE SERVIÇOS ==========")
        print("1. Pagar Boleto")
        print("2. Pagar IPTU")
        print("3. Pagar IPVA")
        print("4. Solicitar Segunda Via de Cartão")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção de serviço: ").strip()
        if opcao == "1":
            saldo, extrato = pagar_boleto(saldo, extrato)
            pausar()
        elif opcao == "2":
            saldo, extrato = pagar_imposto("IPTU", saldo, extrato)
            pausar()
        elif opcao == "3":
            saldo, extrato = pagar_imposto("IPVA", saldo, extrato)
            pausar()
        elif opcao == "4":
            solicitar_segunda_via_cartao()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")
            pausar()
    return saldo, extrato

def main():
    saldo = 0.0
    limite = 500.0
    extrato = []         # Armazena as transações em formato de lista
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []        # Lista de usuários (cada um é um dicionário)
    contas = []          # Lista de contas

    while True:
        limpar_tela()
        print("========== SISTEMA BANCÁRIO ==========")
        print("[d] Depositar")
        print("[s] Sacar")
        print("[e] Extrato")
        print("[nu] Criar Usuário")
        print("[cc] Criar Conta Corrente")
        print("[lc] Listar Contas")
        print("[sv] Serviços")
        print("[q] Sair")
        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "d":
            valor_input = input("Informe o valor do depósito: ")
            valor = tratar_valor(valor_input)
            if valor is not None:
                saldo, extrato = depositar(saldo, valor, extrato)
            pausar()

        elif opcao == "s":
            valor_input = input("Informe o valor do saque: ")
            valor = tratar_valor(valor_input)
            if valor is not None:
                saldo_atual = saldo
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
                # Se o saque for efetuado (saldo diminuiu), atualiza o contador
                if saldo < saldo_atual:
                    numero_saques += 1
            pausar()

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            pausar()

        elif opcao == "nu":
            criar_usuario(usuarios)
            pausar()

        elif opcao == "cc":
            cpf = input("Informe o CPF do usuário para vincular à conta: ").strip()
            criar_conta_corrente(AGENCIA, contas, cpf, usuarios)
            pausar()

        elif opcao == "lc":
            listar_contas(contas)
            pausar()

        elif opcao == "sv":
            saldo, extrato = menu_servicos(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário! Até mais.")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")
            pausar()

if __name__ == "__main__":
    tela_boas_vindas()
    main()  # Ou a função principal do seu sistema bancário
