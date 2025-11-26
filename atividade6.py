import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionário:
    nome: str
    data: str
    matricula: int
    endereco: str

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str

def exibir_dados_funcionarios():
    print ("===DADOS DOS FUNCIONÁRIOS===")
    nome_arquivo_1 = "dados_funcionarios.csv"
    with open(nome_arquivo_1, "a") as arquivo_funcionario:
        for funcionario in lista_de_funcionarios:
            arquivo_funcionario.write(f"{funcionario.nome},{funcionario.data},{funcionario.matricula},{funcionario.endereco}\n")
            print("Dados salvos com sucesso.")


def exibir_dados_clientes():
    print("===DADOS DOS CLIENTES===")
    nome_arquivo_2 = "dados_clientes.csv"
    with open(nome_arquivo_2, "a") as arquivo_cliente:
        for cliente in lista_de_clientes:
            arquivo_cliente.write(f"{cliente.nome},{cliente.nascimento},{cliente.endereco}\n")
            print("Dados salvos com sucesso.")

def exibir_dados_clientes_arquivo():
    print("===DADOS DOS CLIENTES===")
    nome_arquivo_2 = "dados_clientes.csv"
    with open(nome_arquivo_2, "a") as arquivo_cliente:
        for cliente in lista_de_clientes:
            arquivo_cliente.write(f"{cliente.nome},{cliente.nascimento},{cliente.endereco}\n")
            print("Dados salvos com sucesso.")




lista_de_funcionarios = []
lista_de_clientes = []    
  
QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionário(
        nome=input(f"Digite o nome do {i+1}° funcionário: "),
        data=input("Digite a data de admissão: "),
        matricula=int(input("Digite o n° da matricula: ")),
        endereco=input("Digite o endereço: ")
    )
    lista_de_funcionarios.append(funcionario)

    os.system("cls")

for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome=input("Digite o nome do cliente: "),
        nascimento=input("Digite o nascimento: "),
        endereco=input("Digite o endereço: ")
    )
    lista_de_clientes.append(cliente) 

    os.system("cls")

exibir_dados_clientes()
exibir_dados_funcionarios()   
ler_arquivo("dados_funcionarios.csv")




