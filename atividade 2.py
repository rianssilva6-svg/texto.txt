import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    autor: str
    categoria: str
    preco: str

informacao=Dados(nome=input("Digite seu nome: "),
                 autor=input("Digite o nome do autor: "),
                 categoria=input("Digite a categoria do livro: "),
                 preco=input("Digite o valor R$: "))    

arquivo = "dados_livros.txt"

with open (arquivo, "a") as arquivo_dados:
        arquivo_dados.write(f"Nome: {informacao.nome}, Autor: {informacao.autor}, Categoria: {informacao.categoria}, Valor: R${informacao.preco}\n")
        print("salvo com sucesso")