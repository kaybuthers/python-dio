menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 1000
extrato = ''
limite = 500
limite_diario = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Quanto gostaria de depositar? '))

        if valor > 0:
            print(f'Depósito no valor de R$ {valor:.2f} efetuado com sucesso.')
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Por favor, deposite um valor válido.')

    elif opcao == 's':
        valor = float(input('Quanto gostaria de sacar? '))

        if valor > limite or limite_diario == 0:
            print('Saque não permitido por ultrapassar o limite.')
        elif saldo <= 0:
            print('Saque não permitido. Saldo insuficiente.')
        elif valor > 0:
            print(f'Saque no valor de R$ {valor} efetuado com sucesso.')
            extrato += f'Saque: R$ {valor:.2f}\n'
            limite_diario -= 1
            saldo -= valor
        else:
            print("Digite um valor válido")

    elif opcao == 'e':
        print('\n=========== EXTRATO ==========')
        print('Não foram realizadas moimentações.' if not extrato else extrato)
        print(f'Seu saldo é de R$ {saldo:.2f}')
        print('\n==============================')

    elif opcao == 'q':
        break
    
    else:
        print('Digite uma opção válida.')
