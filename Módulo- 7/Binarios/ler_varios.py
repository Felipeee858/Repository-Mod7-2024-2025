"""Programa para ler os dados de um ficheiro binario com o formato:
nome - 20s
idade - i
saldo - f"""
import struct
with open("Dados.bin","rb") as ficheiro:
    #ler os dados de todos de uma vez só
    dados_binarios=ficheiro.read(28)
    dados = struct.unpack("20sif",dados_binarios)

#converter string binario numa stri«ng
nome= dados[0].decode("utf-8").rstrip("\x00")
print("Nome:",nome)
print("Idade: ",dados[1])
print("Saldo: ",dados[2])