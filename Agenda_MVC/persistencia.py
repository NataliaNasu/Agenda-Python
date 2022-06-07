from os.path import exists, getsize
import pickle

class Persistencia:

    def __init__(self) -> None:

        self.file_name = 'contatos.pkl'
        self.dadosContato = {}
        self.carregarAgenda()

    def sair(self, dict) -> None:

        self.dadosContato = dict
        self.gravarAgenda()

    def carregarAgenda(self) -> None:

        if exists(self.file_name) and getsize(self.file_name) > 0:
            with open(self.file_name, 'rb') as file:
                self.dadosContato = pickle.load(file)

    def gravarAgenda(self) -> None:

        with open(self.file_name, 'wb') as file:
            pickle.dump(self.dadosContato, file)
