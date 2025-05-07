"""Fazer um programa que vai encontrar um programa que vai encontrar intruso"""
import os
FICHEIRO_TONDELA="tondela.txt"
FICHEIRO_ACADEMICO="academico.txt"


def socios_repetidos():
    #verificar se existem
    if os.path.exists(FICHEIRO_TONDELA) == False or os.path.exists(FICHEIRO_ACADEMICO) == False:
        return
    with open(FICHEIRO_TONDELA,"r",encoding="utf-8") as ficheiro:
        socios1=ficheiro.readlines()
    with open(FICHEIRO_ACADEMICO,"r",encoding="utf-8") as ficheiro:
        socios2=ficheiro.readlines()
    
    #remover \n
    for i in range(len(socios1)):
        socios1[i]= socios1[i].replace("\n","")
    for i in range(len(socios2)):
        socios2[i]= socios2[i].replace("\n","")
    encontra=False
    for socio in socios1:
        if socio in socios2:
            print(f"{socio} é socio dos dois clubes")
            encontra=True
    if encontra == False:
        print("Não existem sócios repetidos nos dois clubes")

socios_repetidos()

