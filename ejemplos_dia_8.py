### Ejemplos del dia 8

## Funciones = lo usamos para llamar y reutilizar codigo en varias ocaciones sin repetir 

def saludar():
    print("¡Hola, Steven! Bienvenido a la clase del Día 8.")

saludar()

## Funciones con parametros = podemos hacer que la funcion resiva datos y la imprima 

def saludar_persona(nombre):
    print("Hola,", nombre)

saludar_persona("Steven")
saludar_persona("Ana")

## Funciones con retorno (return) = Algunas funciones devuelven un resultado, que podés guardar en una variable.

def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print("La suma es:", total)

## Parámetros por defecto = Podés asignar un valor por defecto en caso de que no se envíe uno.

def saludar(nombre="invitado"):
    print("Hola,", nombre)

saludar("Steven")
saludar()

## unciones dentro de funciones = Podés tener una función que use otra. Esto es muy común en programas grandes.

def cuadrado(x):
    return x * x

def mostrar_cuadrado(numero):
    print("El cuadrado de", numero, "es", cuadrado(numero))

mostrar_cuadrado(4)

## Ejercicios guiados 

## Ejercicio 1

def presentacion(nombre = "invitado"):
    print("Hola, soy", nombre, " y estoy aprendiento Python.")

presentacion("Steven")

## Ejercicio 2

def multiplicar(a, b):
    resultado = a * b
    return(resultado)

total = multiplicar( 8, 10)
print("El resultado es: ", total)

## Ejercicio 3

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print(es_par(5))
print(es_par(4))


### funciones con multiples retornos

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

resultado = operaciones(4, 6) ## de esta forma para llamar a la variable varias veces y reutilizar
print(resultado)

print(operaciones(10, 2))   ### de esta forma solo se usa una vez 
print(operaciones(15, 15))

suma, resta, mult, div = operaciones(10, 2)  ## podemos desempaquetar de esta forma 
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", mult)
print("División:", div)

## Llamar una funcion dentro de otra

def saludar(nombre):
    print("Hola,", nombre)

def bienvenida():
    nombre = input("¿Cómo te llamas?: ")
    saludar(nombre)
    print("Bienvenido a la plataforma de aprendizaje.")

bienvenida()



### Practica dia 8 

## Ejercicio 1

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    division = a / b
    return(suma, resta, multiplicar, division)

sum, rest, multi, divi = operaciones(3, 5)
print("suma = ", sum)
print("resta = ", rest)
print("multiplicacion = ", multi)
print("division = ", divi)


## Ejercicio 2

def saludo(nombre):
    print("Hola, ", nombre)

def bienvenida():
    quien = input("Cual es tu nombre: ")
    saludo(quien)
    print("Bienvenido al programa mas pro.")

bienvenida()

### Funciones con parametros opcionales (Por defecto)

def saludar(nombre="invitado"):
    print("Hola,", nombre)

saludar("Steven")
saludar()


def potencia(base, exponente=2):  ### si solo se le da un numero su exponente siempre va a ser 2 (al cuadrado)
    return base ** exponente

print(potencia(4))     # usa el valor por defecto (4²)
print(potencia(4, 3))  # usa el valor que se le pasa (4³)

## Funciones lambda ( anonimas )

doblar = lambda x: x * 2   ### lambda no usa def, no tiene nombre largo ni return
print(doblar(5))

sumar = lambda a, b: a + b
print(sumar(3, 7))

numeros = [1, 2, 3, 4, 5]
doblados = list(map(lambda n: n * 2, numeros))
print(doblados)



