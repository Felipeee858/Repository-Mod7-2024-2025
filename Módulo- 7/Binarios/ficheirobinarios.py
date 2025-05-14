import struct
import os
TAMANHO_REGISTRO=39
FICHEIRO="Pets.dat"
def Adicionar():
    raça=input("Introduza a raça: ")
    peso=float(input("Introduza o Peso: "))
    genero=input("Introduza o genero: ")
    preço=float(input("Introduza o preço: "))
    with open(FICHEIRO,"ab") as ficheiro:
        dados=struct.pack("30s",raça.encode("utf-8"))
        ficheiro.write(dados)
        dados=struct.pack("f",peso)
        ficheiro.write(dados)
        dados=struct.pack("1s",genero.encode("utf-8"))
        ficheiro.write(dados)
        dados=struct.pack("f",preço)
def ListarTodos():
    if os.path.exists(FICHEIRO) == False:
        print("Ainda não tem dados")
        return
    with open (FICHEIRO,"rb") as ficheiro:
        while True:
            #raça
            dados_binario= ficheiro.read(30)
            if not dados_binario:
                break
            #raça
            dados=struct.unpack("30s",dados_binario)
            print("Raça:",dados[0].decode("utf-8").rstrip("\x00"))
            #peso
            dados_binario= ficheiro.read(4)
            dados=struct.unpack("f",dados_binario)
            print("Peso:",dados[0])
            #genero
            dados_binario= ficheiro.read(1)
            dados=struct.unpack("1s",dados_binario)
            print("Genero:",dados[0].decode("utf-8").rstrip("\x00"))
            #preço
            dados_binario=ficheiro.read(4)
            dados=struct.unpack("f",dados_binario)
            print("Preço:",dados[0])

        
def Apagar():
    with open(FICHEIRO,"rb") as f_ler:
        #criar um ficheiro temporario
        with open("temp.bin","wb") as f_escrever:
            while True:
                raca_binario=f_ler.read(30)
                if not raca_binario:
                    break
            #ler um registo
            peso_binario=f_ler.read(4)
            genero_binario=f_ler.read(1)
            preco_binario=f_ler.read(4)
            raca=struct.unpack("30s",raca_binario)
            #mostrar ao utilizar
            print("Raça: ",raca[0].decode("utf-8").rstrip("\x00"))
            #se NÃO é para apagar gravar no ficheiro temp
            op=input("Pretende apagar este animal? ")
            if op not in "sS":
                f_escrever.write(raca_binario)
                f_escrever.write(peso_binario)
                f_escrever.write(genero_binario)
                f_escrever.write(preco_binario)
    #apagar o ficheiro de dados
    os.remove(FICHEIRO)
    #mudar o nome do ficheiro temporario
    os.rename("temp.bin",FICHEIRO)
    print("Animal removido com sucesso")
def Editar():
    #Abrir o ficheiro para leitura e escrita
    with open(FICHEIRO,"rb+") as ficheiro:
        while True:
            #ler um registo
            raca_binario=ficheiro.read(30)
            if not raca_binario:
                break
            peso_binario=ficheiro.read(4)
            genero_binario=ficheiro.read(1)
            preco_binario=ficheiro.read(4)
            #mostrar ao utilizador
            raca=struct.unpack("30s",raca_binario)[0]
            peso=struct.unpack("f",peso_binario)[0]
            genero=struct.unpack("1s",genero_binario)[0]
            preco=struct.unpack("f",preco_binario)[0]
            genero=genero.decode("utf-8").rstrip("\x00")
            preco=struct.unpack("f",preco_binario)[0]
            print("Pretende editar este animal? ")
            print(f"{raca} - {peso} - {genero} - {preco}")
            #perguntar se quer alterar
            op=input("Deseja alterar (S/N) ? ")
            if op in "sS":
                raca=input("Raça: ")
                peso=float(input("Peso: "))
                genero=input("Genero: ")
                preco=float(input("Preço: "))
                #se alterar gravar novamente o mesmo registo
                ficheiro.seek(-39,os.SEEK_CUR)
                ficheiro.write(struct.pack("30s",raca.encode("utf-8")))
                ficheiro.write(struct.pack("f",peso))
                ficheiro.write(struct.pack("1s",genero.encode("utf-8")))
                ficheiro.write(struct.pack("f",preco))

def Animalcaro():
    with open(FICHEIRO,"rb") as ficheiro:
        while True:
            preco_binario=ficheiro.read(4)
            if not preco_binario:
                break
            dados=struct.unpack("f",dados_binario)
            print("Preço:",dados[0])


       
def Menu():
    op=0
    while op !=5:
        op=int(input("1.Adicionar\n2.Listar Todos\n3.Apagar\n4.Editar\n5.Animalcaro\n6.Sair"))
        if op ==1:
            Adicionar()
        if op == 2:
            ListarTodos()
        if op==3:
            Apagar()
        if op==4:
            Editar()
        if op ==5:
            Animalcaro()
        if op == 6:
            break

if __name__=="__main__":
    Menu()