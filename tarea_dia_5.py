## Tarea del dia 5

## ejercicio 1 - mayor o menor de edad 

edad = int(input("Ingrese su edad: "))
if edad>= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

## Ejercicio 2 - aprobado o reprobado +

nota = float(input("Ingrese su nota: "))
if nota >= 60:
    print("¡Aprobado!")
else:
    print("¡Reprobado!")


## Ejercicio 3 - Recomendación según el clima

temperatura = float(input("Ingrese el clima actual en grados Celsius: "))
if temperatura < 10:
    print("Hace frío, lleva abrigo.")
elif 10 <= temperatura < 20:
    print("El clima es templado, puedes salir con una chaqueta ligera.")
else:
    print("Hace calor, usa ropa ligera.")

## Ejercicio 4 - Número par o impar

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

## Ejercicio 5 - Comparar dos números

num1= float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
