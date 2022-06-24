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

# # Fazendo leitura do dicionario 
# lista_de_palavras = open('dicionario_pt-br.txt', "r", encoding='utf-8')
# dicionario = []
# for line in lista_de_palavras:
#     dicionario.append(line.strip())
# # print(dicionario[4])


# criando permutacoes da palavra digitada
resultado = []
possibilidades = permutations(letras,tamanho_palavra)
for i in list(possibilidades):
    if i not in resultado:    
        resultado.append(i)
    else: 
        skip
print('Total de possibilidades: ' + str(len(resultado)))
if 'amar' in resultado:
    print('SIIIIIIM')
else:
    print('NAO')
print(resultado)

# resultado_real = []
# for x in resultado:
#     if x in dicionario:
#        resultado_real.append(x)
#     else:
#        skip
# print('Total de possibilidades reais: ' + str(len(resultado_real)))