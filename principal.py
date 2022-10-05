contadoraMatricula = 100
alunos = []
contadoraMatricula += 1


def cadastrarAluno(matricula):
    print('-' * 30, '|CADASTRAR ALUNO|', '-' * 30)

    nome = str(input('Digite o nome: '))

    while not nome.isalpha():
        print('Dígito incorreto!\nDigite somente letras e acentos.')
        nome = str(input('Digite o nome: '))

    sobrenome = str(input('Digite o sobrenome: '))

    while not sobrenome.isalpha():
        print('Dígito incorreto!\nDigite somente letras e acentos.')
        sobrenome = str(input('Digite o sobrenome: '))

    dataNascimento = str(input('Digite a data de nascimento: '))

    while not dataNascimento.isdigit():
        print('Dígito incorreto!\nDigite números e caracteres matemáticos.')
        dataNascimento = str(input('Digite a data de nascimento: '))

    while True:
        try:
            tipoEnsino = int(input('Escolha a classficação de ensino\n'
                                   'Opção 1 - Ensino Fundamental\nOpção 2 - Ensino Médio\nDigite: '))
            if tipoEnsino == 1 or tipoEnsino == 2:
                break
        except ValueError:
            print('Dígito incorreto!\nDigite somente as opções válidas.')
            continue

    genero = str(input('Digite o gênero: '))

    while not genero == 'M' and genero == 'm' and genero == 'F' \
            or genero == 'f' and genero == 'O' and genero == 'o':
        print('Gênero inválido!\nDigite somente M, F ou O.')
        genero = str(input('Digite o gênero: '))

    if tipoEnsino == 2:
        tipoEnsino = 'Ensino Médio'
    else:
        tipoEnsino = 'Ensino Fundamental'

    nome = nome.upper()
    sobrenome = sobrenome.upper()
    genero = genero.upper()
    tipoEnsino = tipoEnsino.upper()

    aluno = {
        'Matrícula': matricula,
        'Nome': nome,
        'Sobrenome': sobrenome,
        'Data de Nascimento': dataNascimento,
        'Ensino': tipoEnsino,
        'Gênero': genero
    }

    alunos.append(aluno.copy())

    print('-' * 79)


def consultarAluno():
    while True:
        print('-' * 30, '|CONSULTAR ALUNO|', '-' * 30)
        print('Opção 1 - Consultar todos os alunos.')
        print('Opção 2 - Consultar um aluno.')

        try:
            opcao = int(input('Digite sua opção desejada: '))
            print()
            if opcao == 1:
                for aluno in alunos:
                    for key, value in aluno.items():
                        print('{}:{}'.format(key, value))
            elif opcao == 2:
                matricula = int(input('Digite a matrícula do aluno: '))
                for aluno in alunos:
                    if aluno['Matrícula'] == matricula:
                        for key, value in aluno.items():
                            print('{}:{}'.format(key, value))
                    else:
                        print('Matrícula inválida!')
            else:
                print('Dígito inválido!\nDigite alguma das opções.')

        except ValueError:
            print('Dígito inválido!\nDigite somente as opções.')



def cadastrarNota():
    global notaTeste, notaProva, materia
    materia = ''

    print('-' * 30, '|CADASTRAR NOTA|', '-' * 30)
    matricula = int(input('Digite a matrícula do aluno: '))

    for aluno in alunos:
        if aluno['Matrícula'] == matricula:
            print('Opção 1 - Cadastrar matéria.')
            print('Opção 2 - Cadastrar nota do teste.')
            print('Opção 3 - Cadastrar nota da prova.')
            print('Opção 4 - Ver média final.')

            opcao = int(input('Digite sua opção desejada: '))

            if opcao == 1:
                materia = input('Digite a matéria desejada: ')
                print('Matéria adicionada com sucesso!')

                print('Opção 1 - Cadastrar matéria.')
                print('Opção 2 - Cadastrar nota do teste.')
                print('Opção 3 - Cadastrar nota da prova.')
                print('Opção 4 - Ver média final.')

                opcao = int(input('Digite sua opção desejada: '))

                if len(materia) > 0:
                    if opcao == 2:
                        notaTeste = float(input('Digite a nota do teste: '))
                        print('Nota do teste adicionada com sucesso!')
                    elif opcao == 3:
                        notaProva = float(input('Digite a nota da prova: '))
                        print('Nota da prova adicionada com sucesso!')
                    elif opcao == 4:
                        media = (notaTeste + notaProva) / 2
                        print('A média final da matéria %s é %.2f', materia % media)
            else:
                print('Adicione primeiro a matéria!')
                cadastrarNota()


def exibeMenu():
    while True:
        print('-' * 30, '|MENU PRINCIPAL|', '-' * 30)
        print('Bem-vindo(a) ao sistema escolar "Arte de Educar".')
        print('Opção 1 - Cadastrar aluno.')
        print('Opção 2 - Cadastrar nota.')
        print('Opção 3 - Consultar aluno.')
        print('Opção 4 - Cadastrar professor.')
        print('Opção 6 - Sair.')
        print('-' * 79)
        try:
            opcao = int(input('Digite sua opção desejada: '))
            print()

            if opcao == 1:
                cadastrarAluno(contadoraMatricula)
            elif opcao == 2:
                cadastrarNota()
            elif opcao == 3:
                consultarAluno()

        except ValueError:
            print('Dígito incorreto!\nDigite somente as opções presentes.')
            print()
            continue


exibeMenu()
