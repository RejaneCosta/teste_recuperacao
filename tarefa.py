class CriarTarefas:

    def __init__(self, AdicionarDescricao, SelecionarStatus):
        self.__AdicionarDescricao = AdicionarDescricao
        self.__SelecionarStatus = SelecionarStatus

    def set_AdicionarDescricao(self, AdicionarDescricao):
        self.__AdicionarDescricao = AdicionarDescricao

    def get_AdicionarDescricao(self):
        return self.__AdicionarDescricao

    def set_SelecionarStatus(self,SelecionarStatus):
        self.__SelecionarStatus = SelecionarStatus

    def get_SelecionarStatus(self):
        return self.__SelecionarStatus
