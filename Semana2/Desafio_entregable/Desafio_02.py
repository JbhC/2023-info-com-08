# Desafío 2: ANALIZADOR DE TEXTOS

# Crear un programa que le pida al usuario ingresar un texto y luego 3 letras de su interés; a partir de ello que se analice: 

frase =(input("Ingrese el texto: "))
fm = frase.lower()
l1 = input("Ingrese primera letra: ")
l2 = input("Ingrese segunda letra: ")
l3 = input("Ingrese tercera letra: ")

# 1°) Cantidad de veces que aparece cada letra 

letras = [l1.lower(),l2.lower(),l3.lower()]
for i in letras:
    print("La letra ",i," aparece ",fm.count(i),"veces.")

# 2°) Cantidad total de palabras en el texto

palabras = frase.split(" ")
print("La cantidad de palabras que tiene el texto ingresado es: ",len(palabras))

# 3°) Primera y última letra que aparecen en el mismo

print(f'La primera letra es {frase[0]}, y la última letra es {frase[-1]}')

# 4°) Mostrar el texto en orden inverso

palabras.reverse()
print("El texto en orden inverso es: ",palabras)

# 5°) Indicar si la palabra "Python" aparece en el texto

posibilidades = {
    True : "existe",
    False : "no existe"
}

yes_python = "python" in fm

print("En la frase introducida la palabra Python",posibilidades[yes_python])

