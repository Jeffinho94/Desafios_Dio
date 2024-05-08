menu = '''
========= Banco Dinheiro Brasil =========
=========================================
========= Digite uma das opçoes =========
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
contas = ''
saldo_conta = 300
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3

def saque ():
    global numeros_saques
    global saldo_conta
    global extrato
    
    valor_saque = float((input("Digite o valor a ser sacado")))
    if valor_saque <= saldo_conta and valor_saque <= limite:
        print('Retire o valor selecionado no local indicado')
        numeros_saques += 1
        saldo_conta -= valor_saque
        extrato += f'Saque de R$:{valor_saque:.2f}\n'
        print('Saque realizado com sucesso') 
    else :
        print('saldo insulficiente, ou limite de valor ultrapasado')        
                    
def depositos ():
    global saldo_conta
    global extrato
    
    novo_deposito = float(input('Digite o valor do deposito'))
    if novo_deposito > 0:
        saldo_conta += novo_deposito
        extrato +=  f'Deposito de R$: {novo_deposito:.2f}\n'
        print('Deposito realizado com sucesso')
        
    else :
        print('Valor invalido, operação cancelada')    
    

def cadastro_cliente ():
    novo_cliente = {}
    novo_cliente['Nome'] = input('Digite o nome do cliente')
    novo_cliente['Data Nascimento'] = input('Digite a data de nascimento')
    novo_cliente['CPF'] = int(input('Digite o cpf, somente numeros'))
    
    endereco = {}
    
    endereco['Rua'] = input('Digite o nome da rua:')
    endereco['Bairro'] = input('Digite o bairo:')
    endereco['Cidade'] = input('digite a cidade')
    endereco['Estado'] = input('Digite o estado')
    
    novo_cliente['Endereço'] = endereco
    print('Cliente cadastrado com sucesso')
    print('Nova conta conrrete criada ')
   
    return novo_cliente

def nova_conta_corrente(novas_contas):
    global contas
    cliente = cadastro_cliente()
    cpf = cliente['CPF']
    usuario = cliente['Nome']
    numero_conta = len(novas_contas) + 1  
    nova_conta = {'agencia': '0001', 'Numero da conta': numero_conta, 'usuario': usuario, 'CPF': cpf}
    novas_contas.append(nova_conta)
    contas += novas_contas
    return novas_contas

    
def imprimir_contas():
    if not contas:
        print('Não há contas cadastradas.')
        return

    print('\n--- Contas Cadastradas ---')
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['Numero da conta']}")
        print(f"Usuário: {conta['usuario']}")
        print(f"CPF: {conta['CPF']}")
        print("--------------------------")
    print()

 

  
    

    
            
while True:
    print(menu) 
    opcao = input('Escolha uma opção')

    if opcao == '1':
        saque()
    
    elif opcao == '2':
        depositos() 
                
    elif opcao == '3':
       print(extrato)   
        
    elif opcao == '4':
        cadastro_cliente()
       
    elif opcao == '5':
        nova_conta_corrente()
    
    elif opcao =='6':
        imprimir_contas()
        
    elif opcao == '7':
        print('Saindo...')
        break
    
    else:
        print('Opçao invalida')        
        
                    
        
       
    