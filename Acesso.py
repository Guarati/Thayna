from Classes import Aluno, Empresa


def cadastro(lista):
    print('''Qual seu tipo de usuário:
1 - Aluno
2 - Empresa''')

    escolha = input('R: ').strip()

    if '1' in escolha or 'ALUNO' in escolha.upper():
        print('''\nEscreva suas informações NESSA ORDEM:
Nome, Senha, Área, Período, Dias Disponíveis:''')

        nome = input('Nome: ').strip()
        senha = input('Senha: ').strip()
        area = input('Área: ').strip()
        periodo = input('Período: ').strip()
        diasdisponiveis = input('Dias Disponíveis: ').strip()

        aluno_obj = Aluno(nome, senha, area, periodo, diasdisponiveis)
        print(f"\nCadastro realizado: {aluno_obj.get_info()}")
        lista.append(aluno_obj)

    elif '2' in escolha or 'EMPRESA' in escolha.upper():
        print('''\nEscreva suas informações NESSA ORDEM:
Nome, Senha, Área, Período, Salário:''')

        nome = input('Nome: ').strip()
        senha = input('Senha: ').strip()
        area = input('Área: ').strip()
        periodo = input('Período: ').strip()
        salario = input('Salário: ').strip()

        empresa_obj = Empresa(nome, senha, area, periodo, salario)
        print(f"\nCadastro realizado: {empresa_obj.get_info()}")
        lista.append(empresa_obj)

    else:
        print("\nEscolha inválida. Tente novamente.")


def logon(lista):
    print('\nDigite seu login:')
    usuario = input('Usuário: ').strip()
    senha = input('Senha: ').strip()

    for item in lista:
        if isinstance(item, Aluno) or isinstance(item, Empresa):
            if item.get_nome() == usuario and item.get_senha() == senha:
                print(f"\nVocê está logado:\n{item.get_info()}")
                return

    print("\nUsuário ou senha incorretos.")
