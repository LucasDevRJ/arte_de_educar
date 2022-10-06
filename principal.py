contadoraMatricula = 100
contadoraMatriculaProfessor = 800
alunos = []
professores = []
contadoraMatricula += 1
contadoraMatriculaProfessor += 1


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

    print('Aluno cadastrado com sucesso!')
    print('Matrícula do aluno: {}'.format(matricula))

    print('-' * 79)


def consultarAluno():
    if len(alunos) > 0:
        while True:
            print('-' * 30, '|CONSULTAR ALUNO|', '-' * 30)
            print('Opção 1 - Consultar todos os alunos.')
            print('Opção 2 - Consultar um aluno.')
            print('Opção 3 - Voltar.')

            try:
                opcao = int(input('Digite sua opção desejada: '))
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
                elif opcao == 3:
                    exibeMenu()
                else:
                    print('Dígito inválido!\nDigite alguma das opções.')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre alunos para poder consulta-los.')


def cadastrarNota():
    if len(alunos) > 0:
        global materia
        while True:
            print('-' * 30, '|CADASTRAR NOTA|', '-' * 30)
            try:
                matricula = int(input('Digite a matrícula do aluno: '))
                for aluno in alunos:
                    if aluno['Matrícula'] == matricula:
                        print('Matrícula encontrada com sucesso!')

                        if aluno['Ensino'] == 'ENSINO FUNDAMENTAL':
                            print('Opção 1 - Português.')
                            print('Opção 2 - Ciências.')
                            print('Opção 3 - História.')

                            opcao = int(input('Digite a opção desejada: '))

                            if opcao == 1:
                                materia = 'Português'
                            elif opcao == 2:
                                materia = 'Ciências'
                            elif opcao == 3:
                                materia = 'História'

                            notaTeste = float(input('Digite a nota do teste: '))
                            notaProva = float(input('Digite a nota da prova: '))
                            media = (notaTeste + notaProva) / 2
                            print()

                            if media >= 6.0:
                                aprovado = True
                            else:
                                aprovado = False

                            for key, value in aluno.items():
                                print('{}:{}'.format(key, value))

                            print()
                            print('Matéria: {}'.format(materia))
                            print('Nota do Teste: %.1f' % notaTeste)
                            print('Nota da Prova: %.1f' % notaProva)
                            print('Média: %.1f' % media)
                            if aprovado:
                                print('Situação: Aprovado')
                            else:
                                print('Situação: Reprovado')

                    elif aluno['Ensino'] == 'ENSINO MÉDIO':
                        print('Opção 1 - Física.')
                        print('Opção 2 - Química.')
                        print('Opção 3 - Filosofia.')

                        opcao = int(input('Digite a opção desejada: '))

                        if opcao == 1:
                            materia = 'Física'
                        elif opcao == 2:
                            materia = 'Química'
                        elif opcao == 3:
                            materia = 'Filosofia'

                        notaTeste = float(input('Digite a nota do teste: '))
                        notaProva = float(input('Digite a nota da prova: '))
                        media = (notaTeste + notaProva) / 2
                        print()

                        if media >= 6.0:
                            aprovado = True
                        else:
                            aprovado = False

                        for key, value in aluno.items():
                            print('{}:{}'.format(key, value))

                        print()
                        print('Matéria: {}'.format(materia))
                        print('Nota do Teste: %.1f' % notaTeste)
                        print('Nota da Prova: %.1f' % notaProva)
                        print('Média: %.1f' % media)
                        if aprovado:
                            print('Situação: Aprovado')
                        else:
                            print('Situação: Reprovado')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre alunos para poder cadastrar notas.')


def cadastrarProfessor(matricula):
    global materia, tipoEnsinoProfessor
    tipoEnsinoProfessor = ''
    materia = ''

    print('-' * 30, '|CADASTRAR PROFESSOR|', '-' * 30)
    nomeProfessor = str(input('Digite o nome do professor: '))

    while not nomeProfessor.isalpha():
        print('Dígito incorreto!\nDigite somente letras e acentos.')
        nomeProfessor = str(input('Digite o nome: '))

    sobrenomeProfessor = str(input('Digite o sobrenome do professor: '))

    while not sobrenomeProfessor.isalpha():
        print('Dígito incorreto!\nDigite somente letras e acentos.')
        sobrenomeProfessor = str(input('Digite o sobrenome: '))

    while True:
        try:
            tipoEnsinoProfessor = int(input('Opção 1 - Ensino Fundamental\nOpção 2 - Ensino Médio\nDigite sua opção '
                                            'desejada: '))

            if tipoEnsinoProfessor == 1:
                tipoEnsinoProfessor = 'ensino fundamental'
                print('Opção 1 - Português.')
                print('Opção 2 - Ciências.')
                print('Opção 3 - História.')

                materia = int(input('Digite a matéria desejada: '))

                if materia == 1:
                    materia = 'Português'
                elif materia == 2:
                    materia = 'Ciências'
                elif materia == 3:
                    materia = 'História'

                break
            elif tipoEnsinoProfessor == 2:
                tipoEnsinoProfessor = 'ensino médio'
                print('Opção 1 - Física.')
                print('Opção 2 - Química.')
                print('Opção 3 - Filosofia.')

                materia = int(input('Digite a matéria desejada: '))

                if materia == 1:
                    materia = 'Física'
                elif materia == 2:
                    materia = 'Química'
                elif materia == 3:
                    materia = 'Filosofia'

                break
        except ValueError:
            print('Dígite somente número.')
            continue

    nomeProfessor = nomeProfessor.upper()
    sobrenomeProfessor = sobrenomeProfessor.upper()
    tipoEnsinoProfessor = tipoEnsinoProfessor.upper()

    professor = {
        'Matrícula': matricula,
        'Nome': nomeProfessor,
        'Sobrenome': sobrenomeProfessor,
        'Ensino': tipoEnsinoProfessor,
        'Matéria': materia
    }

    professores.append(professor.copy())

    print('Professor cadastrado com sucesso!')
    print('A matrícula do professor: {}'.format(matricula))


def consultarProfessor():
    if len(professores) > 0:
        while True:
            print('-' * 30, '|CONSULTAR PROFESSOR|', '-' * 30)
            print('Opção 1 - Consultar todos os professores.')
            print('Opção 2 - Consultar um professor.')
            print('Opção 3 - Voltar.')

            try:
                opcao = int(input('Digite sua opção desejada: '))
                if opcao == 1:
                    for professor in professores:
                        for key, value in professor.items():
                            print('{}:{}'.format(key, value))
                elif opcao == 2:
                    matricula = int(input('Digite a matrícula do professor: '))
                    for professor in professores:
                        if professor['Matrícula'] == matricula:
                            for key, value in professor.items():
                                print('{}:{}'.format(key, value))
                        else:
                            print('Matrícula inválida!')
                elif opcao == 3:
                    exibeMenu()
                else:
                    print('Dígito inválido!\nDigite alguma das opções.')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre professores para poder consulta-los.')


def finalizarPrograma():
    print('Programa finalizado.')


def exibeMenu():
    while True:
        print('-' * 30, '|MENU PRINCIPAL|', '-' * 30)
        print('Bem-vindo(a) ao sistema escolar "Arte de Educar".')
        print('Opção 1 - Cadastrar aluno.')
        print('Opção 2 - Cadastrar nota.')
        print('Opção 3 - Consultar aluno.')
        print('Opção 4 - Cadastrar professor.')
        print('Opção 5 - Consultar professor.')
        print('Opção 6 - Finalizar programa.')
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
            elif opcao == 4:
                cadastrarProfessor(contadoraMatriculaProfessor)
            elif opcao == 5:
                consultarProfessor()
            elif opcao == 6:
                finalizarPrograma()
            else:
                print('Opção inválida.')
                continue

        except ValueError:
            print('Dígito incorreto!\nDigite somente as opções presentes.')
            print()
            continue


exibeMenu()
