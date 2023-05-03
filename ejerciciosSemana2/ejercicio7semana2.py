"""7-Escribir un programa que pida al usuario 
un carácter y muestre por pantalla si
es una letra mayúscula, una letra minúscula, 
un número o un carácter especial."""

caracter= input("ingresa un carácter:")
if caracter.islower():
    print("El carácter es un letra minuscula")
elif caracter.isupper():
    print("El carácter es una letra Mayuscula")
elif caracter.isdigit():
    print("El carácter es un numero")
else:
    print("Es un carácter especial")
    
    