### Ejemplos del dia 9

## Repaso, bucles dentro de bucles 

for i in range(1, 5):
    for j in range(1, 4):
        print(i, j)


## Listas animadas (matrices) 

notas = [
    [85, 90, 88],
    [78, 81, 85],
    [92, 95, 91]
]

# Mostrar la primera nota del segundo alumno
print("Primera nota del segundo alumno:", notas[1][0])

# Recorrer todas las notas
for i in range(len(notas)):           # Recorre cada alumno
    for j in range(len(notas[i])):    # Recorre cada nota de ese alumno
        print("Alumno", i + 1, "Nota", j + 1, "=", notas[i][j])


### Manejo de errores (try, except, finally)
"""""
try:
    numero = int(input("Ingresa un número: "))
    resultado = 100 / numero
    print("El resultado es:", resultado)
except:
    print("Ocurrió un error. No se puede dividir entre 0 o se ingresó algo inválido.")
"""
## Ejemplo 2 mas especifico 

try:
    numero = float(input("Ingrese un numero: "))
    print(100 / numero)
except ValueError:
    print("Debe ingresar un número válido.")
except ZeroDivisionError:
    print("No pruede dividir entre 0.")
finally:
    print("Gracias por usar este programa.")