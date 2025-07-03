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
        if email in c:
            print("Email já cadastrado. Digite novamente")
        else: cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)

    @classmethod
    def atualizar(cls):
        cls.listar()
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
            else: print("Contato inexistente") 

    @classmethod
    def excluir(cls):
        cls.listar()
        nome = input("Informe o nome do contato que deseja excluir: ")
        for c in cls.__contatos:
            if c.get_nome() == nome:
                cls.__contatos.remove(c)
                print("Contato excluido")
            else: print("Contato inexistente") 

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

ContatoUI.main()