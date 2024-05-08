menu = '''
========= Banco Dinheiro Brasil =========
=========================================
========= Digite uma das opções =========
=========================================
==========[1] Sacar =====================
=========================================
==========[2] Depositar =================
=========================================
==========[3] Extrato ===================
=========================================
==========[4] Cadastrar novo cliente ====
=========================================
==========[5] Nova conta corrente =======
=========================================
==========[6] Contas ====================
=========================================
==========[7] Sair ======================
'''

contas = []
numero_conta_atual = 0
saldo_conta = 300
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3

def saque():
    global numeros_saques, saldo_conta, extrato

    valor_saque = float(input("Digite o valor a ser sacado: "))
    if valor_saque <= saldo_conta and valor_saque <= limite:
        print('Retire o valor selecionado no local indicado')
        numeros_saques += 1
        saldo_conta -= valor_saque
        extrato += f'Saque de R$: {valor_saque:.2f}\n'
        print('Saque realizado com sucesso') 
    else:
        print('Saldo insuficiente ou limite de valor ultrapassado')

def depositos():
    global saldo_conta, extrato

    novo_deposito = float(input('Digite o valor do depósito: '))
    if novo_deposito > 0:
        saldo_conta += novo_deposito
        extrato +=  f'Depósito de R$: {novo_deposito:.2f}\n'
        print('Depósito realizado com sucesso')
    else:
        print('Valor inválido, operação cancelada')

def cadastro_cliente():
    global contas

    novo_cliente = {}
    novo_cliente['Nome'] = input('Digite o nome do cliente: ')
    novo_cliente['Data Nascimento'] = input('Digite a data de nascimento (DD/MM/AAAA): ')
    novo_cliente['CPF'] = input('Digite o CPF (somente números): ')
    
    endereco = {}
    endereco['Rua'] = input('Digite o nome da rua: ')
    endereco['Bairro'] = input('Digite o bairro: ')
    endereco['Cidade'] = input('Digite a cidade: ')
    endereco['Estado'] = input('Digite o estado: ')
   
    novo_cliente['Endereco'] = endereco
    
    contas.append(novo_cliente)
    print('Cliente cadastrado com sucesso')

def criar_conta_corrente():
    global contas, numero_conta_atual

    cpf = input('Digite o CPF do cliente (somente números): ')

    # Verificar se o CPF está cadastrado como cliente
    cliente_encontrado = False
    for cliente in contas:
        if cliente['CPF'] == cpf:
            cliente_encontrado = True
            break

    # Se o cliente não foi encontrado, exibir uma mensagem e retornar
    if not cliente_encontrado:
        print("CPF não encontrado. Por favor, cadastre o cliente primeiro.")
        return

    # Solicitar o nome para associar à nova conta
    usuario = input("Digite o nome do cliente: ")

    # Incrementar o número da conta
    numero_conta_atual += 1

    # Criar a nova conta corrente sem a agência
    nova_conta = {'Número da Conta': numero_conta_atual, 'CPF': cpf, 'Cliente': {'Nome': usuario}}
    nova_conta ['agencia'] = '0001'
    contas.append(nova_conta)
    print("Nova conta corrente criada com sucesso.")

    # Agora podemos adicionar a agência posteriormente, se necessário
    # nova_conta['Agência'] = '0001'



def imprimir_contas():
    global contas

    if not contas:
        print('Não há contas cadastradas.')
        return

    print('\n--- Contas Cadastradas ---')
    for dados in contas:
        print("--------------------------")
        for chave, valor in dados.items():
            if isinstance(valor, dict):
                print(f"{chave}:")
                for chave_interna, valor_interno in valor.items():
                    print(f"   {chave_interna}: {valor_interno}")
            else:
                print(f"{chave}: {valor}")
        print("--------------------------") 
    

while True:
    print(menu) 
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        saque()
    elif opcao == '2':
        depositos() 
    elif opcao == '3':
        print(extrato)   
    elif opcao == '4':
        cadastro_cliente()
    elif opcao == '5':
        criar_conta_corrente()
    elif opcao =='6':
        imprimir_contas()
    elif opcao == '7':
        print('Saindo...')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
