matriculaProfessor = 800

professores = []


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
    materia = materia.upper()

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
                        print()
                elif opcao == 2:
                    matricula = int(input('Digite a matrícula do professor: '))
                    for professor in professores:
                        if professor['Matrícula'] == matricula:
                            for key, value in professor.items():
                                print('{}:{}'.format(key, value))
                        else:
                            print('Matrícula inválida!')
                elif opcao == 3:
                    exibeMenuProfessor()
                else:
                    print('Dígito inválido!\nDigite alguma das opções.')

            except ValueError:
                print('Dígito inválido!\nDigite somente números.')
    else:
        print('Primeiro cadastre professores para poder consulta-los.')


def exibeMenuProfessor():
    global matriculaProfessor
    while True:
        print('-' * 30, '|MENU DO PROFESSOR|', '-' * 30)
        print('Opção 1 - Cadastrar professor.')
        print('Opção 2 - Consultar professor.')
        print('Opção 3 - Voltar.')

        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1:
                matriculaProfessor = matriculaProfessor + 1
                cadastrarProfessor(matriculaProfessor)
            elif opcao == 2:
                consultarProfessor()
            elif opcao == 3:
                from principal import exibeMenu
                exibeMenu()
            else:
                print('Opção inválida!!')
        except ValueError:
            print('Dígito inválido!\nDigite somente as opções presentes.')