# Codificando letras para numeros (ordem alfabetica)
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

# Importanto as bibliotecas necessarias
from itertools import permutations

# Inserindo a palavra que sera usada para gerar os anagramas
palavra = input('Digite uma palavra :')

# Definindo o tamanho da palavra
tamanho_palavra = int(input('Com quantos algarismos quer o abagrama? '))

# Separando as letras da palavra em uma lista
letras = sorted(palavra)
print(letras)

# criando permutacoes da palavra digitada
possibilidades = permutations(letras,tamanho_palavra)
for i in list(possibilidades):
    print(i)
