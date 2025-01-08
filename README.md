Sistema Bancário

Este é um sistema bancário simples desenvolvido em Python, utilizando programação orientada a objetos (POO), com o objetivo de gerenciar clientes e contas bancárias. O sistema permite criar contas correntes e contas poupança, realizar depósitos e saques, além de autenticar clientes com base no nome e na senha.

Como Utilizar

    Iniciar o sistema:
        O sistema pode ser iniciado executando o script principal(Banco.py). Ele carregará os dados salvos no arquivo dados_banco.json ou criará um novo arquivo se não houver dados existentes.

    Cadastrar um novo cliente:
        Ao iniciar o sistema, o cliente será solicitado a informar se já possui uma conta ou se deseja criar uma nova conta. Caso escolha criar uma nova conta, ele deverá fornecer seu nome, senha e número da conta.

    Autenticar-se no sistema:
        Para clientes existentes, será necessário fornecer o nome e a senha para autenticação. Se a autenticação for bem-sucedida, o cliente poderá acessar o menu de operações bancárias.

    Operações bancárias:
        O cliente pode escolher entre as opções do menu: criar uma nova conta poupança, realizar um depósito ou um saque.

    Salvar dados:
        As alterações realizadas nas contas e clientes serão salvas automaticamente no arquivo dados_banco.json ao final de cada sessão.


Funcionalidades

    Cadastro de clientes:
        O sistema permite que novos clientes se cadastrem, fornecendo nome, senha e número da conta corrente.

    Autenticação de clientes:
        O cliente pode autenticar-se no sistema utilizando o nome e a senha cadastrados previamente.

    Contas bancárias:
        O sistema oferece a possibilidade de criar contas correntes e contas poupança.
        A conta corrente possui um limite de saque de R$ 1000,00.
        O cliente pode realizar depósitos em suas contas.

    Operações bancárias:
        O sistema permite a realização de saques (com validação de saldo e limites) e depósitos em contas.

    Armazenamento de dados:
        Os dados do cliente e das contas são armazenados em um arquivo JSON, que é carregado e atualizado durante a execução do programa
        Estrutura do Código

O código é organizado em duas classes principais: Banco e Conta. A seguir, explicamos brevemente o funcionamento de cada classe.

Banco

    Atributos:
        clientes: Lista de clientes cadastrados no sistema.
        contas: Lista de contas bancárias.
    Métodos:
        autenticar(nome_cliente, senha_cliente): Verifica se o cliente existe e se a senha está correta.
        _checa_cliente(cliente): Verifica se um cliente está registrado no sistema.
        _checa_conta(conta): Verifica se uma conta está registrada no sistema.

Conta (Classe Abstrata)

A classe Conta é uma classe abstrata, o que significa que não pode ser instanciada diretamente. Ela serve como base para as classes ContaCorrente e ContaPoupanca.

    Atributos:
        numero_conta: Número da conta bancária.
        saldo: Saldo da conta.

    Métodos:
        sacar(valor): Método abstrato para realizar saques. Deve ser implementado pelas classes filhas.
        depositar(valor): Realiza o depósito de um valor na conta.

ContaCorrente

A classe ContaCorrente herda a classe Conta e implementa o método sacar com a verificação de limite de saque.

    Método:
        sacar(valor, limite): Realiza o saque, com a verificação do saldo e do limite de R$ 1000,00.

ContaPoupanca

A classe ContaPoupanca herda a classe Conta e implementa o método sacar para permitir saques, desde que haja saldo suficiente.

    Método:
        sacar(valor): Realiza o saque, verificando se há saldo suficiente na conta.

Cliente

A classe Cliente herda a classe Pessoa e representa um cliente do banco. Ela mantém as contas associadas ao cliente.

    Atributos:
        nome: Nome do cliente.
        senha: Senha do cliente.
        contas: Lista de contas do cliente.

Pessoa

A classe Pessoa é uma classe base que contém os atributos comuns a todas as pessoas, como nome e senha.

    Atributos:
        nome: Nome da pessoa.
        senha: Senha da pessoa.
