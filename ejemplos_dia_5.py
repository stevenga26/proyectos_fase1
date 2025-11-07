## ejemplos de condicionales y operadores lógicos

# Ejemplo 1: Verificar si un número es positivo, negativo o cero
n = float(input("Ingresa un número: "))

if n > 0:
    print("Positivo")
elif n == 0:
    print("Cero")
else:
    print("Negativo")



## Ejemplo de condicionales anidados

edad = int(input("¿Qué edad tienes? "))

if edad >= 18:
    if edad >= 65:
        print("Eres adulto mayor.")
    else:
        print("Eres adulto.")
else:
    print("Eres menor de edad.")


## Ejemplo de operadores lógicos combinados

edad = int(input("¿Qué edad tienes? "))

if edad >= 18 and edad <= 65:
    print("Estás en edad laboral.")
elif edad > 65:
    print("Podrías estar jubilado.")
else:
    print("Eres menor de edad.")


# Ejemplo de par o impar

numero = int (input( "ingrese un numero: "))

if numero % 2 == 0:
    print("El numero es par.")
else:
    print(" El nunero es impar.")


### Ejercio de practrica 

## Recomemndacion segun el clima 

temperatura = float(input("Ingrese el clima actual en grados Celsius: "))
if temperatura < 10:
    print("Hace frio, lleva abrigo,")
elif temperatura >= 10 and temperatura < 25:
    print( "El clima es agradable.")
elif temperatura >=25:
    print("Hace calor,toma agua.")