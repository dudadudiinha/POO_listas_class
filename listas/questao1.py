#1
import random

class Bingo:
    def __init__(self, numBolas):
        self.__numBolas = numBolas
        self.__bolas = []
    def sortear(self):
        if len(self.__bolas) == self.__numBolas:
            return -1
        while True:
            bola = random.randint(1, self.__numBolas)
            if bola not in self.__bolas:
                self.__bolas.append(bola)
                return bola
    def sorteados(self):
        return self.__bolas

class BingoUI:
    __bingo = None
    @classmethod
    def menu(cls):
        return int(input("1 - Iniciar jogo, 2 - Sortear, 3 - Sorteados, 4 - Fim\nInforme uma opção: "))
    @classmethod
    def main(cls):
        op = 0
        while op != 4:
            op = BingoUI.menu()
            match op:
                case 1: cls.IniciarJogo()
                case 2: cls.Sortear()
                case 3: cls.Sorteados()
    @classmethod
    def IniciarJogo(cls):
        n_bolas = int(input("Digite o número de bolas que o jogo terá: "))
        cls.__bingo = Bingo(n_bolas)
        print(f"O jogo está sendo iniciado com {n_bolas} bolas")
    @classmethod
    def Sortear(cls):
        if cls.__bingo == None:
            print("Inicie o jogo primeiro")
        else:
            bola = cls.__bingo.sortear()
            if bola == -1:
                print("Todas as bolas já foram sorteadas")
            else:
                print(f"O número sorteado foi {bola}")
    @classmethod
    def Sorteados(cls):
        if cls.__bingo == None:
            print("Inicie o jogo primeiro")
        else:
            print(f"As bolas sorteadas foram: ", end="")
            for bola in cls.__bingo.sorteados():
                print(bola, end=" ")
            print()

BingoUI.main()