import random
import funcoes

def main():
    funcoes.play()
    while input("Jogar novamente (S/N) ").upper() == "S":
        funcoes.play()

if __name__ == "__main__":
    main()