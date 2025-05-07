"""
Programa para verificar uma frase utilizando um ficheiro de texto como dicionario"""

import os
FICHEIRO="words_alpha.txt"

def FicheiroExiste():
    if os.path.exists(FICHEIRO) == False:
        print("Dicionario não existe")
        return False
    return True

def LerFrase():
    "Função para ler uma frase do utilizador e devolver uma lista de palavras"
    texto=input("Introduza uma frase: ")
    texto=texto.strip().lower()
    return texto.split(" ")


def LerFicheiro():
    "Função para ler todas as linhas de um ficheiro de texto e devolver uma lista"
    with open(FICHEIRO,"r",encoding="utf-8") as ficheiro:
        linhas=ficheiro.readlines()
    for i in range(len(linhas)):
        linhas[i]= linhas[i].replace("\n","")
    return linhas

def Verificar(palavras,dicionario):
    """ Função recebe as palvaras a verificar e a lista de palavras do dicionario. Mostra as palvras que não existem no dicionario ou uma
    mensagem de não existencia de erros"""
    erro=False
    for palavra in palavras:
        if palavra not in dicionario:
            print(f"A palavra {palavra} não existe ou está errada")
            erro=True
    if erro == False:
        print("A frase não tem erros")
    

def main():
    if FicheiroExiste()==False:
        print("Não encontrei o ficheiro com o dicionario")
        return
    palavras=LerFrase()
    dicionario=LerFicheiro()
    Verificar(palavras,dicionario)

if __name__=="__main__":
    main()


            



