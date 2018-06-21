arregloFibonacci = [1, 2]
contador = 1
suma = 0

while suma < 4000000:
    arregloFibonacci.append(arregloFibonacci[contador - 1] + arregloFibonacci[contador])
    if (arregloFibonacci[contador] % 2 == 0):
        suma = arregloFibonacci[contador] + suma
    contador += 1

print(suma)