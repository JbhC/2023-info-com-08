# Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).

p = input("Ingresa una palabra: ")

if p == p[::-1]:
    print("La palabra ingresada es palíndromo")
else:
    print("La palabra ingresada no es un palíndromo")