import abc


class Conta(abc.ABC):
    def __init__(self, conta, saldo):
        self.conta = conta
        self.saldo = saldo
        
        
    @abc.abstractmethod   
    def sacar(self, valor):
        pass
        
    def depositar(self, valor):
        self.saldo += valor
       
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}' 
        

        
        
        
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
    
    
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.saldo_conta(f'(SAQUE {valor})')
            return self.saldo
        
        print('Nao foi possivel sacar o valor desejado')
        self.saldo_conta(f'SAQUE NEGADO {valor}')
        
        
class ContaCorrente(Conta):
    
    def __init__(self, conta, saldo = 0):
        super().__init__(conta, saldo)
       
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
    
    
    
        
