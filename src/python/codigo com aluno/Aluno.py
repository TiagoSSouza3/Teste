alunos = []

def lista_de_alunos():
    while True:
        print("\nEncontrar Aluno\nBuscar aluno por cpf: 1\nBuscar aluno por nome: 2\nVer todos os alunos: 3\nVoltar: 4\n")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                cpf = input("\nDigite o cpf do aluno: ")
                for aluno in alunos:
                    if cpf == aluno.cpf:
                        print("\nDados do aluno")
                        print("Nome: " + aluno.nome)
                        print("Idade: " + str(aluno.idade))
                        cpf = format_CPF(cpf)
                        print("CPF: " + cpf)
                        break
            case "2":
                pass
            case "3":
                pass
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

    def get_cpf(self) -> str:
        return self.cpf
    
    def get_nome(self) -> str:
        return self.nome
    
    def get_idade(self) -> int:
        return self.idade

    def adicionar_boletin(self, boletin: list):
        self.boletins.append(boletin)
       