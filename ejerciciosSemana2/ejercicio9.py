"""9-Escribir un programa que pida al usuario 
tres números y muestre por pantalla
el mayor 
de ellos."""  

num1= int(input("ingresa un número: "))
num2= int(input("ingresa otro número: "))
num3= int(input("ingresa otro número: "))

if num1 > num2 and num1 > num3:
    print (f"El {num1} es Mayor")
elif num2 > num3 and num2 > num1:
    print (f"El {num2} es Mayor")
elif num3 > num1 and num3 > num2:
    print (f"El {num3} es Mayor")
else:
    print("los tres numeros son iguales.")  
      
   
    
    