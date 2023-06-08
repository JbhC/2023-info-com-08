catalogo_autos = [
    {'marca': 'Audi', 'modelo': 'A4', 'año': 2020, 'puertas': 4, 'Garantía': True, 'estado': 'Disponible'},
    {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2017, 'puertas': 4, 'Garantía': False, 'estado': 'Reservado'},
    {'marca': 'Ford', 'modelo': 'Fiesta', 'año': 2019, 'puertas': 4, 'Garantía': True, 'estado': 'Disponible'},
    {'marca': 'Toyota', 'modelo': 'Hilux', 'año': 2022, 'puertas': 2, 'Garantía': True, 'estado': 'Vendido'},
    {'marca': 'Volkswagen', 'modelo': 'Gol Trend', 'año': 2012, 'puertas': 2, 'Garantía': False, 'estado': 'Disponible'}
]

def modificar_catalogo():
    contador = 1
    print("-----Catálogo de Autos-----")

    for i in catalogo_autos:
        print(f"Auto N°{contador}: {i}" )
        contador += 1
        
    auto = int(input("Que auto desea editar del catálogo: "))
    continuar = "si"

    while(continuar == "si"):
        
        print(catalogo_autos[auto-1])

        clave= input(f"Ingrese el campo que desea modificar: ")
        valor = input(f"Ingrese el valor correspondiente a {clave}: ")

        catalogo_autos[auto][clave]= valor
        print(catalogo_autos[auto])

        continuar= input("Desea modificar otro campo? (si)(no): ")

        if continuar == "no":
            print("Las modificaciones se guardaron con éxito")
            print(catalogo_autos)


modificar_catalogo()