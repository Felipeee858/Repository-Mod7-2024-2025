import csv

#lista vazia para guardar os dados do ficheiro
dados=[]

#abrir ficheiro para leitura
with open("ficheiro.csv","r",encoding="utf-8") as ficheiro:
    #criar o objeto para ler o csv
    ler = csv.DictReader(ficheiro)
    print("ler",ler)
    #ler cada linha do ficheiro e adicionar a lista
    n=0
    for linha in ler:
        n+=1
    print(n)
print(dados)