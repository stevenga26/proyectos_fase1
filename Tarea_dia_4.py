### Tarea día 4 

# Ejercicio 1: Saludo personalizado 

saludo = str(input("Ingrese un Nombre:" " "))
print("Hola " + saludo + ", ¿cómo estás?")

## Ejecicio 2: pedir dos números y mostrar su suma, resta, multiplicación y división

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:",round(division, 2))

## pedir tu edad y mostrar en cuantos años cumplirás 100 años
edad = int(input("ingrese su edad:" " "))
años_restantes = 100 - edad
print("Faltan", años_restantes, "años para que cumplas 100 años.")

## calcular el área de un triángulo
base = float(input(" ingrese la base del trangulo:" " "))
altura = float(input ( "ingrese la altura del triangulo:" " "))
area = base * altura /2

print("El area del triangulo es de:", area)
