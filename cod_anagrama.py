# Importanto as bibliotecas necessarias
from itertools import permutations
from unittest import skip

# Inserindo a palavra que sera usada para gerar os anagramas
palavra = input('Digite uma palavra :')


# Definindo o tamanho da palavra
tamanho_palavra = int(input('Com quantos algarismos quer o anagrama? '))


# Separando as letras da palavra em uma lista
letras_sep = sorted(palavra)


# Removendo espaços vazios na lista de letras
while ' ' in letras_sep:
    letras_sep.remove(' ')
print(letras_sep)
letras = ''.join(letras_sep)
letras = str(letras)


# Fazendo leitura do dicionario 
lista_de_palavras = open('dicionario_pt-br.txt', "r", encoding='utf-8')
dicionario = []
for line in lista_de_palavras:
    dicionario.append(line.strip())


# criando permutacoes da palavra digitada
resultado = []
def anagrama(x):
    possibilidades = permutations(letras,tamanho_palavra)
    for i in possibilidades:
        if i not in resultado:
            i = ''.join(i)
            resultado.append(i)
        else:
            skip
x = letras
anagrama(x)
print('Total de possibilidades: ' + str(len(resultado)))


resultado_real = []
for x in resultado:
    if x in dicionario:
       resultado_real.append(x)
    else:
       skip
print('Total de possibilidades reais: ' + str(len(resultado_real)))
print(resultado_real)