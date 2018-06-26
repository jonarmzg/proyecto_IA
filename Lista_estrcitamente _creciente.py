entrada = input()
arregloModificado = []     
arreglo2=[]
for elemento in entrada.split(","):
    elementoSinEspacio = elemento.replace(' ', '')
    if elementoSinEspacio != '':
        arregloModificado.append(int(elementoSinEspacio))
for lo in entrada.split(","):
    elementsin = lo.replace(' ', '')
    if elementsin != '':
        arreglo2.append(int(elementsin))
        
        
arregloModificado.sort()

if arreglo2== arregloModificado:
    print(True)
else:
    print(False)
    

