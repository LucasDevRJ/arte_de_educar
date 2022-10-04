def cadastrarAluno():
    print('-' * 30, '|CADASTRAR ALUNO|', '-' * 30)

    alunos = []
    aluno = []

    quantidadeAlunos = int(input('Digite a quantidade de alunos que deseja cadastrar: '))

    for i in range(0, quantidadeAlunos, 1):
        nome = str(input('Digite o nome: '))
        sobrenome = str(input('Digite o sobrenome: '))
        dataNascimento = str(input('Digite a data de nascimento: '))
        tipoEnsino = int(input('Opção 1 - Ensino Fundamental\n2 - Ensino Médio\nDigite: '))
        genero = str(input('Digite o gênero: '))

        aluno.append(nome)
        aluno.append(sobrenome)
        aluno.append(dataNascimento)
        aluno.append(tipoEnsino)
        aluno.append(genero)

def exibeMenu():
    while True:
        print('-' * 30, '|MENU PRINCIPAL|', '-' * 30)
        print('Bem-vindo(a) ao sistema escolar "Arte de Educar".')
        print('Opção 1 - Cadastrar aluno.')
        print('Opção 2 - Cadastrar nota.')
        print('Opção 3 - Consultar aluno.')
        print('Opção 4 - Cadastrar professor.')
        print('Opção 5 - Consultar professor.')
        print('Opção 6 - Sair.')
        print('-' * 79)
        try:
            opcao = int(input('Digite sua opção desejada: '))
            print()

            if opcao == 1:
                cadastrarAluno()

        except ValueError:
            print('Dígito incorreto!\nDigite somente as opções presentes.')
            print()
            continue

exibeMenu()
