# Operadores logicos "and" y "or"
# Un ejemplo donde los estudiantes que vivan a una distancis mayor de 40 y que sean 2 o mas hermanos y que el salariosea sea menor o igual 20000
# distancia > 40 Km 
# numero de hermanos > 2 
# salario familiar <= 20000

print("Programa de becas Año")
distacia_escuela=int(input("Introduce la distancia a la escuela en km "))
print(distacia_escuela)

numeros_hermanos=int(input("Introduce el No de hermanos en el centro "))
print(numeros_hermanos)

salario_familiar=int(input("Introduce el salario anual bruto "))
print(salario_familiar)

if distacia_escuela>40 and numeros_hermanos>2 or salario_familiar<=200000:
    print("Tienes derecho a beca")
else:
    print("No tienes derechos a beca")