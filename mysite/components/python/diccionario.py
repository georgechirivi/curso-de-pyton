# ¿Que son los diccionarios?
# * Estructura de datos que nos permiten almacenar valores de diferentes tipo (enteros, cadenas de texto, decimales) e inclusolistas y otros diccionarios.
# * La principal caracteristicas de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociacion de tipo clave: valor para cada elemento almacenado.
# * Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar informacio en un diccionario.

midiccionario={"Alemania":"Berlin", "España":"Madrid", "Reino Unido":"Londres", "Francia":"Paris"}
print(midiccionario["Francia"])

# Para imprimir todo el diccionario
midiccionario={"Alemania":"Berlin", "España":"Madrid", "Reino Unido":"Londres", "Francia":"Paris"}
print(midiccionario)

# Para agregar un elemento mas
midiccionario={"Alemania":"Berlin", "España":"Madrid", "Reino Unido":"Londres", "Francia":"Paris"}
midiccionario["Italia"]="Roma"
print(midiccionario)

# Para modificar un valor
midiccionario={"Alemania":"Berlin", "España":"Madrid", "Reino Unido":"Londres", "Francia":"Paris"}
midiccionario["Italia"]="Bogota"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)

# Como eliminar unelemento
midiccionario={"Alemania":"Berlin", "España":"Madrid", "Reino Unido":"Londres", "Francia":"Paris"}
del midiccionario["Alemania"]
print(midiccionario)

# se pueden crear un diccionaro con diferentes valores
midiccionario={"Alemani":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario)

# Para tomar valores de otra cadena
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario)
print(midiccionario["Alemania"])

# Agregar un valor al diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario)
print(midiccionario["anillos"])

# Guardar un diccionariodentro de otro diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario["anillos"])
print(midiccionario)

# metodos keys
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())

# metodo values
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.values())

# Longitud del diccionario
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(len(midiccionario))



