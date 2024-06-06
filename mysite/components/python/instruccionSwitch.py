# Condicional
# Switch: no existe
# Concatenacion de operadores de comparacion
# Operadores logicos "and" y "or"
# Oerador "in"


salario_presidente=int(input("Introducir salario presidente "))
print("Salario presidente: " +str(salario_presidente))

salario_director=int(input("Introducir salario director "))
print("Salario director: " +str(salario_director))

salario_jefe_area=int(input("Introducir salario jefe_area "))
print("Salario jefe_area: " +str(salario_jefe_area))

salario_administrativo=int(input("Introducir salario administrativo "))
print("Salario administrativo: " +str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")