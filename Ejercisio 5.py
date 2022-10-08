def es_bisiesto(ano):
	return not ano % 4 and (ano % 100 or not ano % 400)

print("Escriba el año")
ano = int(input())

if es_bisiesto(ano)==True:
	print("bisiesto")
else:
	print("no bisiesto")
