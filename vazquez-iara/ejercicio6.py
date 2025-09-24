#3) y 4)--------------------

colores=[]
nuevo_color=[]

for a in range(0,10):
    colores.append(input("Ingrese un color: "))

for a in range(0,10):
    print(colores[a])
    
nuevo_color=input("Ingrese un nuevo color: ")

encontrado = False

for color in colores:
    if color == nuevo_color:
        encontrado = True
        break

if encontrado:
    
     print("El color", nuevo_color, "ya se encuentra en la lista")
     
else:
    
    print("El color ", nuevo_color, " se ha agregado a la lista")

#6)-----------------------------

numeros = [4, 98, 257, -85, 0, 21, -582, 148, -293]

mayor = numeros[0]   

for a in range(len(numeros)):   
    if numeros[a] > mayor:      
        mayor = numeros[a]
print("El número mayor es:", mayor)

suma = 0
for a in range(len(numeros)):
    suma =suma + numeros[a]
print("La suma de los números es:", suma)

positivos = 0
for a in range(len(numeros)):
    if numeros[a] > 0:
        positivos = positivos + 1
print("La cantidad de números positivos es:", positivos)

pares = []
for a in range(len(numeros)):
    if numeros[a] % 2 == 0:
        pares.append(numeros[a])
print("Los números pares son:", pares)

