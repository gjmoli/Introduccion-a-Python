numeros=[]

menor=numeros[0]
mayor=numeros[0]

for i in range (0,len(numeros)):
    if numeros[i]<menor:
        menor=numeros[i]
print("El número menor es: ", menor)

for i in range (0,len(numeros)):
    if numeros[i]>mayor:
        mayor=numeros[i]
print("El número mayor es: ", mayor)
