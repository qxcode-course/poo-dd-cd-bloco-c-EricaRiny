class teste:

    def __init__(self, x: int):
        self.x = x
    
    def __str__(self):
        return f"teste({self.x})"
    
lista_obj: list[teste] = [teste(1), teste(9), teste(10)]
    
lista_vazia: list[int] = []
print(f"Lista vazia: {lista_vazia}")

lista_vazia.append(10)
print(f"append na lista vazia: {lista_vazia}")

lista_preenchida: list[int] = [3, 4, 1, 10]
print(f"lista preenchida: {lista_preenchida}")

tamanho = len(lista_preenchida)
print(f"tamanho da lista preenchida: {tamanho}")

lista_preenchida.pop()
print(f"removendo final de lista preenchida: {lista_preenchida}")

lista_preenchida.append(2)
print(f"adicionando no final {lista_preenchida}")

lista_preenchida.pop(0)
print(f"removendo do inicio: {lista_preenchida}")

lista_preenchida.insert(0,1)
print(f"adicionando no inicio: {lista_preenchida}")

lista_preenchida.pop(3)
print(f"removendo em posição específica: {lista_preenchida}")

lista_preenchida.insert(1, 0)
print(f"adicionando em posição específica: {lista_preenchida}")

listaObj = "-".join([str(x) for x in lista_obj])
print(f"impressão formatada: {listaObj}")

n = 20
listaSeq = list(range(n+1))
print(f"lista sequencia: {listaSeq}")

import random
listaAleatoria = [random.randint(1,200) for lista in range(10)]
print(f"lista aleatória: {listaAleatoria}")

acessar=listaAleatoria[3]
print(f"acessando por indice: {acessar}")

for i in range(len(listaAleatoria)):
    print(f"o elemento no indice {i} é {listaAleatoria[i]}")

for i in listaAleatoria:
    if i == 41:
        print(f"procurando elemento X: numero {i} está na lista")

i=1
if i in lista_preenchida:
    print(f"procurando: o numero {i} esta na lista")

pares = []
for i in listaAleatoria:
    if i % 2 == 0:
        pares.append(i)
print(f"filtrando pares:{pares}")

quadrados = []
for i in listaAleatoria:
    i = i*i
    quadrados.append(i)
print(f"transformando ao quadrado: {quadrados}") 

x=4
if x in lista_preenchida:
    lista_preenchida.remove(x)
    print(f"procurando e removendo 4: {lista_preenchida}")

x= 1
for x in lista_preenchida:
    lista_preenchida.remove(x)
print(f"removendo todos os 1: {lista_preenchida}")