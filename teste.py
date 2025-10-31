import os
os.system("cls")

texto = input("Digite seu nome: ")

nome_arquivo = "exemplo.txt"

with open(nome_arquivo, "w") as meu_arquivo:
    meu_arquivo.write(texto)
    print("Salvo com sucesso!")