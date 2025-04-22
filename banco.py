import contas
import pessoas
import os
import json


class Banco:
    def __init__(self, clientes=None, contas=None):
        self.clientes = clientes or []
        self.contas = contas or []
        
    

    def _checa_cliente(self, cliente):
        return cliente in self.clientes


    def _checa_conta(self, conta):
        return conta in self.contas

    def autenticar(self, nome_cliente, senha_cliente):
        cliente = next((c for c in self.clientes if c.nome == nome_cliente and c.senha == senha_cliente), None)
        
        if cliente:
                return cliente  
        return None 

    


banco = Banco()


def carregar_dados_json():
    try:
        with open('dados_banco.json', 'r') as f:
            dados = json.load(f)
        
        for cliente_data in dados:
            cliente = pessoas.Cliente(cliente_data['nome'], cliente_data['senha'])
            
            for conta_data in cliente_data['contas']:
                numero_conta = conta_data['numero_conta']
                saldo = conta_data['saldo']
                tipo_conta = conta_data.get('tipo_conta', 'corrente')
                
                if tipo_conta == 'corrente':
                    conta = contas.ContaCorrente(numero_conta, saldo)
                elif tipo_conta == 'poupanca':
                    conta = contas.ContaPoupanca(numero_conta, saldo)
                else:
                    continue  
                
                cliente.contas.append(conta)
                banco.contas.append(conta)

            banco.clientes.append(cliente)

    except FileNotFoundError:
        print("")


def inicio():
    print("=== Sistema Bancário ===")
    carregar_dados_json()
    opcao = input("Já possui conta? Y/N - ")

    if opcao.upper() == "Y":
        nome = input("Digite seu nome completo: ")
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
        os.system("clear")
        print("=== Contas do Cliente ===")
        for i, conta in enumerate(cliente.contas, start=1):
            print(f"{i}. {type(conta).__name__} - Número: {conta.numero_conta} - Saldo: {conta.saldo:.2f}")
        
        print("\n1. Criar Conta Poupança")
        print("2. Depósito")
        print("3. Saque")
        print("4. Transferir")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criar_conta_poupanca(cliente)
        elif opcao == "2":
            deposito(cliente)
        elif opcao == "3":
            saque(cliente)
        elif opcao == "4":
            os.system("clear")
            numero_conta_origem = int(input("Digite o número da conta origem: "))
            numero_conta_destino = int(input("Digite o número da conta destino: "))
            valor = float(input("Digite o valor da transferência: "))
            transferir(cliente, numero_conta_origem, numero_conta_destino, valor)
        elif opcao == "5":
            print("Saindo...")
            salvar_dados()
            break
        else:
            print("Opção inválida! Tente novamente.")


def criar_cliente():
    os.system("clear")
    nome = input("Digite o nome completo: ")
    senha = input("Digite sua senha: ")
    cliente = pessoas.Cliente(nome, senha)
    
    while True:
        try:
            numero_conta_corrente = int(input("Digite um número de conta corrente: "))
            
            if any(conta.numero_conta == numero_conta_corrente for conta in banco.contas):
                print(f"Erro: O número da conta {numero_conta_corrente} já existe. Tente outro número.")
            else:
                break
        except ValueError:
            print("Erro: Digite um número válido para a conta.")
            
    conta_corrente = contas.ContaCorrente(numero_conta_corrente)
    
    cliente.contas.append(conta_corrente) 
    banco.clientes.append(cliente)
    banco.contas.append(conta_corrente)
    
    print(f"Cliente {nome} criado com sucesso com a Conta Corrente número {numero_conta_corrente}!")
    return cliente
    

def criar_conta_poupanca(cliente):
    os.system("clear")
    
    while True:
        try:
            numero_conta = int(input("Digite o número da conta poupança: "))
            
            if any(conta.numero_conta == numero_conta for conta in banco.contas):
                print(f"Erro: O número da conta {numero_conta} já existe. Tente outro número.")
            else:
                break
        except ValueError:
            print("Erro: Digite um número válido para a conta.")
            
    saldo = float(input("Digite o saldo inicial: "))
    conta_poupanca = contas.ContaPoupanca(numero_conta, saldo)
    
    cliente.contas.append(conta_poupanca)  
    banco.contas.append(conta_poupanca)
    
    print(f"Conta Poupança criada com sucesso para o cliente {cliente.nome}!")

def deposito(cliente):
    os.system("clear")
    
    numero_conta = int(input("Digite o número da conta: "))
    conta = next((c for c in banco.contas if c.numero_conta == numero_conta), None)

    if not conta:
        print("Conta não encontrada!")
        return
    
    valor = float(input("Digite o valor do depósito: "))
    conta.depositar(valor)
    
    print(f"Depósito de {valor:.2f} realizado com sucesso!")
    print(f"O saldo atual da conta é: {conta.saldo:.2f}")

def saque(cliente):
    os.system("clear")
    
    numero_conta = int(input("Digite o número da conta: "))
    conta = next((c for c in banco.contas if c.numero_conta == numero_conta), None)

    if not conta:
        print("Conta não encontrada!")
        return
    
    valor = float(input("Digite o valor do saque: "))
    if valor > conta.saldo:
        print("Saldo insuficiente.")
        return

    
    if conta.sacar(valor):
        print("Operacao realizada com sucesso")
        
    else:
        print("Tente novamente!")
        
def transferir(cliente_origem, numero_conta_origem, numero_conta_destino, valor):
    os.system("clear")

    if valor <= 0:
        print("Valor inválido para transferência.")
        return

    conta_origem = next((c for c in cliente_origem.contas if c.numero_conta == numero_conta_origem), None)

    if not conta_origem:
        print("Conta de origem não encontrada para o cliente.")
        return

    if valor > conta_origem.saldo:
        print("Saldo insuficiente para transferência.")
        return

    conta_destino = next((c for c in banco.contas if c.numero_conta == numero_conta_destino), None)

    if not conta_destino:
        print("Conta destino não encontrada.")
        return

   
    if conta_origem.sacar(valor):  
        conta_destino.depositar(valor) 
        print(f"Transferência de R${valor:.2f} realizada com sucesso!")
        salvar_dados() 
    else:
        print("Não foi possível realizar a transferência.")
    

    
def salvar_json():
    dados = []
    for cliente in banco.clientes:
        contas_data = [
            {
                'numero_conta': conta.numero_conta,
                'saldo': conta.saldo,
                'tipo_conta': 'corrente' if isinstance(conta, contas.ContaCorrente) else 'poupanca'
            }
            for conta in cliente.contas  
        ]
        
        cliente_data = {
            'nome': cliente.nome,
            'senha': cliente.senha,
            'contas': contas_data
        }
        dados.append(cliente_data)

    with open('dados_banco.json', 'w') as f:
        json.dump(dados, f, indent=4)



            
def salvar_dados():
    salvar_json()
    
if __name__ == "__main__":
    inicio()
    print("COmecamndo ...")
