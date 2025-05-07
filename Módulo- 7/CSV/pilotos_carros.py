"""Programa para ler e guardar dados em ficheiros csv para carros e pilotos de corrida
carros.csv : marca, modelo, matricula
pilotos.csv : nome, idade, pais

Funcionalidades:
    Adicionar: carros, pilotos
    Listar : carros, pilotos
    Pesquisar : Pilotos de um carro, carro de um piloto

"""
import csv
import os

FICHEIRO_PILOTOS="pilotos.csv"
FICHEIRO_CARROS="carros.csv"

carros=[]

pilotos=[]

def LerFicheiro(nome_ficheiro):
    """Função para ler ficheiro csv e devolver uma lista com os dados"""
    #lista vazia para guardar os dados do ficheiro
    dados=[]
    #verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro)==False:
        print("O ficheiro não existe")
        return dados
    #abrir ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        #criar o objeto para ler o csv
        ler = csv.DictReader(ficheiro)
        #ler cada linha do ficheiro e adicionar a lista
        for linha in ler:
            dados.append(linha)
    #devolver a lista com os dados do ficheiro
    return dados
def Escrever(lista,nome):
    """Função para escrever os dados de uma lista num ficheiro csv"""
    chaves=lista[0].keys()
    with open(nome,"w",encoding="utf-8",newline="") as ficheiro:
        #variável para gravar no ficheiro (ficheiro,campos do dicionario)
        escrever = csv.DictWriter(ficheiro,fieldnames=chaves)
        #gravar o cabeçalho
        escrever.writeheader()
        for i in range(len(lista)):
            escrever.writerow(lista[i]) #grava os dados correspondentes as chaves


def ValidarMatricula(matricula):
    """Devolve True se a matricula existe ou False se não existe"""
    for carro in carros:
        if carro["matricula"] == matricula:
            return True
        return False

def ValidarNrMatricula(matricula):
    """Devolve o número de pilotos de um carro"""
    contar=0
    for p in pilotos:
        if p["matricula"] == matricula:
            contar += 1
    return contar


def Adicionar():
    pergunta=input("Deseja Adicionar um piloto (P) ou um carro (C)? ")
    if not pergunta:
        return
    if pergunta.lower() in "c":
        #ler os dados do carro
        marca=input("Introduza a marca: ")
        modelo=input("Introduza o modelo: ")
        matricula=input("Introduza a matricula: ")
        if ValidarMatricula(matricula) == True:
            print("Matricula já existe")
        #criar um dicionario
        ex={"marca":marca,
         "modelo":modelo,
         "matricula":matricula}
        #adicionar à lista
        carros.append(ex)
        #escrever no ficheiro dos carros
        Escrever(carros,FICHEIRO_CARROS)
    if pergunta.lower() in "p":
        #ler os dados do piloto
        matricula=input("Introduza a matricula: ")
        if ValidarMatricula(matricula) == False:
            print("Matricula introduzida não existe")
            return
        if ValidarNrMatricula(matricula) >=2:
            print("Já existe 2 pilotos no carro")
            return
        nome=input("Introduza o nome: ")
        idade=int(input("Introduza a idade: "))
        pais=input("Introduza o país: ")
        #criar um dicionario
        ex={"nome":nome,
         "idade":idade,
         "pais":pais,
         "matricula":matricula}
        #adicionar à lista
        pilotos.append(ex)
        #escrever no ficheiro dos pilotos
        Escrever(pilotos,FICHEIRO_PILOTOS)
        print("Piloto foi adicionado com sucesso")
        

def Listar():
    pergunta=input("Deseja Listar um piloto (P) ou um carro (C)? ")
    if pergunta.lower() in "c":
        print(carros)
    if pergunta.lower() in "p":
        print(pilotos)
def Pesquisar():
    matricula=input("Qual a matrícula do carro a pesquisar: ")
    if matricula:
        #mostrar os pilotos do carro
        for p in pilotos:
            if p["matricula"] == matricula:
                print(f"Piloto: {p}")
    piloto=input("Qual o nome do piloto a pesquisar: ")
    if piloto:
        #mostrar o carro do piloto
        for p in pilotos:
            if p["nome"] == piloto:
                for c in carros:
                    if p["matricula"] == c["matricula"]:
                        print(f"Carro do piloto: {c}")
                
def Menu():
    global carros
    global pilotos
    carros=LerFicheiro(FICHEIRO_CARROS)
    pilotos=LerFicheiro(FICHEIRO_PILOTOS)
    op=0
    while op != 4:
        op=int(input("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Sair\nIntroduza a opção: "))
        if op == 4:
            break
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Pesquisar()
            
if __name__=="__main__":
    Menu()
