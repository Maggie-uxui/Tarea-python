# celsius=float(input("Ingresar la temperatura en grados Celsius: "))
# fahrenheit=(celsius * 9/5) + 32
# print("La temperatura en Fahrenheit es:", fahrenheit)


# def calcular_perimetro(lado):
#     return 4 * lado

# def calcular_superficie(lado):
#     return lado * lado 

# lado=float(input("Ingrese el valor del lado del cuadrado: "))

# perimetro=calcular_perimetro(lado)
# superficie=calcular_superficie(lado)

# print("El Perímetro del cuadrado es: ",perimetro)
# print("La superficie del cuadrado es: ",superficie)


# def doble(x):
#     return 2 * x

# x=float(input("Ingrese el número que desea multiplicar: "))
# multiplicar=doble(x)

# print("El doble de su numero es: ",multiplicar)


# 1-preguntarle la edad al usuario e informoar si puede votar o no


def verficar_edad(edad):

    if edad >=18:
     return (print("Puedes votar"))
    
    else:
      return print("No puedes votar") 

edad=int(input("Ingrese su edad: "))
resultado=verficar_edad(edad)
print(resultado)
