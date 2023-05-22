# 12-Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(temp):
    farenheit= temp*9/5 +32
    return(farenheit)

print(convertir_temperatura(60)) 