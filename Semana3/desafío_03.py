nombre = input("Ingrese su nombre: ")

print(f' ¡Hola {nombre.capitalize()}!')
print("\n En este juego debes adivinar cual es el número seleccionado, entre 1 y 100. \n ¡Solo tienes 8 intentos para descubrirlo! ")
print("\n ¡Mucha suerte!\n")

from random import randint

n_random = randint (1, 100)

contador = 1

n1 = input("Ingrese un número entre el 1 y el 100: ")

while n1.isdigit()==False:
    print("\nEl valor ingresado no es un número, vuelva a ingresarlo.")
    
    n1 = input("Ingrese un número entre 1 y 100: ")

while contador<8:
    

    if int(n1) < n_random:
        print("\nEl número ingresado es menor que el número de la suerte.")
        print(f'¡Te quedan {8-contador} intentos!')
        n1 = input("\nIngrese un número entre 1 y 100: ")

    elif int(n1) > n_random:
        print("\nEl número ingresado es mayor que el número de la suerte.")
        print(f'¡Te quedan {8-contador} intentos!')
        n1 = input("\nIngrese un número entre 1 y 100: ")

    else:
        print("\nHa ingresado el número de la suerte. ¡Felicitaciones!")
        quit()
    contador+=1

print(f'\nSe te agotaron los intentos, el número de la suerte era {n_random}, ¡Buena suerte la próxima!')
