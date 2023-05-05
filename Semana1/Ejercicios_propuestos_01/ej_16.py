#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal (IMC).

# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

peso = float(input("Ingrese su peso en kg: "))

altura = float(input("Ingrese su altura en m: "))

imc = round(float(peso/(altura**2)),)

print("Su IMC es de ",imc)

