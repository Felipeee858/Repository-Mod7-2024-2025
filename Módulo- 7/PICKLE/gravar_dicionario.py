"""Programa que grava um dicionario com o modulo pickle"""

import pickle
#ler dados
nome=input("Nome: ")
idade=int(input("Idade: "))
email = input("Email: ")

#criar dicionario
registo={
    "nome":nome,
    "idade":idade,
    "email":email
}

#guardar num ficheiro
with open("so_um.dat","ab",) as ficheiro:
    #serialização
    pickle.dump(registo,ficheiro) #dump guarda 
print("Dados adicionados")
