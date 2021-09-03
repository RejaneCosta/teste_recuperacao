class Contato:

    def __init__(self, NomeContato, Apelido, TelefoneContato, EmailContato):
        self.__NomeContato = NomeContato
        self.__Apelido = Apelido
        self.__TelefoneContato = TelefoneContato
        self.__EmailContato = EmailContato

    def set_NomeContato(self, NomeContato):
        set.__NomeContato = NomeContato

    def get_NomeContato(self):
        return self.__NomeContato

    def set_Apelido(self, Apelido):
        set.__Apelido = Apelido

    def get_Apelido(self):
        return self.__Apelido

    def set_TelefoneContato(self, TelefoneContato):
        set.__TelefoneContato = TelefoneContato

    def get_TelefoneContato(self):
        return self.__TelefoneContato

    def set_EmailContato(self, EmailContato):
        set.__EmailContato = EmailContato

    def get_EmailContato(self):
        return self.__EmailContato

