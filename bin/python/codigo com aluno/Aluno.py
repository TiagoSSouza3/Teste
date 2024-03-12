alunos = []

def remover_aluno(cpf: str):
    aluno_atual: Aluno
    for aluno in alunos:
        if cpf == aluno.cpf:
            aluno_atual = aluno
            mostrar_aluno(aluno)
            break
    if aluno_atual != None:
        validacao = input("\nTem certeza que deseja remover este aluno? S/N")
        if validacao == "S":
            alunos.remove(aluno_atual)
            print("Aluno removido!!")
        else:
            print("Aluno não removido")
    else:
        print("Aluno não encontrado")

def lista_de_alunos():
    while True:
        print("\nEncontrar Aluno\nBuscar aluno por cpf: 1\nBuscar aluno por nome: 2\nVer todos os alunos: 3\nVoltar: 4\n")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                cpf = input("\nDigite o cpf do aluno: ")
                for aluno in alunos:
                    if cpf == aluno.cpf:
                        mostrar_aluno(aluno)
                        break
            case "2":
                nome = input("\nDigite o nome completo do aluno: ")
                for aluno in alunos:
                    if nome == aluno.nome:
                        mostrar_aluno(aluno)
                        break
            case "3":
                for aluno in alunos:
                    mostrar_aluno(aluno)
            case _:
                break

def format_CPF(cpf: str) -> str:
    return cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

class Aluno():
    def __init__(self, nome: str, idade: int, cpf: str):

        try:
            idade = int(idade)
            if idade not in range(60):
                print("Idade invalida!!!")
                return
        except:
            print("Idade invalida!!!")
            return
        
        try:
            int(cpf)
            if len(cpf) != 11:
                print("\nCPF invalido!!!")
                return
        except:
            print("\nCPF invalido!!!")
            return
    
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.boletins = []
        alunos.append(self)
        print("\nAluno Cadastrado!")

    def adicionar_boletin(self, boletin: list):
        self.boletins.append(boletin)

def mostrar_aluno(aluno: Aluno):
    print("\nDados do aluno")
    print("Nome: " + aluno.nome)
    print("Idade: " + str(aluno.idade))
    print("CPF: " + format_CPF(aluno.cpf))