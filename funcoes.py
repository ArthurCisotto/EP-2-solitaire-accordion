import random

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
            continue
        try:
            if extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-e]) or extrai_valor(baralho[i]) == extrai_valor(baralho[i-e]):
                movimentos_possiveis.append(e)
        except IndexError:
            pass
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

def ascii(carta):
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)
    carta_final = '\n'
    carta_final += '┌─────────┐\n'
    if valor == '10':
        carta_final += f'│{valor}       │\n'
    else:
        carta_final += f'│{valor}        │\n'
    carta_final += '│         │\n'
    carta_final += '│         │\n'
    carta_final += f'│    {naipe}    │\n'
    carta_final += '│         │\n'
    carta_final += '│         │\n'
    if valor == '10':
        carta_final += f'│       {valor}│\n'
    else:
        carta_final += f'│        {valor}│\n'
    carta_final += '└─────────┘'
    return carta_final

def play():
    class colors:
        AZUL = '\033[94m'
        VERDE = '\033[92m'
        AMARELO = '\033[93m'
        VERMELHO = '\033[91m'
        ENDC = '\033[0m'
    
    baralho = cria_baralho()
    random.shuffle(baralho)

    while possui_movimentos_possiveis(baralho):
        print('O estado atual do baralho é:')
        for posicao, carta in enumerate(baralho, 1):
            if extrai_naipe(carta) == ':spades:':
                print(f'{posicao}. {colors.AZUL}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == ':hearts:':
                print(f'{posicao}. {colors.VERMELHO}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == ':diamonds:':
                print(f'{posicao}. {colors.VERDE}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == ':clubs:':
                print(f'{posicao}. {colors.AMARELO}{ascii(carta)}{colors.ENDC}')
        carta_escolhida = int(input(f'Escolha uma carta (digite um número entre 1 e {len(baralho)}):'))

        #Checar os movimentos possíveis
        if lista_movimentos_possiveis(baralho, carta_escolhida-1) == []:
            print(f'A carta {baralho[carta_escolhida-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(baralho)}:')
        if lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1, 3]:
            print(f'Sobre qual carta você quer empilhar o {baralho[carta_escolhida-1]}?')
            print(f'1. {baralho[carta_escolhida-2]}')
            print(f'2. {baralho[carta_escolhida-4]}\n')
            escolha = int(input('Digite o número de sua escolha (1-2):'))
            if escolha == 1 :
                empilha(baralho, carta_escolhida-1, carta_escolhida-2)
            if escolha == 2:
                empilha(baralho, carta_escolhida-1, carta_escolhida-4)
        if lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1]:
            empilha(baralho, carta_escolhida-1, carta_escolhida-2)
        if lista_movimentos_possiveis(baralho, carta_escolhida-1) == [3]:
            empilha(baralho, carta_escolhida-1, carta_escolhida-4)

    if len(baralho) == 1:
        print('Parabéns! Você ganhou!')
    else:
        print('Você perdeu :(')