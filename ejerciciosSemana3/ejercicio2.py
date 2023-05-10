# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

numero=int(input("ingrese un numero: "))
contador=0
suma=0
while contador < numero:
    contador += 1
    suma += contador
print(f'la suma de los numeros del 1 hasta el {numero} es: {suma}')
    

