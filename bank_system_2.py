import datetime, textwrap

def menu():
    menu = '''\n
    ======== MENU ========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [lc]\tListar Contas
    [cc]\tCriar Conta Corrente
    [nu]\tCadastrar Novo Usuário
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        #extrato += f'Depósito feito em {dia_convertido}:\t\tR$ {valor:.2f}\n'
        extrato += f'Depósito:\t\tR$ {valor:.2f}\n'
        print(f'Depósito no valor de R$ {valor:.2f} efetuado com sucesso.')
    else:
        print('Por favor, deposite um valor válido.')
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > limite:
        print('Saque não permitido por ultrapassar o limite de saque por saque.')
    elif valor > saldo:
        print('Saque não permitido. Saldo insuficiente.')
    elif numero_saques >= limite_saques:
        print('Saque não permitido por ultrapassar o limite diário de saques.')
    elif valor > 0:
        #extrato += f'Saque feito em {dia_convertido}:\t\tR$ {valor:.2f}\n'
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        saldo -= valor
        print(f'Saque no valor de R$ {valor} efetuado com sucesso.')
    else:
        print("Digite um valor válido")
    return saldo, extrato, numero_saques

def extrato(saldo, /, *, extrato):
    print('\n=========== EXTRATO ==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Seu saldo é de R$ {saldo:.2f}')
    print('\n==============================')

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input('Informe o CPF a ser cadastrado (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Já existe usuário cadastrado neste CPF!')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascmineto (no formato dd-mm-aaaa): ')
    endereco = input('Informe o endereço (no formato: logradouro - número - bairro - cidade/sigla do estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('\nUsuário cadastrado com sucesso!')
    
    # Deve armazenar os usuários em uma lista. Nome, data de nascimento, cpf e endereço. Endereço é logradouro - nro - bairro - cidade/sg_estado. CPF apenas numeros (string). Não pode cpf duplicado.

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n Usuario não encontrado. Cadastre um usuário.')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 10)
        print(textwrap.dedent(linha))

def main():
    LIMITE = 500
    AGENCIA = '0001'

    saldo = 0
    extrato = ''
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    #hoje = datetime.datetime.today()

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Quanto gostaria de depositar? '))
            #dia_hora = datetime.datetime.now()
            #dia_convertido = dia_hora.strftime('%d/%m/%Y %H:%M:%S')

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Quanto gostaria de sacar? '))
            #dia_hora = datetime.datetime.now()
            #dia_convertido = dia_hora.strftime('%d/%m/%Y %H:%M:%S')
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques= numero_saques, limite_saques=limite_saques)
            
        elif opcao == 'e':
            extrato(saldo, extrato =extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'cc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
    
        else:
            print('Digite uma opção válida.')


main()
