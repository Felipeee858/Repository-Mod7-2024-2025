with open("Exemplo.txt","r",encoding="utf-8") as ficheiro:
    teste=ficheiro.readlines()
    for t in teste:
        print(t)
    