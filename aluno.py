matriculaAluno = 100
alunos = []


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
                        print()
                elif opcao == 2:
                    matricula = int(input('Digite a matrícula do aluno: '))
                    for aluno in alunos:
                        if aluno['Matrícula'] == matricula:
                            for key, value in aluno.items():
                                print('{}:{}'.format(key, value))
                        else:
                            print('Matrícula inválida!')
                elif opcao == 3:
                    exibeMenuAluno()
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

                            break

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

                break

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre alunos para poder cadastrar notas.')


def excluirAluno():
    if len(alunos) > 0:
        while True:
            print('-' * 30, '|EXCLUIR ALUNO|', '-' * 30)
            print('Opção 1 - Excluir todos os alunos.')
            print('Opção 2 - Excluir um aluno.')
            print('Opção 3 - Voltar.')

            try:
                opcao = int(input('Digite sua opção desejada: '))
                if opcao == 1:
                    for aluno in alunos:
                        alunos.clear()
                        print('Alunos excluídos com sucesso!')
                elif opcao == 2:
                    matricula = int(input('Digite a matrícula do professor: '))
                    for aluno in alunos:
                        if aluno['Matrícula'] == matricula:
                            alunos.remove(matricula)
                            print('Aluno excluído com sucesso!')
                        else:
                            print('Matrícula inválida!')
                elif opcao == 3:
                    exibeMenuAluno()
                else:
                    print('Dígito inválido!\nDigite alguma das opções.')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre alunos para poder excluí-los.')


def atualizarAluno(matricula):
    print('-' * 30, '|ATUALIZAR ALUNO|', '-' * 30)
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

    alunos.pop()
    alunos.append(aluno.copy())

    print('Informações atualizadas com sucesso!')
    print('-' * 79)


def alterarAluno():
    if len(alunos) > 0:
        while True:
            print('-' * 30, '|EXCLUIR ALUNO|', '-' * 30)
            print('Opção 1 - Alterar informações do aluno.')
            print('Opção 2 - Voltar.')

            try:
                opcao = int(input('Digite sua opção desejada: '))
                if opcao == 1:
                    matricula = int(input('Digite a matrícula do aluno: '))
                    for aluno in alunos:
                        if aluno['Matrícula'] == matricula:
                            atualizarAluno(matricula)
                            print('Informações atualizadas com sucesso!')
                            break
                        else:
                            print('Matrícula inválida!')
                elif opcao == 2:
                    exibeMenuAluno()
                else:
                    print('Dígito inválido!\nDigite alguma das opções.')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre alunos para poder excluí-los.')


def exibeMenuAluno():
    global matriculaAluno
    while True:
        print('-' * 30, '|MENU DO ALUNO|', '-' * 30)
        print('Opção 1 - Cadastrar aluno.')
        print('Opção 2 - Consultar aluno.')
        print('Opção 3 - Excluir aluno.')
        print('Opção 4 - Alterar aluno.')
        print('Opção 5 - Cadastrar nota.')
        print('Opção 6 - Voltar.')

        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                matriculaAluno = matriculaAluno + 1
                cadastrarAluno(matriculaAluno)
            elif opcao == 2:
                consultarAluno()
            elif opcao == 3:
                excluirAluno()
            elif opcao == 4:
                alterarAluno()
            elif opcao == 5:
                cadastrarNota()
            elif opcao == 6:
                from principal import exibeMenu
                exibeMenu()
            else:
                print('Opção inválida!!')
                continue
        except ValueError:
            print('Dígito inválido!\nDigite somente as opções presentes.')
