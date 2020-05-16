print("Complejo de cines")

#datos
espectadores = int(input("Número de espectadores (cierra en 0: "))
recaudacion = 0
funciones = 0
fun_descuento = 0
while espectadores != 0:
    descuento = input("Hay descuento? (S/N): ")
    if descuento == "S":
        precio = 50
        fun_descuento += 1
    else:
        precio = 75
    recaudacion = recaudacion + (espectadores * 50)
    funciones += 1
    espectadores = int(input("Número de espectadores (cierra en 0: "))

if funciones != 0:
    porcentaje = (fun_descuento * 100) / funciones
else:
    porcentaje = 0

#resultado
print("La recaudación es:",recaudacion)
print("Cantidad de funciones con descuento:",fun_descuento)
print(("Porcentaje de funciones con descuento:",porcentaje))

