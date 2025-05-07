FICHEIROA="ficheiroa.txt"
FICHEIROB="ficheirob.txt"

with open(FICHEIROA,"r",encoding="utf-8") as ficheiro:
    f_a=ficheiro.readlines()
with open(FICHEIROB,"w",encoding="utf-8") as ficheiro:
    for teste in range(len(f_a)-1,-1,-1):
        ficheiro.write(f_a[teste])





