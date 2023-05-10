# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al
# 100.

numeros_pares=1
suma=0
while numeros_pares <= 100:
    if numeros_pares %2== 0:
        suma+= numeros_pares
print(f' la suma de los nuemros pares del 1 al 100 es: {suma}.')