# 15-Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.

def contar_palabras(texto):
    lista_texto=list(texto.split())
    return len(lista_texto)

print(contar_palabras("hola como te va"))