FICHEIRO_LER="ficheiroa.txt"
FICHEIRO_ESCREVER="ficheirob.txt"


#Ler Ficheiro
with open(FICHEIRO_LER,"r",encoding="utf-8") as ficheiro:
    linhas=ficheiro.readlines()

#Escrever Ficheiro
with open(FICHEIRO_ESCREVER,"w",encoding="utf-8") as ficheiro:
    for i in range(len(linhas)-1,-1,-1):
        if linhas[i][len(linhas[i])-1] != "\n":
            linhas[i] += "\n"
        ficheiro.write(linhas[i])
print("Copia feita com sucesso")