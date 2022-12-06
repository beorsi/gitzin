import os
os.system("cls")
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
# filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
ímpares = [numero for numero in numeros if numero % 2 != 0]
print(ímpares)
# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
