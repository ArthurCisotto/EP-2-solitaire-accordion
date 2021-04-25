def extrai_naipe(carta):
    if len(carta)>2:
        return carta[2]
    else:
        return carta[1]

def extrai_valor(carta):
    if len(carta)>2:
        return carta[:2]
    else:
        return carta[0]

def lista_movimentos_possiveis(baralho, i):
    posicoes_validas = [1,3]
    movimentos_possiveis = []
    for e in posicoes_validas:
        if i<e:
            break
        if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-e]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-e]):
            movimentos_possiveis.append(e)
    return movimentos_possiveis

def possui_movimentos_possiveis(baralho):
    check = 0
    for i in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, i) != []:
            check += 1
    if check == 0:
        return False
    else:
        return True