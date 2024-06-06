# # Que son las listas?
# import array
# * Estructuras de datos que nos permite almacenar gran cantidad de valores (equivalentes a los arrayen otros lenguajes de programacion)
# * En python las listas pueden guardar diferentes tipo de valores en otrso lenguajes no ocurre esto con los array
# * Se pueden expandir dinamicamente añadiendo nuevos elelmentos (otranovedad respecto alos arrays en otros lenguajes)

# Sintasis de las listas
# nombrelista 0 [elem1, elem2, elem3 ....]
#                  0       1      2

miLista = ["Maria", "Pepe", "Martha", "Antonio"]
#            0        1       2          3
print(miLista[2])

# Porcion de lista
print(miLista[0:3])
print(miLista[2:])
print(miLista[0:3])

# Agregar elementos
miLista.append("Jose")
print(miLista[:])

# Agregar elementos de acuerdo a la posicion
miLista.insert(1,"Edgar")
print(miLista[:])

# Agregar varios elementos
miLista.extend(["Jorge", "Luis", "Bertha"])
print(miLista[:])

# Saber la posicion
print(miLista.index("Antonio"))

# Saber si esta el elemento true o false
print("Jorge" in miLista)
print("Fernando" in miLista)

# Eliminar elementos elementos
miLista.remove("Luis")
print(miLista[:])

# Eliminar ultimo elementos
miLista.pop()
print(miLista[:])


# Agregar otra lista
miLista2 = ["Rita", "Alexandra"]
miLista3 = miLista + miLista2
print(miLista3)

# signo * multiplicador
miLista = ["Maria", "Pepe", "Martha", "Antonio"] * 3
print(miLista[:])