
def main():
    print('Calculadora')
    numero = input('\nDigite o primeiro numero para fazer sua operação: ')

    try:
        numero = int(numero)
    except:
        print('Numero invalido')
        return

    print('\nQual operação você quer fazer : ')
    print('soma "+": 1')
    print('subtração "-": 2')
    print('multiplicação "*": 3')
    print('divisão "/": 4')
    operacao = input('\nEscolha: ')
    try:
        if int(operacao) not in range(1, 5):
            print('Opção invalida')
            return
    except:
        print('Opção invalida')
        return

    numero2 = input('\nDigite o segundo numero da operação: ')

    try:
        numero2 = int(numero2)
    except:
        print('Numero invalido')
        return

    match operacao:
        case "1":
            result = numero + numero2
        case "2":
            result = numero - numero2
        case "3":
            result = numero * numero2
        case "4":
            if numero2 == 0:
                print('Impossivel dividir por 0')
                return
            else:
                result = numero / numero2
        case _:
            print('A operação descrita não é uma opção valida')

    print("\nO resultado é: " + str(result))
main()



