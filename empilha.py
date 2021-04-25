def empilha(baralho, o, d):
    baralho[d]=baralho[o]
    del(baralho[o])
    return baralho