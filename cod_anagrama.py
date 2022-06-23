# # Codificando letras para numeros (ordem alfabetica)
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# h = 8
# i = 9
# j = 10
# k = 11
# l = 12
# m = 13
# n = 14
# o = 15
# p = 16
# q = 17
# r = 18
# s = 19
# t = 20
# u = 21
# v = 22
# w = 23
# x = 24
# y = 25
# z = 26

# Importanto as bibliotecas necessarias
from itertools import permutations
from unittest import skip

# Inserindo a palavra que sera usada para gerar os anagramas
palavra = input('Digite uma palavra :')

# Definindo o tamanho da palavra
tamanho_palavra = int(input('Com quantos algarismos quer o anagrama? '))

# Separando as letras da palavra em uma lista
letras = sorted(palavra)

# Removendo espaços vazios na lista de letras
while ' ' in letras:
    letras.remove(' ')
print(letras)

# Fazendo leitura do dicionario 
lista_de_palavras = open('dicionario_pt-br.txt', "r", encoding='utf-8')
dicionario = []
for line in lista_de_palavras:
    dicionario.append(line.strip())


# criando permutacoes da palavra digitada
resultado = []
resultado_real = []

possibilidades = permutations(letras,tamanho_palavra)
for i in list(possibilidades):
    if i not in resultado:    
        resultado.append(i)
    else: 
        skip
print('Total de possibilidades: ' + str(len(resultado)))

for i in resultado:
    if i in dicionario:
       resultado_real.append(i)
    else:
       skip
    resultado_real.append(i)
print('Total de possibilidades reais: ' + str(len(resultado_real)))