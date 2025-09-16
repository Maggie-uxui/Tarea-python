
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

