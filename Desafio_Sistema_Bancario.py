menu = '''
[1] Sacar [2] Depositar [3] Extrato [4] Sair
'''

saldo = 300
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input('Escolha uma opção' + menu)

    if opcao == '1':
        saque = float(input('Digite o valor do saque: '))
        if saque > saldo or saque > limite:
            print('Saque cancelado, valor excede o saldo ou limite.')
            continue
        elif numeros_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingidos.')
            continue
        print('Retire o valor: R$', saque)
        numeros_saques += 1
        saldo -= saque
        extrato += f'Saque de R${saque:.2f}\n'
        
    elif opcao == '2':
        deposito = float(input('Digite o valor do depósito: '))
        if deposito <= 0:
            print('Valor de depósito inválido, operação cancelada.')
            continue
        else:
            saldo += deposito
            print('Depósito realizado com sucesso.')
            extrato += f'Depósito de R${deposito:.2f}\n'
            
    elif opcao == '3':
        print('Extrato:')
        print(extrato)
        
    elif opcao == '4':
        print("Obrigado por utilizar nosso sistema")
        break