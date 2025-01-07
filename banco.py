import contas
import pessoas
import os
import json
import random

class Banco:
    def __init__(self, clientes=None, contas=None):
        self.clientes = clientes or []
        self.contas = contas or []
        
    

    def _checa_cliente(self, cliente):
        return cliente in self.clientes


    def _checa_conta(self, conta):
        return conta in self.contas

    def autenticar(self, nome_cliente, senha_cliente, numero_conta):
        # Verifica se o cliente com o nome e a senha existe
        cliente = next((c for c in self.clientes if c.nome == nome_cliente and c.senha == senha_cliente), None)
        
        if cliente:
            # Verifica se a conta associada ao cliente corresponde ao número fornecido
            if cliente.conta.conta == numero_conta:
                return cliente  # Autenticação bem-sucedida, retorna o cliente
        return None  # Retorna None caso o cliente ou a conta não coincidam

    


banco = Banco()


def carregar_dados_json():
    try:
        with open('dados_banco.json', 'r') as f:
            dados = json.load(f)
        
        # Recarregar clientes e contas
        for cliente_data in dados:
            cliente = pessoas.Cliente(cliente_data['nome'], cliente_data['senha'])
            numero_conta = cliente_data['conta']['numero_conta']
            saldo = cliente_data['conta']['saldo']
            
            # Adicionando uma verificação para o tipo de conta
            tipo_conta = cliente_data['conta'].get('tipo_conta', 'corrente')  # Ajuste isso de acordo com o formato dos dados
            if tipo_conta == 'corrente':
                conta = contas.ContaCorrente(numero_conta, saldo)
            elif tipo_conta == 'poupanca':
                conta = contas.ContaPoupanca(numero_conta, saldo)
            else:
                continue  # Caso haja erro no tipo de conta
            
            cliente.conta = conta
            banco.clientes.append(cliente)
            banco.contas.append(conta)
        
        print("Dados carregados com sucesso!")
    
    except FileNotFoundError:
        print("Arquivo 'dados_banco.json' não encontrado. Iniciando com dados vazios.")

def inicio():
    print("=== Sistema Bancário ===")
    carregar_dados_json()
    opcao = input("Já possui conta? Y/N - ")
    
    if opcao.upper() == "Y":
        nome = input("Digite o nome completo: ")
        senha = input("Digite sua senha: ")
        
        numero_conta = int(input("Digite o número da conta: "))
        
        cliente = banco.autenticar(nome, senha, numero_conta)
        
        if cliente:
            print("Autenticação bem-sucedida!")
            menu(cliente)  # Redireciona para o menu do cliente
        else:
            print("Nome ou senha incorretos. Tente novamente.")
            inicio()  # Se falhar, chama novamente a função para tentar autenticar
        
    else:
        print("Faça seu cadastro!")
        cliente = criar_cliente()  # Permite o cadastro de um novo cliente
        menu(cliente)  # Redireciona para o menu após o cadastro
  

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
    
def salvar_json():
    dados = []
    for cliente in banco.clientes:
        cliente_data = {
            'nome': cliente.nome,
            'senha': cliente.senha,
            'conta': {
                'numero_conta': cliente.conta.conta,
                'saldo': cliente.conta.saldo
            }
        }
        dados.append(cliente_data)

    with open('dados_banco.json', 'w') as f:
        json.dump(dados, f, indent=4)

def salvar_txt():      
    with open('dados_banco.txt', 'w') as f:
        for cliente in banco.clientes:
            f.write(f"Cliente: {cliente.nome}\n")
            f.write(f"Senha: {cliente.senha}\n")
            f.write(f"Conta: {cliente.conta.conta}\n")
            f.write(f"Saldo: {cliente.conta.saldo:.2f}\n")
            f.write("-" * 40 + "\n")
            
def salvar_dados():
    salvar_json()
    salvar_txt()
    print("Dados do banco foram salvos!")

if __name__ == "__main__":
    inicio()
