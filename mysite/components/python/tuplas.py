# ¿Que sonlas tuplas?
# * Las tuplas son listas inmutables, es decir, no se pueden modificar despues de su creacion.
# * No permiten añadir, eliminar, mover elementos etc(no append, extend, remove
# * Si permiten extraer porciones, pero el resultado de la extraccion es una tupla nueva.
# * No permiten busquedas(No index)
# * Si permite comprobar si un telemento se encuentra en la tupla

# ¿Que utilidad o ventaja tiene respecto a las listas?
#  * Mas rapidad
#  * Menos espacio (mayor optimizacion)
#  * Formatean String
#  * Pueden utilizarse como claves en un diccionario. (Las listas no)

mitupla=("Jorge", 9, 4, 1974)
print(mitupla[1])

# Crear una tupla en lista
# lista es []
# tupla es ()
mitupla=("Jorge", 9, 4, 1974)
milista=list(mitupla)
print(milista)
print(mitupla)

# Crear una lista en tupla
# es con el metodo tuple
milista=["Jorge", 9, 4, 1974]
mitupla=tuple(milista)
print(mitupla)

# Para saber si un elemento esta en la tupla 
# es con el metodo in imprime true o false
milista=["Jorge", 9, 4, 1974]
mitupla=tuple(milista)
print("Jorge" in mitupla)
print("Jose" in mitupla)

# Para saber cuantos veces esta el elementos  en la tupla 
# es con el metodo count
milista=["Jorge", 9, 4, 1974, 1974]
mitupla=tuple(milista)
print(mitupla.count("Jorge"))
print(mitupla.count(1974))

# Para saber cuantos elementos hay en la tupla 
# es con el metodo len
milista=["Jorge", 9, 4, 1974, 1974]
mitupla=tuple(milista)
print(len(mitupla))

# Una tupla unitaria
# es con una coma a lo ultimo

mitupla=(milista,)
print(len(mitupla))

# la tupla no necesita de las parentesis
mitupla="Jorge", 9, 4, 1974, 1974
print(mitupla)

# Empaquetado de una tupla
mitupla=("Jorge", 9, 4, 1974, 1974)
nombre, dia, mes, agno, valor=mitupla
print(nombre, dia, mes, agno, valor)

# No se pueden agregar elementos a las tuplas
#  mitupla.append("Paco")
mitupla=("Jorge", 9, 4, 1974, 1974)
mitupla.append("Paco")
nombre, dia, mes, agno, valor=mitupla
print(nombre, dia, mes, agno, valor)