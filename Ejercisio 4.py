contador = 0
lista = []


while contador <= 99:
	contador+=1
	lista.append(contador)

Ordenada = sorted(lista,reverse=True)

for x in Ordenada:
	print(x)