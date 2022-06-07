import sys
import tkinter as tk
from tkinter import messagebox
from controller import Controller

class View():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x350')
        self.root.title('Agenda Telefônica')

        self.controller = Controller(self)

        self.telaAdicionar()
        self.telaExibirDados()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.bind('<Escape>', self.exit)

        self.root.mainloop()


    def telaAdicionar(self):
        self.telaPrincipal = tk.Frame(self.root)
        self.telaPrincipal.grid(row=0, column=0)

        labelTitulo = tk.Label(self.telaPrincipal, width=20, text='CONTATO:')
        labelTitulo.grid(row=0, column=0)

        labelNome = tk.Label(self.telaPrincipal, width=20, text='Nome:')
        labelNome.grid(row=1, column=0)

        self.entryNome = tk.Entry(self.telaPrincipal, width=20)
        self.entryNome.grid(row=1, column=1)

        labelTelefone = tk.Label(self.telaPrincipal, width=20, text='Telefone:')
        labelTelefone.grid(row=2, column=0)

        self.entryTelefone = tk.Entry(self.telaPrincipal, width=20)
        self.entryTelefone.grid(row=2, column=1)

        labelTipoConta = tk.Label(self.telaPrincipal, width=20, text='Tipo da Conta:')
        labelTipoConta.grid(row=3, column=0)

        self.radioValue = tk.StringVar()
        self.radioComercial = tk.Radiobutton(self.telaPrincipal, text='Comercial',
                                             width=10, variable=self.radioValue,
                                             value='comercial')
        self.radioComercial.grid(row=4, column=0)

        self.radioPessoal = tk.Radiobutton(self.telaPrincipal, text='Pessoal',
                                           width=10, variable=self.radioValue,
                                           value='pessoal')
        self.radioPessoal.grid(row=4, column=1)

        labelFavorito = tk.Label(self.telaPrincipal, width=10, text='Favorito:')
        labelFavorito.grid(row=5, column=0)

        self.addFav = tk.BooleanVar()
        chkBtn = tk.Checkbutton(self.telaPrincipal, text='Sim', width=10,
                                 variable=self.addFav)
        chkBtn.grid(row=5, column=1)

        btnSalvar = tk.Button(self.telaPrincipal, text='Salvar',
                           width=20, command=self.add_contact)
        btnSalvar.grid(row=6, column=1)


    def telaExibirDados(self):
        self.telaPrincipal = tk.Frame(self.root)
        self.telaPrincipal.grid(row=7, column=0)

        labelPesquisar = tk.Label(self.telaPrincipal, width=40, text='PESQUISAR: ')
        labelPesquisar.grid(row=0, column=0)

        labelSearch = tk.Label(self.telaPrincipal, width=40, text='Nome:')
        labelSearch.grid(row=1, column=0)

        self.srchNome = tk.Entry(self.telaPrincipal, width=30)
        self.srchNome.grid(row=2, column=0)

        btnTelaPesquisar = tk.Button(self.telaPrincipal,
                                     text='Pesquisar',
                                     width=20, command=self.srch_contact)
        btnTelaPesquisar.grid(row=3, column=0)

        btnTelaExcluir = tk.Button(self.telaPrincipal,
                                   text='Excluir',
                                   width=20, command=self.del_contact)
        btnTelaExcluir.grid(row=4, column=0)

        labelShow = tk.Label(self.telaPrincipal, width=40, text='RESULTADO:')
        labelShow.grid(row=5, column=0)

        self.labelExibir = tk.Label(self.telaPrincipal, width=40, text='')
        self.labelExibir.grid(row=6, column=0)

    def add_contact(self):
        returned = self.controller.adicionarView(self.entryNome.get(), self.entryTelefone.get(),
                                                 self.radioValue.get(), self.addFav.get())
        self.eval(returned)

    def del_contact(self):
        returned = self.controller.excluirView(self.srchNome.get())
        self.labelExibir['text'] = ''
        self.eval(returned)

    def srch_contact(self):
        returned = self.controller.pesquisarView(self.srchNome.get())
        self.labelExibir['text'] = returned
        self.eval(returned)


    def showInfo(self, msg):
        messagebox.showinfo('Informação', msg)

    def showWarning(self, msg):
        messagebox.showwarning('Warning', msg)

    def eval(self, returned) -> None:

        if returned[0] == 'ALERT':
            self.showWarning(returned[1])
        elif returned[0] == 'MSG':
            self.showInfo(returned[1])
        elif returned[0] == 'CONTATO':
            self.showInfo('Nome: ' + str(returned[1][0]) + '\n' +
                          'Dados: ' + str(returned[1][1]) + '\n')


    def exit(self, evento=None):
        self.controller.sair()
        sys.exit()

View()