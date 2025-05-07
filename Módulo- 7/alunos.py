"""ficheiro=open("alunos.txt","w",encoding="UTF-8")

ficheiro.write("Olá Mundo\n")

ficheiro.write("Fim")

ficheiro.close()"""

#ou
with open("alunos.txt","w",encoding="UTF-8") as ficheiro:
    ficheiro.write("Olá Mundo\n")
    ficheiro.write("Fim")
    
