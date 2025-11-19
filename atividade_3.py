import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}\n Idade: {self.nascimento}\n RG: {self.rg}\n CPF: {self.cpf}")

lista_de_dados = []
quantidade = 5

for i in range (quantidade):
    dados = Dados(nome=input("Digite o nome: "),
                  nascimento= input("Digite a data de nascimento: "),
                  rg=input("Digite o RG: "),
                  cpf=input("Digite seu CPF: "))
    os.system("cls")
    
    lista_de_dados.append(dados)
    print()

nome_arquivo = "funcionarios.csv"
with open(nome_arquivo, "a") as arquivo_dados:
    for dados in lista_de_dados:
        arquivo_dados.write(f"Nome: {dados.nome}\n Nascimento: {dados.nascimento}\n RG: {dados.rg} \n CPF: {dados.cpf}\n\n")
        print("Dados Salvos")

# print ("\n Exibir lista das pessoas")
# for dados in lista_de_dados:
# dados.exibir_dados()      

print("\nExibindo todos os dados: ")
try:
    with open (nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
     