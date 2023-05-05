texto = input("Ingrese articulo o frase: ")

letra1=input("Ingrese la letra 1 a elección: ")
letra2=input("Ingrese la letra 2 a elección: ")
letra3=input("Ingrese la letra 3 a elección: ")

letras = [letra1, letra2, letra3]

texto = texto.lower()
letras = [letra1.lower(), letra2.lower(), letra3.lower()]

for letra in letras:
    print(f'La letra{letra} apareció {texto.count(letra)} veces.')

palabras = texto.split(' ') #ver que tambien pueden estar separadas por punto o coma

print("La cantidad de palabras que tiene el texto es de: ",len(palabras))

#para el punto 3 sino queres tener en cuenta los caracteres
palabras = texto.replace('.',' ')
palabras = palabras.replace(':',' ')
palabras = palabras.replace(';',' ')
palabras_sep= palabras.split(' ')
print("Las palabras sin caracteres de puntuación", palabras)

cant_palabras = len(palabras_sep)
print("La cantidad de palabras en el texto es: ",cant_palabras)

#3

print("Primera letra: ", palabras[0], "Ultima letra: ",palabras[-1])

#4 mostrar el texto en orden inverso

palabras_reversa = palabras.reverse()
print("El texto en forma inversa: ", palabras_reversa)

#otra forma
"""
texto_reversa = palabras[::-1]
print("El texto en forma inversa: ", texto_reversa)"""

"""para las palabras en orden inverso:
palabras_reversa = palabras_sep[:::-1] #['hola','como' , 'estas']
print("Palabras en forma inversa: ",palabras_reversa)"""

"""para las palabras en orden inverso:
texto_palabras_reversa = " " .join(palabras_reversa)
print("Palabras en forma inversa: ",texto_palabras_reversa)"""


#5)

"""if ("python" in texto):
    print("Existe python en el texto")
else:
    print("No existe python en el texto")"""

#con un diccionario:

opciones=(True:"existe", False:"no existe") #aca cree el diccionario, con true y false que son las llaves o keys o claves. Existe y No exite son valores o values
existe_python = "python" in texto #esto es una operacion booleana, que si existe la palabra en el texto

print("La palabra python",opciones[existe_python]) #







# letras_buscadas = []

# for letra in range(3):
# letras_buscadas.append(input(f"Ingrese su letra {letra+1}: ").lower()) #ahi les va un ejemplo con estructura repetitiva, en este caso un for
