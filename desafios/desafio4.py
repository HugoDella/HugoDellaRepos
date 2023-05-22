#desafio semana 4 La inmobiliaria.
def agregar_inmueble(lista_inmuebles):
    inmueble={}
    inmueble['año']= int(input( "ingrese año de construccion: "))
    inmueble['metros']= int(input( "ingrese metros cuadrados del inmueble: "))
    inmueble['habitaciones']= int(input( "ingrese cantidad de habitaciones: "))
    inmueble['garaje']= input( "¿cuenta con garaje?: ").upper()== "SI"
    inmueble['zona']= input( "ingrese a que zona pertenece (A, B O C) : ").upper()
    inmueble['estado']= input( "ingrese el estado del inmueble (Disponible, Reservado o Vendido): ").capitalize()
    
    if validar_inmueble(inmueble):
        print("se agrego el inmueble correctamente")
        return inmueble
    else:
        print("el inmueble no se pudo validar")

def validar_inmueble(inmueble):
    if inmueble['año']< 2000:
        return False
    if inmueble['metros']<60:
        return False
    if inmueble['habitaciones']<2:
        return False
    if inmueble['zona']not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible','Reservado','Vendido']:
        return False
    return True

def mostrar_inmueble(lista_inmuebles):
    contador=1
    for inmueble in lista_inmuebles:
        print(f"inmueble num:{contador}")
        print("año: ",inmueble['año'])
        print("metros: ", inmueble['metros'])
        print("habitaciones: ",inmueble['habitaciones'])
        print("garaje: ","SI" if inmueble['garaje'] else "NO")
        print("zona: ",inmueble['zona'])
        print("estado: ", inmueble['estado'])
        print("precio: ", calcular_precio(inmueble))
        print("#########################")
        contador+=1

def calcular_precio(lista_inmuebles):
    precio_base=(lista_inmuebles['metros'] * 100) +(lista_inmuebles['habitaciones'] * 500) +(lista_inmuebles['garaje'] * 1500)     
    antiguedad= 2023 - lista_inmuebles['año']
    if lista_inmuebles['zona']== "A":
        precio=precio_base*(1 - antiguedad / 100)
    elif lista_inmuebles['zona']== "B":
        precio=precio_base*(1 - antiguedad / 100)*1.5
    elif lista_inmuebles['zona']== "C":
        precio=precio_base*(1 - antiguedad / 100)*2
    return precio

def modificar_inmuebles(lista_inmuebles):
    mostrar_inmueble(lista_inmuebles)
    index= int(input("ingrese el numero de inmueble a modificar: "))
    if index>= 0 and index <= len(lista_inmuebles):
        inmueble= lista_inmuebles[index -1]
        inmueble_modificado= {}
        inmueble_modificado.update(inmueble)

    inmueble['estado']= input( "ingrese el estado del inmueble (Disponible, Reservado o Vendido): ").capitalize()
    if validar_inmueble(inmueble):
        print("modificacion exitosa")
    else:
        print("falla en la modificacion, reintentar")
        inmueble.clear()
        inmueble.update(inmueble_modificado)

def eliminar_inmuebles(lista_inmuebles):
    mostrar_inmueble(lista_inmuebles)
    index= int(input("ingrese el numero de inmueble a eliminar: "))
    if index>= 0 and index <= len(lista_inmuebles):
        del lista_inmuebles[index -1]
        print("inmueble eliminado")
    else:
        print("el inmueble no pudo ser eliminado")

def buscar_inmuebles(presupuesto, lista_inmuebles):
    inmuebles_sugeridos= []
    for inmueble in lista_inmuebles:
        if inmueble['estado'] in ['Disponible', 'Reservado'] and calcular_precio(inmueble)<=presupuesto:
            inmueble['precio']= calcular_precio(inmueble)
            inmuebles_sugeridos.append(inmueble)
    return inmuebles_sugeridos
    

lista_inmuebles=[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado':'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

while True:

    print("-----BIENVENIDO-----")
    print("MENU")
    print("1- BUSCAR INMUEBLES")
    print("2- AGREGAR INMUEBLES")
    print("3- MODIFICAR INMUEBLES")
    print("4- ELIMINAR INMUEBLES")
    print("5- VER CATALOGO")
    print("6- SALIR")
    opciones=input("elija una opcion: ")
    if opciones=="1":
        print("BUSQUEDA DE INMUEBLES")
        presupuesto= float(input("ingrese su presupuesto: "))
        resultado= buscar_inmuebles(presupuesto, lista_inmuebles)
        for inmueble_sugerido in resultado:
            print(inmueble_sugerido)
    elif opciones =="2":
        print("AGREGAR INMUEBLES")
        lista_inmuebles.append(agregar_inmueble(lista_inmuebles))
    elif opciones=="3":
        print("MODIFICAR INMUEBLES")
        modificar_inmuebles(lista_inmuebles)
    elif opciones == "4":
        print("ELIMINAR INMUEBLES")
        eliminar_inmuebles(lista_inmuebles)
    elif opciones== "5":
        print("VER CATALOGO")
        mostrar_inmueble(lista_inmuebles)
    elif opciones =="6":
        print("¿ESTA SEGURO DE QUE QUIERE SALIR?")
        respuesta= input("si/no:  ")
        if respuesta== "no":
            continue
        else:
            break

print("PROGRAMA FINALIZADO")

