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