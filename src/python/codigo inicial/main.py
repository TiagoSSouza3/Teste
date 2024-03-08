import boletins
import historico

def mensagem_principal() -> str:
    print("\nGerar Boletin Virtual \n")
    print("Para gerar boletins aleatorios digite 1 \n")
    print("Para gerar boletins de forma manual digite 2 \n")
    print("Para ver o historico de boletins digite 3 \n")
    print("Sair digite 4\n")
    return str(input("opção: "))

def mensagem_boletin_aleatorio() -> str:
    return str(input("Escolher tamnho do boletin? S/N \nResposta: "))

def mensagem_digitar_tamanho() -> int:
    return int(input("Digite o numero de notas do boletin: \nTamanho: "))

def mensagem_boletin_manual():
    boletin = []
    while True:
        acao = input("Adicionar uman nota (add) ou encerrar o boletin (end)?\nR: ")
        if acao == "add":
            try:
                nota = int(input("Digite a nota: "))
                numeros = list(range(11))
                if nota in numeros:
                    boletin.append(nota)
                    print("Adicionado")
                else:
                    print("isso não é um numero compreendido, ou sai do limite de notas estabelecidos")
            except:
                print("Isso não é um numero")
        else: 
            print("Boletin encerrado")
            break
    boletins.mostrar_notas(boletin)

def mostrar_historico():
    historico = historico.historico_boletins
    for index, boletin in enumerate(historico):
        print("---------------------------")
        print("Boletin " + str(index + 1))
        for index, nota in enumerate(boletin):
            if index == len(boletin) - 1:
                print("Media final = " + str(nota))
            else:
                print("Nota " + str(index + 1) + " = " + str(nota))
        print("---------------------------")
            
def mensagem_criar_boletin():
    match mensagem_principal():
        case "1":
            match mensagem_boletin_aleatorio():
                case "S":
                    tamanho = mensagem_digitar_tamanho()
                    boletins.mostrar_notas(list(boletins.criar_boletin_pseudoaleatorio(tamanho)))
                case "N":
                    boletin_aleatorio = boletins.criar_boletin_aleatorio()
                    boletins.mostrar_notas(list(boletin_aleatorio))
        case "2":
            mensagem_boletin_manual()
        case "3":
            mostrar_historico()
        case "4":
            main()
    input("Aperte enter para voltar")
    mensagem_criar_boletin()

def main():
   print("SUAP")
   escolha = int(input("Pagina de alunos: 1\nPagina de boletins: 2\nEncerrar programa: 3\nEscolha: "))
   match escolha:
        case 1:
           pass
        case 2:
           mensagem_criar_boletin()
        case _: 
           return

main()