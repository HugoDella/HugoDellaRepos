#desafio semana 3
import random
print("Bienvenido al juego adivina el numero!")
nombre= input("cual es tu nombre? ")
print(nombre, "deberas adivinar un numero entre 1 y 100, solo tenes 8 intentos")
print("Buena Suerte!")

numero= random.randint(1,100)
intentos=0
while intentos <= 7:
    numero_j=input("ingresa un numero: ")
    intentos += 1
    if intentos == 8:
        print(f"mala suerte {nombre} se acabaron los intentos")
        print(f"El numero que debias adivinar es el {numero}")
        print("juega otra vez!")
        break
    if not numero_j.isdigit(): 
         print("debes ingresar numeros enteros, intenta de nuevo")
         intentos-= 1
         continue
    if int(numero_j) < numero:
        print("ouch! fallaste, el numero es mas grande")
        print(f"te quedan ",{8-intentos}," intentos.")
    elif int(numero_j) > numero:
        print("ouch! fallaste, el numero es mas chico")
        print(f"te quedan ",{8-intentos}," intentos.")
    
    elif int(numero_j) == numero:
         print("felicidades adivinaste!")
         print("Ganaste el juego!")
         break