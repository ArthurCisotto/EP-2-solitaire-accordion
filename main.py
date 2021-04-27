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


def main():
    funcoes.play()
    while input("Jogar novamente (S/N) ").upper() == "S":
        funcoes.play()

if __name__ == "__main__":
    main()