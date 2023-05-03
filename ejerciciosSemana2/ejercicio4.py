#4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#pantalla si está aprobado (5 o más) o no.


nota= int((input("ingresa tu nota: ")))

if nota <= 10:
    print("Felicidades has aprobado.")
if nota < 5:
    print("Desafortunadamente no has aprobado.")
    