#Crea un programa que pida al usuario el radio de un círculo y calcule su área. 
#La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
#Supongamos que pi = 3.1416

pi= float(3.1416)
radio=float(input("Ingrese el radio del circulo en [cm]: "))

area=round(pi*radio*radio,2)

print("El área del circulo es: ",area, "cm^2.")
