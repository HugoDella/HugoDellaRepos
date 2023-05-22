# 14-Crea una función llamada encontrar_maximo que tome una lista de números
# como parámetro y devuelva el número máximo de la lista.

def encontrar_maximo(numeros):
    lista_num=list(numeros)
    max= lista_num[0]
    for mayor in lista_num:
        if mayor > max:
            max = mayor
    return f"el numero maximo de la lista es: {max}"

print(encontrar_maximo([2,4,9,7]))