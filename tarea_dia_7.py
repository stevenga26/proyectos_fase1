### Tareas del dia 7

## Ejercicio 1 lista con comidas favoritas y mostar solo la primera y ultima

comidas =["Arroz con pollo", "Sushi", "pizza", "Hamburguesas"]
print(comidas[0])
print(comidas[-1])

## Ejercicio 2 Crear una tupla con los días de la semana e imprimir cada uno.

dias_de_la_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(dias_de_la_semana)

## Ejercicio 3 Crear un set con varios números, agregar uno nuevo y eliminar otro.

numero = {1, 2, 45, 4, 87, 98, 32, 10, 45}
numero.add(3)
print(numero)
numero.remove(45)
print(numero)

## Ejercicio 4 Crear un diccionario con tus datos personales y mostrar cada clave y valor

datos = {
    "Nombre:": "Steven",
    "Apellido:": "Garcia",
    "Edad:": "24",
    "Alias:": "Neshink"
}
for clave, valor in datos.items():
    print(clave, valor)

print(datos)

## Ejercicio 5 Hacer un mini proyecto de lista de tareas

tareas = ["Correr", "Saltar", "Levantar pesas"]

while True:
    print("1. Agregar tareas.")
    print("2. Ver tareas.")
    print("3. Eliminar tarea.")
    print("4. Modificar tarea.")
    print("5. Salir.")

    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nueva = input("Escriba la nueva tarea: ")
        tareas.append(nueva)
        print("Tarea:", nueva, ", Agregada con exito")

    elif opcion == "2":
        print("Las tareas en la lista son: ")
        for i in tareas:
            print("-", i)

    elif opcion == "3":
        eliminar = input("Escreiba la tarea que desea eliminar: ")
        tareas.remove(eliminar)
        print("Tarea: ", eliminar, "Eliminada con exito.")

    elif opcion == "4":
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
        modificar = input("indique que tarea desea modificar: ")
        if modificar in tareas:
            remplazo = tareas.index(modificar)
            agregar_nueva = input("Indique que tarea desea agregar: ")
            tareas[remplazo] = agregar_nueva
            print("Tarea ", modificar, "modificada con exito a ", agregar_nueva)
        else:
            print("La tarea,", modificar, ",  no se encuentra en la lista.")

    elif opcion == "5":
        print("Hasta luego, buen dia.")
        break
    
    else:
        print("Opcion no encontrada")

