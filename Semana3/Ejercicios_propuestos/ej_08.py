# Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene.

texto = input("Ingrese el texto: ")

t = texto.split(" ")

print("El número de palabras que contiene el texto ingresado es: ", len(t))

