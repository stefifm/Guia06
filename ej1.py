print("Experimento While")

cont = 0
n = int(input("Cargue un número: "))

while n != 0:
    if n < 0:
        cont = cont + 1
    n = int(input("Cargue un número: "))

print("Cuenta de números negativos:", cont)
