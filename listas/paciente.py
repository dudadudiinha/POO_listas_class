from datetime import datetime
class Paciente:
    def __init__(self, nome, cpf, tel, nasc)
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__nasc = nasc
        self.set_nasc(self.__nasc)
    def set_nasc(self, nasc):
        if nasc > datetime.today():
            raise ValueError("A data de nascimento é inválida")
        self.__nasc = nasc
    def get_nasc(self):
        return self.__nasc
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_tel(self):
        return self.__tel

class PacienteUI:
    @classmethod
    def main(cls):
        pass

    @classmethod
    def menu(cls):
        return int(input("1-Inserir, 2-Listar, 3-Alterar, 4-Recuperar, 6-Fim\nInforme uma opção: "))

    @classmethod
    def inserir(cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        tel = input("Informe o telefone: ")
        nasc = input("Informe a data de nascimento: ")
        paciente = Paciente(nome, cpf, tel, nasc)