from datetime import datetime

class Livro:
    def __init__(self, id, titulo, autor, data_leitura):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__data_leitura = data_leitura
    def set_id(self, id):
        if id < 0: raise ValueError("ID inválido.")
        self.__id = id
    def get_id(self):
        return self.__id
    def set_titulo(self, titulo):
        if titulo == "": raise ValueError("Título inválido.")
        self.__titulo = titulo
    def get_titulo(self):
        return self.__titulo
    def set_autor(self, autor):
        if autor == "": raise ValueError("Autor inválido.")
        self.__autor = autor
    def get_autor(self):
        return self.__autor
    def set_data_leitura(self, data_leitura):
        if data_leitura > datetime.now(): raise ValueError("Data inválida.")
        self.__data_leitura = data_leitura
    def get_data_leitura(self):
        return self.__data_leitura
    
    def __str__(self):
        return f"{self.__id} - {self.__titulo}, {self.__autor}\nLido em {self.__data_leitura.strftime('%d/%m/%Y')}"

class LivroUI:
    __livros = []
    @classmethod
    def main(cls):    
        return int(input("1 - Inserir, 2 - Listar todos, 3 - Listar pelo ID, 4 - Atualizar, 5 - Excluir, 6 - Primeiro livro, 7 - Fim\nInforme uma opçao: "))
    @classmethod
    def menu(cls):
        op = 0
        while op != 7:
            op = cls.main()
            match op:
                case 1: cls.inserir()
                case 2: cls.listar()
                case 3: cls.listar_id()
                case 4: cls.atualizar()
                case 5: cls.excluir()
                case 6: cls.primeiro()
    @classmethod
    def inserir(cls):
        id = int(input("Informe o ID: "))
        titulo = input("Informe o título da obra: ")
        autor = input("Informe o autor: ")
        data_leitura = datetime.strptime(input("Informe a data de leitura: "), '%d/%m/%Y')
        l = Livro(id, titulo, autor, data_leitura)
        cls.__livros.append(l)
    @classmethod
    def listar(cls):
        for l in cls.__livros:
            print(l)
        if len(cls.__livros) == 0:
            print("Nenhum livro foi cadastrado.")
    @classmethod
    def listar_id(cls):
        id = int(input("Informe o ID: "))
        for l in cls.__livros:
            if l.get_id() == id:
                print(l)
                return
        print("ID não encontrado.")
    @classmethod
    def atualizar(cls):
        id = int(input("Informe o ID: "))
        for l in cls.__livros:
            if l.get_id() == id:
                titulo = input("Informe o título da obra: ")
                autor = input("Informe o autor: ")
                data_leitura = datetime.strptime(input("Informe a data de leitura: "), '%d/%m/%Y')
                l.set_titulo(titulo)
                l.set_autor(autor)
                l.set_data_leitura(data_leitura)
                print("Dados atualizados.")
                return
        print("ID não encontrado.")
    @classmethod
    def excluir(cls):
        id = int(input("Informe o ID: "))
        for l in cls.__livros:
            if l.get_id() == id:
                cls.__livros.remove(l)
                return
        print("ID não encontrado.")
    @classmethod
    def primeiro(cls):
        if len(cls.__livros) == 0:
            print("Nenhum livro cadastrado.")
            return
        antigo = cls.__livros[0]
        for l in cls.__livros[1:]:
            if antigo.get_data_leitura() > l.get_data_leitura():
                antigo = l
        print(f"{antigo}")

LivroUI.menu()