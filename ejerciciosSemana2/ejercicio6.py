#6-Escribir un programa que pida al usuario un número entero y muestre por
#pantalla si es múltiplo de 2 y de 3 a la vez.

numero= int(input("Ingresa un numero entero: "))

if numero %2 == 0 and numero %3 == 0:
    print ( f'{numero} es multiplo de 2 y de 3 a la vez.')
else:
    print ( f'{numero} no es multiplo de 2 y de 3 a la vez.')

    