### Tarea di 8

## Ejercicio 1 

def potencia(base, exponente = 2):
    return base * exponente


print(potencia(2))
print(potencia(4, 3))


## Ejercicio 2

mitad = lambda n: n / 2
numero = float(input("Ingrese un numero: "))
print(mitad(numero))

### Ejercicio 3

numeros = [2, 4, 6, 8, 10]

doble = list(map(lambda n: n * 2, numeros))
print(doble)
             


