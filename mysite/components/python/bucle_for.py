# <!-- Bucles for:
# el bucle consta de dos partes
# declaracion
# cuerpo

# -Determinados
# * Se ejecutan un numero determinado de veces
# * Se sabe a priori cuantas veces se va a ejecutar el codigo del  interior del Bucle

# Bucle for (determinado). Sintaxis
#     for variabe in elementosa recorrer: "Los elementos pueden ser listas, tuplas, cadenas de texto"

#     el cuerpo del bucle es el codigoy tiene una identacion(una seperacion) y tener varias lineas de codigo



# -Indeterminados 
# * Se ejecutan un numero indeterminado de veces
# * No se sabe a priori cuantas veces se va a ejecutar el codigo * del interior delbucle.
# * El numero de veces que se ejecutara dependera de las circunstancias durante la ejecucion del programa
# * Bucle for
# es repetir codigo -->

from logging import StringTemplateStyle
from re import T


for i in[1,2,3]:
    print("Hola")

for i in["Primavera","Verano","otoño","invierno"]:
    print("Hola")

for i in["Primavera","Verano","otoño","invierno"]:
    print(i)

# Bucle for
# * Recorriendo String
for i in "georgechir@hotmail.com.co":
    print("Hola", end="")
# * Tipo booleano 
email=False
for i in "georgechir@hotmail.com.co":
    if (i=="@"):
        email=True
if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")

# * Notaciones  con print
email=False
miEmail=input("Introduce ti direccion de email: ")

for i in "georgechir@hotmail.com.co":
    if (i=="@"):
        email=True
if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")

#  *tipo range
for i in range (5):
    print(f"Vaolr de la variable {i}")

for i in range (5,50,3):
    print(f"Vaolr de la variable {i}")

# funccion len cuenta los caracteres de una string
valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")