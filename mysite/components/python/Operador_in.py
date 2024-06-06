# Operador "in"
# un alumno que tiene escoger una materia optativa y sele da un listado para escoger

print("Asignaturas de materia optativas")
print("Asignaturas optativas:Informatica_graficas - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escriba la asignatura escogida? ")
asignatura=opcion.lower()

if asignatura in("Informatica grafica", "Pruebas de software", "Usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asigantura escogida no esta contemplada")