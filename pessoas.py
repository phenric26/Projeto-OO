import contas

class Pessoa:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha= senha
        self.contas = []
        
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
        
class Cliente(Pessoa):
    def __init__(self, nome, senha):
        super().__init__(nome, senha)
        self.conta: contas.Conta | None = None
        
