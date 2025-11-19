import os 
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")

lista_de_paciente = []
QUANTIDADE_DE_PACIENTES = 2

for i in range (QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome=input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_de_paciente.append(paciente)
    print() #pula uma linha

nome_do_arquivo = "dados_pacientes.txt"
with open(nome_do_arquivo, "a") as arquivo_paciente:
    for paciente in lista_de_paciente:
        arquivo_paciente.write (f"{paciente.nome}, {paciente.idade}")
        print("Dados salvos")

# print("\nExibindo lista de pacientes:")
# for paciente in lista_de_paciente:
# paciente.exibir_dados()    

lista = []
try:
    with open(nome_do_arquivo, "r") as arquivo:
        lista_de_todos_paciente = arquivo.readline()
        for paciente in lista_de_todos_paciente:
            nome, idade = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados() 
except FileNotFoundError:
    print("O arquivo não foi encontrado.")               