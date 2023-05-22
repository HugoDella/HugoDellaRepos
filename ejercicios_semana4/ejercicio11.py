# 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.


def contar_vocales(palabra):
    vocales=0
    for letra in palabra:
       if letra in "aeiouAEIOU":
        vocales= vocales + 1
    return(f"el texto contiene {vocales} vocales")

print(contar_vocales("murcielago"))