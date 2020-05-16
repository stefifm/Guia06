print ("Nuevo ejemplo")

cont = 0
cont_total = 0

while cont_total < 10:
    n = int(input("Cargue un número: "))
    if n < 0:
        cont = cont + 1
    cont_total = cont_total + 1

print("Contador de negativos:",cont)