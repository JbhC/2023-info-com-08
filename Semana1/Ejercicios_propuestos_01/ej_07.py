# Escribe un programa que calcule el área de un triángulo a partir de la base y la altura dadas.

base = float (input("Ingrese valor de la base del triángulo [cm]: "))

altura = float (input("Ingrese valor de la altura del triángulo [cm]: "))

at = round((base*altura)/2,2)

print("El área del triangulo es: ",at," cm^2")
