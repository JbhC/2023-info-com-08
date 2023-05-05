#Escribe un programa que solicite al usuario un número decimal y luego
#imprima la parte entera y decimal por separado

nro = float(input("Ingrese un número decimal: "))
print("El número ingresado es: ",nro)


entero= math.trunc(nro)

print("La parte entera es: ",entero," y la parte decimal es: ")


