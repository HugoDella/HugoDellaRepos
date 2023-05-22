# 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio
# después de aplicar el descuento.

def calcular_descuento(precio, porcentaje_descuento):
    desc= precio* porcentaje_descuento/100
    precio_final= precio - desc
    return(precio_final)

print(calcular_descuento(100,20))