from datetime import datetime, timedelta

class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

    def set_id(self, id):
        if id < 0:
            raise ValueError("ID inválido.")
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_data(self, data):
        if data > datetime.now():
            raise ValueError("Data inválida.")
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_distancia(self, distancia):
        if distancia < 0:
            raise ValueError("Distância inválida.")
        self.__distancia = distancia
    def get_distancia(self):
        return self.__distancia
    
    def set_tempo(self, tempo):
        if tempo < timedelta(0):
            raise ValueError("Tempo inválido.")
        self.__tempo = tempo
    def get_tempo(self):
        return self.__tempo
    
    def __str__(self):
        return f"\n{self.__id} - Treino de {self.__data.strftime('%d/%m/%Y')}\nTempo marcado: {self.__tempo}\nDistância percorrida: {self.__distancia}\n"
    
class TreinoUI:
    __treino = []

    @classmethod
    def menu(cls):
        return int(input("1 - Inserir, 2 - Listar, 3 - Procurar, 4 - Atualizar, - 5 - Excluir, 6 - Mais rápido, 7 - Fim\nInforme uma opção: "))
    
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = cls.menu()
            match op:
                case 1: cls.inserir()
                case 2: cls.listar()
                case 3: cls.listar_id()
                case 4: cls.atualizar()
                case 5: cls.excluir()
                case 6: cls.mais_rapido()

    @classmethod
    def inserir(cls):
        data = datetime.strptime(input("Informe a data do treino: "), '%d/%m/%Y')
        distancia = float(input("Informe a nova distância percorrida: "))
        h, m, s = map(int, input("Informe o tempo de treino (bb:mm:ss): ").split(":"))
        tempo = timedelta(hours=h, minutes=m, seconds=s)
        id = 1
        for t in cls.__treino:
            id += 1
        t = Treino(id, data, distancia, tempo)
        cls.__treino.append(t)

    @classmethod
    def listar(cls):
        for t in cls.__treino:
            print(t)
        if len(cls.__treino) == 0:
            print("Não há nenhum treino cadastrado.")

    @classmethod
    def listar_id(cls):
        id = int(input("Informe o id: "))
        for t in cls.__treino:
            if id == t.get_id():
                return print(t)
        print("Treino não encontrado.")

    @classmethod
    def atualizar(cls):
        id = int(input("Informe o id: "))
        for t in cls.__treino:
            if id == t.get_id():
                data = datetime.strptime(input("Informe a nova data do treino: "), '%d/%m/%Y')
                distancia = float(input("Informe a nova distância percorrida: "))
                h, m, s = map(int, input("Informe o tempo de treino (bb:mm:ss): ").split(":"))
                tempo = timedelta(hours=h, minutes=m, seconds=s)
                t.set_data(data)
                t.set_distancia(distancia)
                t.set_tempo(tempo)
        else:
            print("Treino não encontrado.")

    @classmethod
    def excluir(cls):
        id = int(input("Informe o id: "))
        for t in cls.__treino:
            if id == t.get_id():
                cls.__treino.remove(t)
                return
        print("Treino não encontrado.")

    @classmethod
    def mais_rapido(cls):
        if len(cls.__treino) == 0:
            print("Nenhum treino cadastrado.")
            return
        maior = cls.__treino[0] 
        for t in cls.__treino[1:]:
            v_t = t.get_distancia() / (t.get_tempo().total_seconds() / 3600)
            v_maior = maior.get_distancia() / (maior.get_tempo().total_seconds() / 3600)
            if v_t > v_maior:
                maior = t
        print(maior)

TreinoUI.main()