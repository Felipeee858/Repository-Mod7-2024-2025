"""Programa para criar um ficheiro com produtos e preços"""
NOME_FICHEIRO="produtos.txt"
import os


def Ficheiroexiste():
    if os.path.exists(NOME_FICHEIRO)==False:
        print("O ficheiro não existe")
        return False
    return True
def AdicionarProdutos():
    with open(NOME_FICHEIRO,"a",encoding="utf-8") as ficheiro:
        nome=input("Nome: ")
        preço=float(input("Preço: "))
        linha= f"{nome} - {preço}\n"
        ficheiro.write(linha)

def LerProdutos():
    if Ficheiroexiste==False:
        print("O ficheiro não existe")
        return
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        while True:
            linha = ficheiro.readline()
            if not linha:
                break
            partes=linha.split("-")
            nome=partes[0].strip()
            preco=float(partes[1].strip())
            print(f"Produto: {nome} Preço {preco}€")

def EditarProdutos():
    #verificar se existe o ficheiro
    if Ficheiroexiste()==False:
        return
    #ler nome do produto a editar
    nome=input("Qual o produto que pretende editar? ")
    #abrir o ficheiro dos produtos para ler
    ficheiro_ler=open(NOME_FICHEIRO,"r","utf-8")
    #abrir ficheiro temporário para escrever
    ficheiro_escrever=open(NOME_FICHEIRO,"temp.txt","w",encoding="utf-8")
    while True:
        #ler um produto
        linha=ficheiro_ler.readline()
        if not linha:
            break
        #verificar se é o produto a editar
        partes=linha.split("-")
        if nome == partes[0].strip():
            #se sim ler os novos dados
            novo_nome=input("Novo nome para o produto: ")
            novo_preco=float(input("Novo preço para o produto: "))
            linha=f"{novo_nome} - {novo_preco}"
        #gravar no ficheiro temporário
        ficheiro_escrever.write(linha)
    #fechar os dois ficheiros
    ficheiro_ler.close()
    ficheiro_escrever.close()
    #apagar o ficheiro produtos
    os.remove(NOME_FICHEIRO)
    #mudar o nome do ficheiro temporário para produtos
    os.rename("temp.txt",NOME_FICHEIRO)
    print("Produto editado com sucesso")
    

def ApagarProdutos():
    #verificar se existe o ficheiro
    if Ficheiroexiste()==False:
        return
    #ler nome do produto a editar
    nome=input("Qual o produto que pretende editar? ")
    #abrir o ficheiro dos produtos para ler
    ficheiro_ler=open(NOME_FICHEIRO,"r","utf-8")
    #abrir ficheiro temporário para escrever
    ficheiro_escrever=open(NOME_FICHEIRO,"temp.txt","w",encoding="utf-8")
    while True:
        #ler um produto
        linha=ficheiro_ler.readline()
        if not linha:
            break
        #verificar se é o produto a editar
        partes=linha.split("-")
        if nome == partes[0].strip():
            continue
        #gravar no ficheiro temporário
        ficheiro_escrever.write(linha)
    #fechar os dois ficheiros
    ficheiro_ler.close()
    ficheiro_escrever.close()
    #apagar o ficheiro produtos
    os.remove(NOME_FICHEIRO)
    #mudar o nome do ficheiro temporário para produtos
    os.rename("temp.txt",NOME_FICHEIRO)
    print("Produto apagado com sucesso")
def Menu():
    op=0
    while op !=5:
        print("1.Adicionar\n2.Ler\n3.Editar\n4.Apagar\n5.Sair")
        op=int(input("Introduza a opção: "))
        if op ==1:
            AdicionarProdutos()
        if op==2:
            LerProdutos()
        if op==3:
            EditarProdutos()
        if op==4:
            ApagarProdutos()
        if op==5:
            break


if __name__=="__main__":
    Menu()