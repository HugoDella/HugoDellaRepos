"""11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares."""

numero1=int(input("ingresa el primer numero: "))
numero2=int(input("ingresa el segundo numero: "))

if numero1 %2==0  and numero2 %2==0:
   print("ambos son pares su suma es:", numero1+numero2)
else:
   print("uno o ambos numeros no son pares")
   
    