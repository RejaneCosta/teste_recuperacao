from agenda_telefonica import AgendaTelefonica
from contato import Contato
from tarefa import CriarTarefas


class main:
    def __init__(self):
        self.AgendaTelefonica = []
        self.CadastrarContato = []
        self.ListarContatos = []
        self.ExcluirContato = []
        self.CriarTarefas = []
        self.ListarTarefas = []
        self.ExcluirTarefas = []
        self.Sair = []

    def v_menu(self):
        menu = 0
        while (menu != 99):
            print("-----> MENU <-----")
            print("01 - Agenda Telefonica")
            print("02 - Cadastrar Contato")
            print("03 - Listar Contatos")
            print("04 - Excluir Contato")
            print("05 - Criar Tarefas")
            print("06 - Listar Tarefas")
            print("07 - Excluir Tarefas")
            print("99 - sair")
            menu = input("Qual a opção desejada? ")
            print("----------------------")

            if(menu == "01"):
                return self.AgendaTelefonica
            elif(menu == "02"):
                return self.v_CadastrarContato
            elif(menu == "03"):
                return self.v_ListarContatos
            elif(menu == "04"):
                return self.v_ExcluirContato
            elif(menu == "05"):
                return self.CriarTarefas
            elif(menu == "06"):
                return self.ListarTarefas
            elif(menu == "07"):
                return self.ExcluirTarefas
            elif(menu == "99"):
                return self.Sair

    def v_AgendaTelefonica(self):
        NomeProprietario = input("Informe seu nome")
        Ano = input("informe o apelido")
        Agenda = AgendaTelefonica(NomeProprietario, Ano)
        self.AgendaTelefonica.append(Agenda)

    def v_CadastrarContato(self):
        NomeContato = input("Informe seu nome")
        Apelido = input("informe o apelido")
        TelefoneContato = input("informe o telefone")
        EmailContato = input("informe seu e-mail")
        ContatoNovo = Contato(NomeContato, Apelido, TelefoneContato, EmailContato)
        self.CadastrarContato.append(ContatoNovo)

    def v_ListarContatos(self):
        for i in self.CadastrarContato:
            print("Nome: " + str(i.getNomeContato()))
            print("Apelido: " + str(i.getApelido()))
            print("Telefone: " + str(i.getTelefoneContato()))
            print("Email: " + str(i.getEmailContato()))

    def v_ExcluirContato(self):
        TelefoneContato = input("Qual CPF deseja excluir?")
        for i in self.CadastrarContato:
            if(i.geTelefoneContato() == TelefoneContato):
                print("Excluíndo " + i.getNome())
                self.CadastrarContato.remove(i)
                print("item excluido")

    def v_CriarTarefas(self):
        AdicionarDescricao = input("Informe a descrição")
        SelecionarStatus = False
        NovaTarefa = CriarTarefas(AdicionarDescricao, SelecionarStatus):
        self.CriarTarefas.append(NovaTarefa)

    def v_ListarTarefas(self):
        id = -1
        for i in self.CriarTarefas:
            id = id + 1
            print("ID: " + str(id))
            print('Tarefa: ' + str(i.getAdicionarDescricao()))
            print('Status: ' + str(i.getSelecionarStatus()))

    def v_ExcluirTarefas(self):
        id = input("Qual Id deseja excluir?")
        posicao = -1
        for i in self.ListarTarefas:
            posicao = posicao + 1
            if(str(posicao) == id):
                print("Excluíndo " + i.getDescricao())
                self.ListarTarefas.remove(i)
                print("item excluido")




