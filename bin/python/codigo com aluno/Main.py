import Aluno
import Boletim

def tela_alunos():
    while True:
        print("\nAlunos\nCadastrar aluno: 1\nVer lista de alunos: 2\nRemover aluno: 3\nVoltar: 4")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                nome = input("Digite o nome do aluno: ")
                idade = input("Digite a idade do aluno: ")
                cpf = input("Digite o cpf do aluno: ")
                _aluno = Aluno.Aluno(nome, idade, cpf)
            case "2":
                Aluno.lista_de_alunos()
            case "3":
                cpf = input("Digite o CPF do aluno que quer remover: ")
                Aluno.remover_aluno(cpf)
            case _:
                break
        
def tela_boletins():
    while True:
        print("\nBoletins\nCriar boletin: 1\nVer boletim por aluno: 2\nVer boletim por data: 3\nVoltar:4")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                Boletim.criar_boletim()
            case "2":
                Boletim.ver_boletim_aluno()
            case "3":
                Boletim.ver_boletim_data()
            case _:
                break

while True:
    print("\nOrganizador de notas\nPara gerenciar alunos digite: 1\nPara gerenciar boletins digite: 2\nEncerrar programa: 3")
    escolha = input("Escolha: ")
    match escolha:
        case "1":
            tela_alunos()
        case "2":
            tela_boletins()
        case _:
            break