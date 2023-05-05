#Escribe un programa que solicite al usuario una temperatura en grados
#Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.

#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

tempC = float(input("Ingrese la temperatura en °C: "))

tempF= round(float((tempC*1.8)+32),1)

print("La temperatura es:  ",tempF," °F.")