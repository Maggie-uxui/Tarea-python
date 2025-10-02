
# 1)---------------------------------------

def esPar(numero):
  
    if numero % 2 == 0:
        return True   
      
    else:
        return False
    
n = int(input("Ingrese un número: "))

if esPar(n):
    print("El número es par")
  
else:
    print("El numero es impar")

# 2)---------------------------------------

def mayor(a, b, c):
  
    if a >= b and a >= c:
        print("El mayor es:", a)
      
    elif b >= a and b >= c:
        print("El mayor es:", b)
      
    else:
        print("El mayor es:", c)


x = int(input("Ingrese el primer número: "))

y = int(input("Ingrese el segundo número: "))

z = int(input("Ingrese el tercer número: "))

mayor(x, y, z)


# 3)---------------------------------------

def multiplos(n):
    contador = 0
  
    for i in range(1, n + 1):
      
        if i % 3 == 0:   
            contador = contador + 1
            
    print("Cantidad de múltiplos de 3 entre 1 y", n, "es:", contador)

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    multiplos(numero)
else:
    print("Debe ingresar un número positivo.")

# 4)---------------------------------------

def multiplicar(a, b):
    resultado = 0
    n = 0
    
    if b >= 0:
        while n < b:
            resultado += a
            n += 1
            
    else:
        while n > b:   
            resultado = resultado - a
            n = n - 1
    return resultado

x = int(input("Ingrese el primer número: "))

y = int(input("Ingrese el segundo número: "))

print("El resultado de", x, "*", y, "es:", multiplicar(x, y))

# 5)---------------------------------------

def potencia(a, b):
    resultado = 1
    
    for i in range(b):
        resultado = resultado * a   
        
    return resultado

numero = int(input("Ingrese un numero: "))

exponente = int(input("Ingrese el exponente: "))

print(numero, "^", exponente, "=", potencia(numero, exponente))

# 6)---------------------------------------

def primo (n):

    if n % n:
        print(n, "No es un número primo")
        return
    
    if n == 2:
        print(2, "Es un número primo")
        return
    
    for i in range(2 , n):
        if n % i == 0:

            print(n, "No es un número primo")
            return

    print(n, "Es un número primo")

numero = int(input("ingrese un número:"))

primo(numero)

#7)--------------------------------------------

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b   


opcion = 0

while opcion != 5:
    print("--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Elija una opción: "))

    if opcion == 5:
        print("Saliendo...")
        break

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print("Resultado:", sumar(a, b))
    elif opcion == 2:
        print("Resultado:", restar(a, b))
    elif opcion == 3:
        print("Resultado:", multiplicar(a, b))
    elif opcion == 4:
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")
      
#8)--------------------------------------------

def cuenta (n):

    if n < 1:
        print("Tiene que ser un número mayor o igual a 1")
        return

    for i in range(n,0,-1):
        print(i)

numero=int(input("Ingrese un número: "))

cuenta(numero)

#9)--------------------------------------------

def sumas(n):
    pares = 0
    impares = 0

    for a in range(1, n + 1):
        
        if a % 2 == 0:   
            pares = a + pares
        else:            
            impares = a + impares

    print("Suma de pares:", pares)
    print("Suma de impares:", impares)


numero = int(input("Ingrese un número entero positivo: "))

sumas(numero)

#10)--------------------------------------------

saldo = 1000  

opcion = 0

while opcion != 4:
    
    print("--- Cajero Automático ---")
    
    print("1. Depositar dinero")
    
    print("2. Retirar dinero")
    
    print("3. Mostrar saldo")
    
    print("4. Salir")
    
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto a depositar: $"))
        saldo = saldo + monto
        print("Depósito exitoso. Saldo actual: $", saldo)

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: $"))
        
        if monto <=  saldo:
            
            saldo = saldo - monto
            print("Retiro exitoso. Saldo actual: $", saldo)
        else:
            print("Fondos insuficientes. Saldo actual: $", saldo)

    elif opcion == 3:
        print("Su saldo actual es: $", saldo)

    elif opcion == 4:
        print("saliendo...")



