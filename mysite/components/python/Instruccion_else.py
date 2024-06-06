# condicional else
# else = y si  no es verdad

print("Verificacion de acceso")

edad_usuario = int(input("Introduce una edad, por favor ")) 

if edad_usuario < 18:

    print("No puedes pasar")

elif edad_usuario > 100:

    print("Edad incorrecta")

else:

    print("Puedes pasar")

print("El programa a fnalizado")
