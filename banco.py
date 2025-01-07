import contas
import pessoas
import os
import random

class Banco:
    def __init__(self, clientes=None, contas=None):
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_cliente(self, cliente):
        return cliente in self.clientes


    def _checa_conta(self, conta):
        return conta in self.contas

    def autenticar(self, cliente, conta):
        return self._checa_cliente(cliente) and \
               self._checa_conta(conta)


banco = Banco()


def inicio():
    print("=== Sistema Bancário ===")
    opcao = input("Já possui conta? Y/N - ")
    
    if opcao.upper() == "Y":
        nome = input("Digite o nome completo: ")
        senha = input("Digite sua senha: ")
        cliente = banco.autenticar(nome, senha)  
        if cliente:
            print("Autenticação bem-sucedida!")
            menu(cliente)
        else:
            print("Nome ou senha incorretos. Tente novamente.")
            inicio()  
        
    else:
        print("Faça seu cadastro!")
        cliente = criar_cliente()  
        menu(cliente)  

def menu(cliente):
    while True:
        print(f"=== Saldo da Conta: {cliente.conta.saldo:.2f} ===")
        
        print("1. Criar Conta Poupança")
        print("2. Depósito")
        print("3. Saque")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            criar_conta_poupanca(cliente)
            input("Pressione Enter para voltar ao menu.")
                
        elif opcao == "2":
            deposito(cliente)
            input("Pressione Enter para voltar ao menu.")
            
        elif opcao == "3":
            saque(cliente)
            input("Pressione Enter para voltar ao menu.")
            
        elif opcao == "4":
            print("Salvando dados antes de encerrar...")
            salvar_dados()
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

def criar_cliente():
    os.system("clear")
    nome = input("Digite o nome completo: ")
    senha = input("Digite sua senha: ")
    cliente = pessoas.Cliente(nome, senha)
    numero_conta_corrente = int(input("Digite um numero de conta corrente: ")) 
    conta_corrente = contas.ContaCorrente(numero_conta_corrente)
    
    cliente.conta = conta_corrente  
    banco.clientes.append(cliente)
    banco.contas.append(cliente.conta)
    
    print(f"Cliente {nome} criado com sucesso com a Conta Corrente número {numero_conta_corrente}!")
    return cliente  

def criar_conta_poupanca(cliente):
    os.system("clear")
    
    if cliente.conta:
        print("Cliente já possui uma conta!")
        return

    numero_conta = int(input("Digite o número da conta poupança "))
    saldo = float(input("Digite o saldo inicial: "))

    conta = contas.ContaPoupanca(numero_conta, saldo)
    cliente.conta = conta
    banco.contas.append(conta)
    print(f"Conta Poupança criada com sucesso para o cliente {cliente.nome}!")

def deposito(cliente):
    os.system("clear")
    
    numero_conta = int(input("Digite o número da conta: "))
    conta = next((c for c in banco.contas if c.conta == numero_conta), None)

    if not conta:
        print("Conta não encontrada!")
        return
    
    valor = float(input("Digite o valor do depósito: "))
    cliente.conta.depositar(valor)
    
    print(f"Depósito de {valor:.2f} realizado com sucesso!")
    print(f"O saldo atual da conta é: {cliente.conta.saldo:.2f}")

def saque(cliente):
    os.system("clear")
    
    numero_conta = int(input("Digite o número da conta: "))
    conta = next((c for c in banco.contas if c.conta == numero_conta), None)

    if not conta:
        print("Conta não encontrada!")
        return
    
    valor = float(input("Digite o valor do saque: "))
    if valor > cliente.conta.saldo:
        print("Saldo insuficiente.")
        return

    cliente.conta.sacar(valor)
    print(f"Saque de {valor:.2f} realizado com sucesso!")

def salvar_dados():
    # Exemplo de salvamento de dados (pode ser adaptado para JSON, banco de dados, etc.)
    print("Dados do banco foram salvos!")

if __name__ == "__main__":
    inicio()
