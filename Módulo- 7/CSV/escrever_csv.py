lista=[
    {"nome":"Joaquim",
        "morada":"Viseu",
        "idade":30},

    {"nome":"Maria",
        "morada":"Satão",
        "idade":25}
]

#ler e escrever em ficheiros de texto de formato csv
import csv

#cabeçalho do ficheiro csv
chaves=lista[0].keys()

with open("ficheiro.csv","w",encoding="utf-8",newline="") as ficheiro:
    #variável para gravar no ficheiro (ficheiro,campos do dicionario)
    escrever = csv.DictWriter(ficheiro,fieldnames=chaves)
    #gravar o cabeçalho
    escrever.writeheader()
    for i in range(len(lista)):
        escrever.writerow(lista[i]) #grava os dados correspondentes as chaves
