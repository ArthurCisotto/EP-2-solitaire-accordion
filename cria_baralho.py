def cria_baralho():
    lista_base = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista_final = []
    for e in range(len(lista_base)):
        lista_final.append(lista_base[e]+'♠')
        lista_final.append(lista_base[e]+'♥')
        lista_final.append(lista_base[e]+'♦')
        lista_final.append(lista_base[e]+'♣')
    return lista_final

