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

#2
class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def set_nome(self, nome2):
        self.__nome = nome2
    def get_nome(self):
        return self.__nome
    def set_email(self, email2):
        self.__email = email2
    def set_fone(self, fone2):
        self.__fone = fone2
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o phone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        nome = input("Informe o nome do contato que deseja atualizar: ")
        for c in cls.__contatos:
            if c.get_nome() == nome:
                nome2 = input("Informe o nome: ")
                email2 = input("Informe o email: ")
                fone2 = input("Informe o phone: ")
                c.set_nome(nome2)
                c.set_email(email2)
                c.set_fone(fone2)
                print("Contato atualizado")

    @classmethod
    def excluir(cls):
        nome = input("Informe o nome do contato que deseja excluir: ")
        for c in cls.__contatos:
            if c.get_nome() == nome:
                cls.__contatos.remove(c)
                print("Contato excluido")


    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

ContatoUI.main()

#3
class Pais:
    def __init__(self, i, n, p, a):
        self.__id = i
        self.__nome = n
        self.__populacao = p
        self.__area = a
    def get_nome(self):
        return self.__nome
    def set_populacao(self, nova_p):
        self.__populacao = nova_p
    def get_populacao(self):
        return self.__populacao
    def set_area(self, nova_a):
        self.__area = nova_a
    def densidade(self):
        return self.__populacao/self.__area
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__populacao} - {self.__area}"

class PaisUI:
    __paises = []

    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.atualizar()
            if op == 4: cls.excluir()
            if op == 5: cls.mais_populoso()
            if op == 6: cls.mais_povoado()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Mais Populoso, 6-Mais Povoado, 7-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        i = int(input("Informe o id: "))
        n = input("Informe o nome: ")
        p = int(input("Informe a população: "))
        a = float(input("Informe a área: "))
        pais = Pais(i, n, p, a)
        cls.__paises.append(pais)

    @classmethod
    def listar(cls):
        for p in cls.__paises:
            print(p)

    @classmethod
    def atualizar(cls):
        nome = input("Informe o nome do país que deseja atualizar: ")
        for p in cls.__paises:
            if p.get_nome() == nome:
                nova_p = int(input("Informe a população: "))
                nova_a = float(input("Informe a área: "))
                p.set_populacao(nova_p)
                p.set_area(nova_a)
                print("País atualizado")
            else:
                print("País não cadastrado")

    @classmethod
    def excluir(cls):
        nome = input("Informe o nome do país a ser excluído: ")
        for p in cls.__paises:
            if p.get_nome() == nome:
                cls.__paises.remove(p)
                print("País excluído")
            else:
                print("País não cadastrado")

    @classmethod
    def mais_populoso(cls):
        if len(cls.__paises) == 0:
            print("Nenhum país cadastrado")
        else:
            mais = cls.__paises[0]
            for p in cls.__paises:
                if p.get_populacao() > mais.get_populacao():
                    mais = p
            print(f"País mais populoso: {mais}")

    @classmethod
    def mais_povoado(cls):
        if len(cls.__paises) == 0:
            print("Nenhum país cadastrado")
        else:
            mais = cls.__paises[0]
            for p in cls.__paises:
                if p.densidade() > mais.densidade():
                    mais = p
            print(f"País mais povoado: {mais}")

PaisUI.main()