"""
Crie um programa que pede ao usuário para digitar seu nome e idade, e então salva essas informações em um ficheiro chamado dados.txt.
"""

idade=int(input("Idade: "))
nome=input("Nome: ")
idade=str(idade)

with open("dados_gpt.txt","a",encoding="utf-8") as ficheiro:
    ficheiro.write(idade+"\n")
    ficheiro.write(nome+"\n")

"""
Crie um programa que leia e imprima o conteúdo do ficheiro dados.txt (criado no exercício anterior).
"""

with open("dados_gpt.txt","r",encoding="utf-8") as ficheiro:
    f=ficheiro.readlines()
    for i in range(len(f)-1):
        print(f[i])