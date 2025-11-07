### Tarea dia 9 

## reto dia 9

while True:
    try:
        solicitud = input("ingrese un número (o escriba salir si desea finalizar): ")
        if solicitud.lower() == "salir":
            print("Programa finalizado por el usuario, ¡Gracias po usar el programa!")
            break
        numero = float(solicitud)
        resultado = 100 / numero
        print("El resultado de 100 dividido entre", numero, "es: ", resultado)
    except ValueError:
        print("Ingrese un dato válido.")
    except ZeroDivisionError:
        print("Error: No puede dividir entre 0.")
    finally:
        print("Intento Completado.")

print("Gracias por usar el programa de Steven.")

