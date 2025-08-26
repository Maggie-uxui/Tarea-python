edad=int(input("Ingrese su edad: "))
if edad >=16:
    print("Puedes votar")
else:
    print("No puedes votar")
    

total=float(input("Ingrese su monto total de compra:$"))
if total >=5000:
    print("Tenés un 10% de descuento")
else:
    print("Sin descuento")


promedio=float(input("Ingrese su promedio:"))
if 11> promedio >=7:
    print("Obtienes una beca")
else:
    print("No puede obtener una beca, su promedio debe ser mayor a 7 y menos a 10")