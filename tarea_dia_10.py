### Ejemplos del dia 10 

## introduccion a los Strings
""""
nombre = "Steven"
print("Hola " + nombre )

## Los strings son inmutables (no se pueden modificar directamente), pero sí podés crear nuevas versiones transformadas usando métodos.

frase = "   hola steven   "
print("Original:", frase)
print("Mayúsculas:", frase.upper())
print("Título:", frase.title())
print("Sin espacios:", frase.strip())
print("Reemplazo:", frase.replace("steven", "programador"))
print(frase.split()) ## combierte el string en una lista y separar los elementos dentro

## mini practica 

nombre = str(input("Ingrese su nombre: "))
letras = len(nombre)
print(f"Hola, ", nombre, "tu nombre tine ", letras, "letras.")
print(nombre.upper())
remplazo = (nombre.replace("t", "p"))
print(f"Remplazo: ", remplazo)
"""""
""""
## listas 

frutas = ["manzana", "pera", "sandía"]
print(frutas[0])  # manzana

## agregar elemento
frutas.append("uva")      # Agrega al final
frutas.insert(1, "mango") # Inserta en posición 1
print(frutas)

## Eliminar elemento ( hay que especifificar la pocicion con .pop() si no elimina el ultimo )
frutas.remove("pera")  # Elimina el valor indicado
frutas.pop(2)          # Elimina el elemento en la posición 2
print(frutas)

## ordenar y contar listas 
numeros = [4, 2, 9, 1, 5 ,5]
numeros.sort()     # Ordena de menor a mayor
print(numeros)
numeros.reverse()  # Invierte el orden
print(numeros)
print(numeros.count(5))  # Cuenta cuántas veces aparece el 5

### buscar elementos con condicionales

if "manzana" in frutas:
    print("Sí está la manzana")
else:
    print("No está la manzana")

## combinar listas 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_total = lista1 + lista2
print(lista_total)

### Ejercicio 
fruta = []
for i in range(5):
    fruta.append(input(f"Ingrese la fruta #{i+1}: "))
print(fruta)
while True:
    print(f"\n--- MENÚ DE OPCIONES ---")
    print(f"1. Agregar una fruta.")
    print(f"2. Eliminar una fruta.")
    print(f"3. ordenar alfabeticamente.")
    print(f"4. Mostar cuantas frutas hay.")
    print(f"5. Salir del programa.")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        nueva = input("Indique que fruta desea agregar: ")
        fruta.append(nueva)
        print(f"Fruta '{nueva}' agregada con éxito.")
    elif opcion == "2":
        eliminar = input("Indique la fruta que desa eliminar: ")
        if eliminar in fruta:
            fruta.remove(eliminar)
            print(f"{eliminar}, A sido eliminada de la lista.")
        else:
            print(f"Esta fruta no esta en la lista.")
    elif opcion == "3":
        fruta.sort()
        print(f"{fruta} Ordenada en orden alfabetico.")
    elif opcion == "4":
       print(f"Hay {len(fruta)} frutas en la lista.")
    elif opcion == "5":
        print(f"Gracias por utilizar este programa.")
        break
    else:
        print(f"Opccion no valida ingrese otra opcion.")              
print(f"!Hasta la proxima¡.")
"""

### Diccionarios avanzados = Un diccionario guarda pares clave: valor

estudiantes = {
    "Steven": {"edad": 24, "nota": 90},
    "Carlos": {"edad": 43, "nota": 85}
}

for nombre, info in estudiantes.items():
    print(f"{nombre} tiene {info['edad']} años y una nota de {info['nota']}.")

estudiantes["Steven"]["nota"] = 95
print(estudiantes["Steven"])

### Ejercicio de diccionarios 
Alumnos = []
while True:
    print(f"\n--- MENÚ DE OPCIONES ---")
    print(f"1. Añadir a 1 alumno.")
    print(f"2. Modificar nota.")
    print(f"3. Visualizar lista completa.")
    print(f"4. Buscar a 1 alumno.")
    print(f"5. Eliminar a un alumno.")
    print(f"6. Salir.")
    opcion = input(f"Elija una opcion: ")
    if opcion == "1":
        nombre = input(f"Nombre del alumno: ")
        edad = int(input(f"Ingrese la edad del alumno: "))
        nota = float(input(f"Ingrese la nota del alumno: "))
        nuevo = {
            "nombre": nombre,
            "edad": edad,
            "nota": nota
        }
        Alumnos.append(nuevo)
        print(f"Alumno '{nombre}' agregado con exito")
    elif opcion == "2":
        quien = input(f"Indique nombre del alumno: ")
        encontrado = False
        for alumno in Alumnos:
            if alumno["nombre"] == quien:
                nota_edit = input (f"Ingrese la nueva nota: ")
                alumno["nota"] = float(nota_edit)
                encontrado = True
                print(f"Nota de '{quien}' modificada a '{nota_edit}' con exito.")
                break
        if not encontrado:
            print(f"No se encontro ningun alumno con ese nombre.")
    elif opcion == "3":
        if not Alumnos:
            print("No hay alumnos registrados todavía.")
        else:
            print("\n--- LISTADO DE ALUMNOS REGISTRADOS ---")
            for persona in Alumnos:
                print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Nota: {persona['nota']}")
            print("------------------------------------------")
    elif opcion == "4":
        busqueda = input(f"Ingrese el nombre del alumno que desea buscar: ")
        encontrado = False
        for alumno in Alumnos:
            if alumno["nombre"] == busqueda:
                print(f"Nombre: {alumno["nombre"]}, Edad: {alumno["edad"]}, Nota: {alumno["nota"]}")
                encontrado = True
                break
        if not encontrado:
            print(f"Alumno no encontrado.")
    elif opcion == "5":
        eliminar = input(f" Ingrese el nombre del alumno que desea eliminar: ")
        elimminado = False
        for alumno in Alumnos:   
            if alumno["nombre"] == eliminar:
                Alumnos.remove(alumno)
                elimminado = True
                print(f"El alumno '{eliminar}' fue eliminado con exito.")
                break
        if not elimminado:
            print(f"Alumno no esta en la lista.")
    elif opcion == "6":
        print(f"Saliendo del programa con exito.")
    else:
        print(f"Opcion no válida, vuelva a intentarlo.")
        break
print(f"---- Gracias por usar este programa ---- ")