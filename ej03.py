print("Mayor de una suceción de valores")
may = None
n = int(input("Cantidad de números a procesar: "))
for i in range(n):
    num = int(input("Ingrese un número: "))
    if i == 0 or num > may:
        may = num
print("El mayor es:",may)
