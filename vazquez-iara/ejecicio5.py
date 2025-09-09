# 1)------------------------------------------------------

contador=0
numero=int(input("Ingrese un número: "))
while numero != 0:
    contador= contador + 1 
    numero= int(input("Ingrese un número: "))
print("La cantidad de números ingresados es:", contador)

#2)------------------------------------------------------

suma=0
numero= int(input("Ingrese un número: "))
while numero !=0:
    suma= suma + numero
    numero= int(input("Ingrese un número: "))

print("La suma de los números ingresados es:", suma)

# 3)------------------------------------------------------

suma=0
contador=0
numero = int(input("Ingrese un número: "))
while numero != 0:
    suma =suma + numero         
    contador = contador + 1          
    numero = int(input("Ingrese un número: "))
    
if 1 <= numero <= 10:  
    promedio = suma / contador
    print("El promedio de los números ingresados es:", promedio)

else:
    print("Número inválido. Debe estar entre 1 y 10.")
    
numero = int(input("Ingrese un número entre 0 y 10: "))

if contador > 0:
    promedio = suma / contador
    print("El promedio de los números ingresados es:", promedio)
    
else:
    print("No se ingresaron números válidos.")


# 4)------------------------------------------------------

numero = int(input("Ingrese un número: "))

if numero == 0:
    print("No se ingresaron números.")
else:
    mayor = numero
    numero = int(input("Ingrese un número: "))

    while numero != 0:
        if numero > mayor:
            mayor = numero
        numero = int(input("Ingrese un número: "))

    print("El mayor número ingresado es:", mayor)
