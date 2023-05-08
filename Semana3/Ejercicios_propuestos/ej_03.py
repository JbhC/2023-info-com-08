# Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

n = int(input("Ingrese un número: "))

for i in range (1,11):
    # print(n,"X",i,"= ",n*i )
    print(f'{n} X {i} = {n*i}' )
    