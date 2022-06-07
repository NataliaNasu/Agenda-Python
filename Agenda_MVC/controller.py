from model import Model

class Controller():

    def __init__(self, view):
        self.model = Model()
        self.view = view

    def sair(self):
        self.model.sair()

    def adicionarView(self, name: str, phone: str,
                      accountType: str, favourite: str) -> None:
        try:
            self.model.adicionarModel(name, phone, accountType, favourite)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('MSG', 'Contato salvo!')

    def excluirView(self, name) -> None:
        try:
            self.model.excluirModel(name)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('MSG', 'Contato excluído!')

    def pesquisarView(self, name):
        try:
            nome = self.model.pesquisarModel(name)
        except ValueError as err:
            return ('ALERT', str(err))
        else:
            return ('CONTATO', nome)
