import os
NOME_FICHEIRO="nomes.txt"
if os.path.exists(NOME_FICHEIRO)==False:
    print("O ficheiro não existe")
else:
    with open("nomes.txt","r",encoding="UTF-8") as ficheiro:
        linhas=ficheiro.readlines()

    for linha in linhas:
        print(linha)
        

    #versão
    with open("nomes.txt","r",encoding="UTF-8") as ficheiro:
        while True:
            linha=ficheiro.readlines()
            #verificar se encontrou o fim do ficheiro (EDF)
            if not linha:
                break
            print(linha,end="") 