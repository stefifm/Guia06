print("Notas de un alumno")

n1 = int(input("Ingrese Nota Parcial 1: "))
n2 = int(input("Ingrese Nota Parcial 2: "))
n3 = int(input("Ingrese Nota Parcial 3: "))
np = int(input("Ingrese Nota Prácticos: "))

p_aprobados = 0
if n1 >= 4:
    p_aprobados = p_aprobados + 1
if n2 >= 4:
    p_aprobados = p_aprobados + 1
if n3 >= 4:
    p_aprobados = p_aprobados + 1

promedio = (n1 + n2 + n3) / 3

alumno = "Regular"
if p_aprobados < 2 or np < 4:
    alumno = "Libre"
else:
    if n1 >= 7 and n2 >= 7 and n3 >= 7 and np >= 8:
        if promedio >= 9:
            alumno = "Aprobado"
        else:
            if promedio >= 8:
                alumno = "Promocionado"

print("El promedio del alumno es:",promedio)
print("La condición del alumno:",alumno)