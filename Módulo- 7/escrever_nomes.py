"""Programa para ler 10 nomes e escrever num ficheiro"""

"""f=open("nomes.txt","w",encoding="UTF-8")

f.close()"""

with open("nomes.txt","a",encoding="UTF-8") as ficheiro:
    for _ in range(10):
        nome=input("Introduza um nome: ")
        ficheiro.write(nome)
        ficheiro.write("\n")
print("Ficheiro criado com sucesso")