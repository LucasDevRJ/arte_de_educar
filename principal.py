from aluno import exibeMenuAluno
from professor import exibeMenuProfessor


def finalizarPrograma():
    print('Programa finalizado.')


def exibeMenu():
    global matricula, matriculaAluno, matriculaProfessor
    while True:
        print('-' * 30, '|MENU PRINCIPAL|', '-' * 30)
        print('Bem-vindo(a) ao sistema escolar "Arte de Educar".')
        print('Opção 1 - Menu dos Alunos.')
        print('Opção 2 - Menu dos Professores.')
        print('Opção 3 - Finalizar Programa.')

        print('-' * 79)
        try:
            opcao = int(input('Digite sua opção desejada: '))
            print()

            if opcao == 1:
                exibeMenuAluno()
            elif opcao == 2:
                exibeMenuProfessor()
            elif opcao == 3:
                finalizarPrograma()
                break
            else:
                print('Opção inválida.')
                continue

        except ValueError:
            print('Dígito incorreto!\nDigite somente as opções presentes.')
            print()
            continue


exibeMenu()
