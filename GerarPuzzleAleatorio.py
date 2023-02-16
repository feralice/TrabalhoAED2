import random

def criaListaAleatoria(estadoInicial):
    puzzle = estadoInicial.copy()
    random.shuffle(puzzle)

    if(verificaSolucionavel(puzzle)):
        return puzzle
    else:
        return criaListaAleatoria(estadoInicial)


def verificaSolucionavel(puzzle):
    numInversoes = 0
    for i in range(len(puzzle)):
        if(puzzle[i]==0):
            continue
        for j in range(i+1, len(puzzle)) :
            if(puzzle[j]==0):
                continue
            if puzzle[i] > puzzle[j]:
                numInversoes+=1

    if(numInversoes)%2==1:
        return False
    else: 
        return True

estadoFinal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(criaListaAleatoria(estadoFinal))

