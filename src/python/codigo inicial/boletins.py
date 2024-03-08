import random

def criar_boletin_pseudoaleatorio(tamanho: int) -> list:
    notas = []
    while tamanho > 0:
        notas.append(random.randint(0,10))
        tamanho -= 1
    return notas

def criar_boletin_aleatorio() -> list:
    notas = []
    tamanho = random.randint(1,10)
    while tamanho > 0:
        notas.append(random.randint(0,10))
        tamanho -= 1
    return notas

def media(notas: list) -> float:
    subtotal = 0
    for nota in notas:
        subtotal += nota
    return subtotal/len(notas)
