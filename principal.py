
def cadastrarAluno():
    print('-' * 30, '|CADASTRAR ALUNO|', '-' * 30)

    alunos = []

    quantidadeAlunos = int(input('Digite a quantidade de alunos que deseja cadastrar: '))

    for i in range(0, quantidadeAlunos, 1):
        nome = str(input('Digite o nome: '))

        while not nome.isalpha():
            print('Dígito incorreto!\nDigite somente letras e acentos.')
            nome = str(input('Digite o nome: '))

        sobrenome = str(input('Digite o sobrenome: '))

        while not sobrenome.isalpha():
            print('Dígito incorreto!\nDigite somente letras e acentos.')
            nome = str(input('Digite o nome: '))

        dataNascimento = str(input('Digite a data de nascimento: '))
        tipoEnsino = int(input('\nOpção 1 - Ensino Fundamental\nOpção 2 - Ensino Médio\nDigite: '))
        genero = str(input('Digite o gênero: '))

        alunos.append([nome, sobrenome, dataNascimento, tipoEnsino, genero])
        print(alunos)

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
