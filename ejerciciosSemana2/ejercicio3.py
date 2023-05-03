#3-Escribir un programa que pida al usuario dos números y muestre por pantalla
#cuál de ellos es mayor.

num1= int(input("ingresa un numero: "))
num2= int(input("ingresa otro numero: "))

if num1 > num2:
    print(f'{num1} es mayor')
else:
    print(f'{num2} es mayor')
    