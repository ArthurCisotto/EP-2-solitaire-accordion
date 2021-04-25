import random
import funcoes


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

#Randomiza a ordem do baralho#
baralho = funcoes.cria_baralho()
random.shuffle(baralho)

#Estado do baralho
while funcoes.possui_movimentos_possiveis(baralho):
    print('O estado atual do baralho é:')
    for e in range(len(baralho)):
        print(f'{e+1}. {baralho[e]}')
    carta_escolhida = int(input(f'Escolha uma carta (digite um número entre 1 e {len(baralho)}):'))

        #Checar os movimentos possíveis
    if funcoes.lista_movimentos_possiveis(baralho, carta_escolhida-1) == []:
        print(f'A carta {baralho[carta_escolhida-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(baralho)}:')
    if funcoes.lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1, 3]:
        print(f'Sobre qual carta você quer empilhar o {baralho[carta_escolhida-1]}?')
        print(f'1. {baralho[carta_escolhida-2]}')
        print(f'2. {baralho[carta_escolhida-4]}\n')
        escolha = int(input('Digite o número de sua escolha (1-2):'))
        if escolha == 1 :
            funcoes.empilha(baralho, carta_escolhida-1, carta_escolhida-2)
        if escolha == 2:
            funcoes.empilha(baralho, carta_escolhida-1, carta_escolhida-4)
    if funcoes.lista_movimentos_possiveis(baralho, carta_escolhida-1) == [1]:
        funcoes.empilha(baralho, carta_escolhida-1, carta_escolhida-2)
    if funcoes.lista_movimentos_possiveis(baralho, carta_escolhida-1) == [3]:
        funcoes.empilha(baralho, carta_escolhida-1, carta_escolhida-4)

