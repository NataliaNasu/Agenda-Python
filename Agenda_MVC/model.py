from persistencia import Persistencia

class Model():

    def __init__(self) -> None:

        self.persistencia = Persistencia()

        self.dict = self.persistencia.dadosContato


    def sair(self):
        self.persistencia.sair(self.dict)

    def adicionarModel(self, nome: str, telefone: str, tipoConta: str, favorito: str) -> None:
        self.dict[nome] = telefone, tipoConta, favorito


    def excluirModel(self, nome: str) -> None:
        try:
            del self.dict[nome]
        except KeyError:
            raise ValueError('Contato inexistente!')

    def pesquisarModel(self, nome: str) -> dict:
        if nome in self.dict:
            return nome, self.dict[nome]
        else:
            raise ValueError('Contato não foi encontrado!')
