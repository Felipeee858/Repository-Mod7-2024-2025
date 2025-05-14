string=input("Introduza: ")

with open("dados.txt","a",encoding="utf-8") as ficheiro:
    ficheiro.write(string+"\n")
