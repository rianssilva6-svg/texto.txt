from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Dados:
    nome: str
    idade: str
    telefone: str
    email: str

QUANTIDADE_PESSOAS = 2
lista_pessoas = []

for i in range (QUANTIDADE_PESSOAS):
    pessoa = Dados(nome=input("Digite seu nome: "),
                   idade = input("Digite sua idade: "),
                   telefone = input("Digite seu telefone: "),
                   email = input("Digite seu email: "))
    os.system("cls")
    lista_pessoas.append(pessoa)

print()
print("===Salvando dados===")
arquivo = "dados_pessoas.txt" 

with open (arquivo, "a") as arquivo_dados:
    for pessoa in lista_pessoas:
        arquivo_dados.write(f"{pessoa.nome}, {pessoa.idade}, {pessoa.telefone}, {pessoa.email}\n")
        print("salvo com sucesso")