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

def regras():
    print("PACIÊNCIA ACORDEÃO\n==================")
    print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n")
    print('Existem apenas dois movimentos possíveis:\n') 
    print("1. Empilhar uma carta sobre a carta imediatamente anterior;") 
    print("2. Empilhar uma carta sobre a terceira carta anterior.\n") 
    print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n") 
    print("1. As duas cartas possuem o mesmo valor ")
    print('2. As duas cartas possuem o mesmo naipe.\n') 
    print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n') 
    print('Aperte [Enter] para iniciar o jogo...')
    input()

def play():
    class colors:
        AZUL = '\033[94m'
        VERDE = '\033[92m'
        AMARELO = '\033[93m'
        VERMELHO = '\033[91m'
        ENDC = '\033[0m'
    
    baralho = cria_baralho()
    random.shuffle(baralho)
    regras()
    
    while possui_movimentos_possiveis(baralho):
        empilhou = False
        print('O estado atual do baralho é:')
        for posicao, carta in enumerate(baralho, 1):
            if extrai_naipe(carta) == '♠':
                print(f'{posicao}. {colors.AZUL}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == '♥':
                print(f'{posicao}. {colors.VERMELHO}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == '♦':
                print(f'{posicao}. {colors.VERDE}{ascii(carta)}{colors.ENDC}')
            if extrai_naipe(carta) == '♣':
                print(f'{posicao}. {colors.AMARELO}{ascii(carta)}{colors.ENDC}')
        
        while empilhou == False:
            carta_escolhida = int(input(f'Escolha uma carta (digite um número entre 1 e {len(baralho)}):'))
            if carta_escolhida > 0 and carta_escolhida <= len(baralho):
                #Checar os movimentos possíveis
                if lista_movimentos_possiveis(baralho, carta_escolhida-1) == []:
                    print(f'A carta {baralho[carta_escolhida-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(baralho)}:')
                elif lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1, 3]:
                    print(f'Sobre qual carta você quer empilhar o {baralho[carta_escolhida-1]}?')
                    print(f'1. {baralho[carta_escolhida-2]}')
                    print(f'2. {baralho[carta_escolhida-4]}\n')
                    escolha = int(input('Digite o número de sua escolha (1-2):'))
                    if escolha > 0 and escolha < 3:
                        if escolha == 1 :
                            empilha(baralho, (carta_escolhida-1), (carta_escolhida-2))
                            empilhou = True
                        if escolha == 2:
                            empilha(baralho, (carta_escolhida-1), (carta_escolhida-4))
                            empilhou = True
                    else:
                        print("Escolha inválida")
                elif lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1]:
                    empilha(baralho, carta_escolhida-1, carta_escolhida-2)
                    empilhou = True
                elif lista_movimentos_possiveis(baralho, carta_escolhida-1) == [3]:
                    empilha(baralho, carta_escolhida-1, carta_escolhida-4)
                    empilhou = True
            else:
                print("Essa carta não é valida")

    if len(baralho) == 1:
        print('Parabéns! Você ganhou!')
    else:
        print('Você perdeu :(')