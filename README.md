# Sistema Bancário com Funções em Python

Este projeto é um sistema bancário simples desenvolvido em Python, com foco em boas práticas de programação, modularização e funcionalidades básicas de gestão bancária.

## Principais Melhorias

### Modularização
- Cada operação principal foi transformada em uma função.
- Separação clara entre operações bancárias e gestão de usuários/contas.

### Novas Funcionalidades
- **`criar_usuario()`**: Cadastra clientes com validação de CPF único.
- **`criar_conta_corrente()`**: Vincula contas a usuários existentes.

### Estrutura de Dados
- Uso de listas de dicionários para armazenar usuários e contas.
- Validação de existência de usuário pelo CPF.

### Boas Práticas
- Funções com responsabilidades únicas.
- Uso de parâmetros nomeados para maior clareza.
- Retorno de valores modificados em vez de usar variáveis globais.

## Funcionalidades

1. **Saque**:
   - Valida saldo disponível, limite por saque e número máximo de saques diários.
2. **Depósito**:
   - Registra o valor depositado no extrato.
3. **Extrato**:
   - Exibe o histórico formatado de movimentações e o saldo atual.
4. **Cadastro de Usuários**:
   - Armazena informações completas (nome, CPF, data de nascimento e endereço).
   - Garante que o CPF seja único.
5. **Criação de Contas**:
   - Vincula contas a usuários existentes.
   - Cada conta é associada à agência padrão ("0001") e recebe um número sequencial.

## Principais Alterações e Regras de Parâmetros

<<<<<<< HEAD
### Função `sacar`
- **Parâmetros**:
  - `valor`: Parâmetro posicional obrigatório (`/`).
  - Demais parâmetros (`saldo`, `extrato`, etc.): Somente keyword-only (`*`).
- **Exemplo de uso**:
  ```python
  sacar(100.0, saldo=500, extrato=[...])
=======
1. Execute o script principal (`desafio-2.0.py` ou `desafio-1.3.py`).
2. Siga o menu interativo para realizar operações bancárias ou gerenciar usuários e contas.
3. Cada nova conta é automaticamente vinculada à agência padrão ("0001") e recebe um número sequencial.

## Estrutura do Projeto

- **`desafio.py`**: Versão inicial do sistema com funcionalidades básicas.
- **`desafio-1.3.py`**: Versão intermediária com modularização e introdução de gestão de usuários e contas.
- **`desafio-2.0.py`**: Versão final com melhorias na estrutura de dados, validações e boas práticas.

## Requisitos

- Python 3.6 ou superior.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou novas funcionalidades.

## Licença

Este projeto é de uso livre e aberto para fins educacionais e de aprendizado.
>>>>>>> 738fab471079231ea9c939994737e054168965a9
