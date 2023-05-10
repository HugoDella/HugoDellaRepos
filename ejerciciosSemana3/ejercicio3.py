# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

numero= int(input("ingrese un numero: "))

multiplicador=0

while multiplicador < 10:
    multiplicador +=1
    print(f'{numero}*{multiplicador}=', numero * multiplicador)
    