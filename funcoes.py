def cria_baralho():
    lista_base = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista_final = []
    for e in range(len(lista_base)):
        lista_final.append(lista_base[e]+'♠')
        lista_final.append(lista_base[e]+'♥')
        lista_final.append(lista_base[e]+'♦')
        lista_final.append(lista_base[e]+'♣')
    return lista_final

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

def empilha(baralho, o, d):
    baralho[d]=baralho[o]
    del(baralho[o])
    return baralho