### Dia 6 bucles y estructyuras repetitivas ##

# Ejemplo 1 

## bucle for 

for i in range(5):
    print("Hola, Steven")

for i in range(1, 6):
    print("numero:", i)

for i in range(1, 20, 3):
    print(i)

### bucle while 

numero = 1
while numero <= 5:
    print("Número:", numero)
    numero = numero + 1

## mescla de bucle con condicion 

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

## brake 

nombres = ["Ana", "Carlos", "David", "Elena", "Fernando"]
nombre_buscado = "David"

for nombre in nombres:
    if nombre == nombre_buscado:
        print(f"¡{nombre_buscado} encontrado!")
        break # Detiene el bucle por completo
    print(f"Comprobando a {nombre}...")

print("Búsqueda finalizada.")

## continue

numeros = [5, 10, -2, 15, -7, 20]

for num in numeros:
    if num < 0:
        print(f"Saltando el número negativo: {num}")
        continue # Pasa a la siguiente iteración, omitiendo el print inferior
    print(f"Procesando el número: {num}")

### Ejercio de practica

numero = int(input("Ingrese un número: "))
if numero <1 or numero > 10:
        print("Número fuera de rango. Intenta de nuevo.")
else:
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
                
        
        
