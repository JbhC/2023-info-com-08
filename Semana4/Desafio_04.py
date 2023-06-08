
def condiciones_verificacion(lista):
    if int(lista['año']) < 2000 or int(lista['metros']) < 60 or int(lista['habitaciones']) < 2:
        return False
    else:
        return True


def agregar_a_lista():
    inmueble={}
    inmueble['año']=input("Ingrese año de construcción del inmueble: ")
    inmueble['metros']=input("Ingrese metros cuadrados: ")
    inmueble['habitaciones']=input("Ingrese n° de habitaciones: ")
    inmueble['garaje']=input("¿Posee garaje, SI - NO? ").upper()
    while inmueble['garaje']!="SI" and inmueble['garaje']!="NO":
        inmueble['garaje']=input("¿Posee garaje, SI - NO? ").upper()
    inmueble['zona']=input("Ingrese zona (A, B, C): ").upper()
    while inmueble['zona']!="A" and inmueble['zona']!="B" and inmueble['zona']!="C":
        inmueble['zona']=input("Ingrese zona (A, B, C): ").upper()
    inmueble['estado']=input("Ingrese estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()
    while inmueble['estado'].upper()!="RESERVADO" and inmueble['estado'].upper()!="DISPONIBLE" and inmueble['estado'].upper()!="VENDIDO":
        inmueble['estado']=input("Ingrese estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()
   
    if condiciones_verificacion(inmueble)==True:
        inmuebles.append(inmueble)
        return print("Se añadió el inmueble al listado.")
    else:
        return print("No se puede agregar este inmueble al listado, no cumple los requisitos.")


def listado_inmuebles(lista):
    contador = 1
    print("Los inmuebles administrados por la inmobiliaria son: ")

    for i in lista:
        print(f"Inmueble N°{contador}: {i}" )
        contador += 1

def editar_inmueble(lista):
    listado_inmuebles(lista) 
    inmueble_a_editar = int(input("Ingrese el número del inmueble que desea modificar: "))
    caracteristica = input("Ingrese la característica del inmueble que desea editar: ")   
    campo = (input(f'Ingrese el dato correspondiente al inmueble N° {inmueble_a_editar}: ' ))
    inmuebles[inmueble_a_editar-1][caracteristica]= campo
    print(listado_inmuebles(lista))
    
    
def eliminar_inmueble(lista):
    listado_inmuebles(lista) 
    inmueble_a_eliminar = int(input("Ingrese el número del inmueble que desea eliminar: "))
    inmuebles.pop(inmueble_a_eliminar-1)
    print(listado_inmuebles(lista))


def modificar_estado_del_inmueble(lista):
    listado_inmuebles(lista)
    inmueble_a_modificar_estado = int(input("Ingrese el número del inmueble para modificar su estado: "))
    estado_inmueble = (input(f'Ingrese el estado actual de inmueble N° {inmueble_a_modificar_estado}: ' ))
    inmuebles[inmueble_a_modificar_estado-1]['Estado']= estado_inmueble
    print(f'El nuevo estado del inmueble {inmueble_a_modificar_estado} es: {estado_inmueble}')


def buscar_inmueble(lista):
    print("Ejercicio no resuelto")

inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]



opcion=int(input('Bienvenido, ¿Qué desea hacer?\n1- Agregar inmueble\n2- Editar inmueble\n3- Elimiar inmueble\n4- Modificar estado del inmueble\n5- Busqueda de inmueble\n\nIngrese opción elegida: '))

if opcion==1:
    agregar_a_lista()
    listado_inmuebles(inmuebles)

elif opcion==2:
    editar_inmueble(inmuebles)
    print("El inmueble ha sido editado correctamente!")

elif opcion==3:
    eliminar_inmueble(inmuebles)
    print("El inmueble ha sido eliminado")

elif opcion==4:
    modificar_estado_del_inmueble(inmuebles)
    print("Se ha modificado el estado del inmueble correctamente!") 

else:
    buscar_inmueble(inmuebles)
    print("LO SIENTO, NO TUVE TIEMPO DE TERMINAR ESTA OPCIÓN")

