import os
os.system("cls")

def exibir_dados_funcionarios():
    print("=== DADOS DOS FUNCIONÁRIOS ===")

    nome_arquivo = "dados_funcionarios.csv"

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, data_adm, matricula, endereco = linha.strip().split(",")

                print(f"Nome: {nome}")
                print(f"Data de admissão: {data_adm}")
                print(f"Matrícula: {matricula}")
                print(f"Endereço: {endereco}")
                print("-" * 30)

    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")


def exibir_dados_clientes():
    print("=== DADOS DOS CLIENTES ===")

    nome_arquivo = "dados_clientes.csv"

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, data_nasc, endereco = linha.strip().split(",")

                print(f"Nome: {nome}")
                print(f"Data de nascimento: {data_nasc}")
                print(f"Endereço: {endereco}")
                print("-" * 30)

    except FileNotFoundError:
        print("Arquivo de clientes não encontrado.")        

exibir_dados_funcionarios()        
exibir_dados_clientes()