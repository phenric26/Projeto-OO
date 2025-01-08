from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, conta, saldo):
        self.numero_conta = conta
        self.saldo = saldo
        
        
    @abstractmethod   
    def sacar(self, valor):
        pass
        
    def depositar(self, valor):
        self.saldo += valor 
        
class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
    
    
        if valor_pos_saque >= 0:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
            return True 
        
        
class ContaCorrente(Conta):
    
    def __init__(self, numero_conta, saldo = 0):
        super().__init__(numero_conta, saldo)
       
    
    def sacar(self, valor, limite = 1000):
        self.limite = limite
        valor_pos_saque = self.saldo - valor
    
        
        if valor > limite:
            print("Saque maior que o limite de R$ 1000,00")
            return False
        elif valor_pos_saque >= 0:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
            return True 
        
        
            
    
    
    
        
