import Aluno

todos_boletins = []

def criar_boletim():
    boletim = []
    while True:
        acao = input("Adicionar uma nota (add) ou encerrar o boletin (end)?\nR: ")
        if acao == "add":
            try:
                nota = int(input("Digite a nota: "))
                numeros = list(range(11))
                if nota in numeros:
                    boletim.append(nota)
                    print("Adicionado")
                else:
                    print("isso não é um numero compreendido, ou sai do limite de notas estabelecidos")
            except:
                print("Isso não é um numero")
        else: 
            while True:
                aluno_atual: Aluno
                cpf = input("Digite o CPF do aluno no qual deseja atribuir o boletim ou 'sair' para voltar ao menu: ")
                if cpf == "sair":
                    break
                for aluno in Aluno.alunos:
                    if cpf == aluno.cpf:
                        aluno_atual = aluno
                if aluno_atual != None:
                    mostrar_aluno(aluno)
                    validacao = input("Este é o aluno desejado? S/N\n")
                    if validacao == "S":
                        while True:
                            data = input("Digite a data de hoje(dd/mm/aaaa): ")
                            print(data_format(data))
                            if validate_data(data_format(data)):
                                boletim.append(data)
                                boletim.append(aluno.cpf)
                                aluno.adicionar_boletin(boletim)
                                todos_boletins.append(boletim)
                                print("Boletim associado com sucesso!!!")
                                break
                            else:
                                print("Data invalida")
                    break
                else:
                    ("CPF não encontrado")
            break

def ver_boletim_data():
    data = input("Digite a data desejada: ")
    if validate_data(data_format(data)):
        for boletim in todos_boletins:
            if boletim[len(boletim) - 2] == data:
                for aluno in Aluno.alunos:
                    if boletim[len(boletim) - 1] == aluno.cpf:
                        print("---------------------------")
                        mostrar_aluno(aluno)
                mostrar_boletim(boletim)
    else: 
        print("Data invalida") 
   
def ver_boletim_aluno():
    escolha = input("Deseja procurar por cpf(1) ou por nome(2): ")
    match escolha:
        case "1":
            cpf = input("\nDigite o cpf do aluno: ")
            for aluno in Aluno.alunos:
                if cpf == aluno.cpf:
                    mostrar_aluno(aluno)
                    try:
                        aluno.boletins[0]
                        print("\nBoletins\n")
                        for boletim in aluno.boletins:
                            print("---------------------------")
                            mostrar_boletim(boletim)
                    except:
                        print("Este aluno não possui boletins associados")
                    break
        case "2":
            nome = input("\nDigite o nome do aluno: ")
            for aluno in Aluno.alunos:
                if nome == aluno.nome:
                    mostrar_aluno(aluno)
                    try:
                        aluno.boletins[0]
                        print("\nBoletins\n")
                        for boletim in aluno.boletins:
                            print("---------------------------")
                            mostrar_boletim(boletim)
                    except:
                        print("Este aluno não possui boletins associados")
                    break
        case _:
            print("Não esta na lista de opções")

def media(notas: list) -> float:
    subtotal = 0
    for index, nota in enumerate(notas):
        if final_boletim(notas, index):
            break
        subtotal += nota
    return subtotal/(len(notas) - 2)

def data_format(data: str) -> list:
    if len(data) != 10:
        return []
    return [int(data[:2]),int(data[3:5]),int(data[6:])]

def validate_data(data: list) -> bool:
    if data == []:
        return False

    if data[0] not in range(1, 31):
        return False
    
    if data[1] not in range(1, 12):
        return False
    else:
        match data[1]:
            case "2":
                if data[2] % 4 == 0:
                    if data[0] not in range(1, 29):
                        return False
                else:
                    if data[0] not in range(1, 28):
                        return False
            case "4","6","9","11":
                if data[0] not in range(1, 30):
                    return False
                
    if data[2] not in range(1900, 2025):
        return False
    
    return True

def mostrar_aluno(aluno: Aluno):
    print("\nDados do aluno")
    print("Nome: " + aluno.nome)
    print("Idade: " + str(aluno.idade))
    print("CPF: " + Aluno.format_CPF(aluno.cpf))

def mostrar_boletim(boletim: list):
    print("Boletim")
    for index, nota in enumerate(boletim):
        if final_boletim(boletim, index):
            break
        print("Nota " + str(index + 1) + " = " + str(nota))
    media_formatada = str("{:.2f}".format(media(boletim)))
    print("Media final = " + media_formatada)
    print("Data: " + boletim[len(boletim) - 2])
    print("---------------------------")

def final_boletim(boletim: list, index: int):
    try:
        boletim[index + 2]
        return False
    except:
        return True