import random
CULPADO="culpado.txt"
DESCULPA="desculpa.txt"
INTRO="intro.txt"
culpado=[]
desculpa=[]
intro=[]

with open(INTRO,"r",encoding="utf-8") as ficheiro:
    intro=ficheiro.readlines()

with open(CULPADO,"r",encoding="utf-8") as ficheiro:
    culpado=ficheiro.readlines()

with open(DESCULPA,"r",encoding="utf-8") as ficheiro:
    desculpa=ficheiro.readlines()


def aleatorio(lista):
    devolve=random.choice(lista)
    return devolve


def frase():
    Intro=aleatorio(intro)
    Culpado=aleatorio(culpado)
    Desculpa=aleatorio(desculpa)
    Intro=Intro.replace("\n"," ")
    Culpado=Culpado.replace("\n"," ")
    Desculpa=Desculpa.replace("\n"," ")
    print(f"{Intro}{Culpado}{Desculpa}")

frase()