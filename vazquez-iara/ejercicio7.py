alumnos=[]

def agregar_alumno():
   nombre = input("Ingrese el nombre del alumno: ")
   edad = input("Ingrese la edad del alumno: ")
   calificacion = input("Ingrese la calificación del alumno: ")
   alumno={"nombre": nombre, "edad": edad, "calificacion": calificacion}
   alumnos.append(alumno)
   print(" Alumno agregado exitosamente.")
   
def modificar_alumno():
    
    nombre = input("Ingrese el nombre del alumno a modificar: ")
    
    for j in range(len(alumnos)):
        
        if alumnos[j]["nombre"] == nombre:
            
            print("Alumno encontrado. Ingrese los nuevos datos:")
            
            alumnos[j]["nombre"] = input("Nuevo nombre: ")
            alumnos[j]["edad"] = input("Nueva edad: ")
            alumnos[j]["calificacion"] = input("Nueva calificación: ")
            
            print(" Alumno modificado exitosamente.")
            return
        
    print(" Alumno no encontrado.")


def eliminar_alumno():
    
    nombre = input("Ingrese el nombre del alumno a buscar: ")
    
    for j in range(len(alumnos)):
        
        if alumnos[j]["nombre"] == nombre:
            alumnos.pop(j)
            print(" Alumno eliminado exitosamente.")
            return
        
    print(" Alumno no encontrado.")

def listar_alumnos():
    if len(alumnos) == 0:
        print(" No hay alumnos registrados.")
    else:
        print("Lista de alumnos:")
        
        for j in range(len(alumnos)):
            print(f"Nombre: {alumnos[j]['nombre']}, Edad: {alumnos[j]['edad']}, Calificación: {alumnos[j]['calificacion']}")

   

while True:
    print("------ MENÚ ------")
    print("1. Agregar alumno")
    print("2. Modificar alumno")
    print("3. Eliminar alumno")
    print("4. Listar alumnos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        modificar_alumno()
    elif opcion == "3":
        eliminar_alumno()
    elif opcion == "4":
        listar_alumnos()
    elif opcion == "5":
        print(" Saliendo del programa...")
        
        break
        
    else:
        print(" Opción inválida.")
