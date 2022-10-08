import math

print("Ingrese su peso en Kg")

peso = int(input())

print("Ingrese su estatura en metros")

altura  = float(input())

IMC = peso /altura**2

print("Tu índice de masa corporal es: "+ str(round(IMC, 2)))