# 7-Crea una función llamada imprimir_pares que tome un número entero como
# parámetro y imprima todos los números pares desde 1 hasta ese número.


def imprimir_pares(numero):
        num_par=0
        while num_par < numero:
            num_par +=1
            if num_par %2== 0:
                print(num_par)

print(imprimir_pares(15))        



