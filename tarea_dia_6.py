### trarea del dia 6

## Ejercicio 1: imprimir los números del 1 al 10 con un for 

for i in range(1,11):
    print(i)
    numero = i + 1

## Ejercicio 2: imprimir los numeros del 10 al 1 con un while

numero = 10
while numero >= 1:
    print(numero)
    numero= numero - 1

## Ejercicio 3: calcular la suma de los numeros del 1 al 100

suma = 0
for i in range(1,101):
    suma = suma + i
print("La suma de los numeros del 1 al 100 es:", suma)

## Ejercicio 4: Mostrar los numeros pares del 1 al 10

for i in range(1,21):
    if i % 2 == 0:
        print(i)

## Ejercicio 5: Pedir 5 edades y contar cuantas son mayores de edad 

contadores = 0
for i in range(5):
    edad = int(input("Ingrese una edad: "))
    if edad >= 18:
        contadores = contadores + 1
print("Hay", contadores, "mayores de edad")

## Ejercicio 6: Crear un programa que pida numeros hasta que el usario escriba 0, y al final muestre la suma total

suma = 0

while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break 
    suma = suma + numero
print("La suma total delos numero ingresados es: ", suma)