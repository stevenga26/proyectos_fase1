### listas y colecciones 

frutas = ["manzana", "uva", "pera", "mango"]
print(frutas)

print(frutas[0])  # Muestra el primer elemento
print(frutas[2])  # Muestra el tercero
print(frutas[-1])  # Muestra "mango"

## este se utiliza para modificar un elemento de la lista 
modificar = input("Elemento: ")
frutas[2] = "sandía"
print(frutas)

# este se usa para agragar un elemento al final de la lista 

frutas.append("piña")
print(frutas)

## Este agreba un  elemento enel numeroqueindiquemos correindo asi alos demas 

frutas.insert(1, "fresa")
print(frutas)

## En este caso borra el elemento por posicion  indicada
 
frutas.pop(2)
print(frutas)

## En este caso lo indicamos para limpiar o vaciar la lista 

frutas.clear()
print(frutas)

## vamos a utoilizar aun bucle para recorrer iuna lista 

frutas = ["manzana", "pera", "mango", "sandía"]
for fruta in frutas:
    print("Me gusta la", fruta)

## si quieremos saber cuantos elementos tiene nuestra lista utlizaremos len 

print("Hay", len(frutas), "frutas en la lista.")


### tuplas 

colores = ("rojo", "verde", "azul")
print(colores)

# colores[0] = "negro" estoo da error ya que una tupla es inmutable y noi se opuede modificar

## al igual que una lista estas pueden corrrerse dentro de un bucle 

colores = ("rojo", "verde", "azul")
for color in colores:
    print("Este es el color", color)

### conjuntos o sets 

numeros = {1, 2, 3, 3, 4}  ## al imprimir no tienen orden y nor permite elementrtos repetidos se puede declarar con {} o indicando set()
print(numeros)  # Muestra {1, 2, 3, 4}

numeros.add(5)     # Agregar
print(numeros)

numeros.remove(2)  # Eliminar
print(numeros)

### diccionarios 

persona = {
    "nombre": "Steven",
    "edad": 24,
    "pais": "Guatemala"
}
print(persona)
print(persona["nombre"])


persona["edad"] = 25           # Modificar
print(persona)
persona["email"] = "steven@mail.com"  # Agregar nueva clave
print(persona)



#### Ejercicio de practrica

tareas = ["Hacer la cama", "Tarea de programación", "Proyecto"]

while True:
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Elija una opción: ").strip()

    if opcion == "1":
        nueva = input("Escriba la tarea nueva: ")
        tareas.append(nueva)
        print("Tarea agragada con exito")

    elif opcion == "2":
        print("Tus tareas son:")
        for i in tareas:
            print("-", i)
    
    elif opcion == "3":
        eliminar = input("Escriba la tarea que desea eliminar: ")
        if eliminar in tareas:
            tareas.remove(eliminar)
            print("Tarea eliminada con exito")
        else:
            print("Esta tarea no existe.")
    elif opcion == "4":
        print("¡Hasta, luego!.")
        break
    else:
        print("Opción no válida.")
