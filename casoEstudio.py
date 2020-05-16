print("Cantidad de coches de estudio")

n = int(input("Cargue número mensual de ventas: "))

cant10000 = 0
cant15000 = 0
catMay15000 = 0
acu_n = 0
hay_ceros = False
while n != -1:
    if n >= 0 and n < 10000:
        cant10000 = cant10000 + 1
    else:
        if n >= 10000 and n < 15000:
            cant15000 = cant15000 + 1
        else:
            if n >= 15000:
                catMay15000 = catMay15000 + 1
    if n >= 0:
        acu_n = acu_n + n
    if n == 0:
        hay_ceros = True
    n = int(input("Cargue número mensual de ventas: "))

print("Cantidad de coches vendidos entre 0 y 10000:", cant10000)
print("Cantidad de coches vendidos entre 10000 y 15000:", cant15000)
print("Cantidad de coches vendidos mayor a 15000:", catMay15000)
print("Cantiodad total de coches vendidos:",acu_n)
if hay_ceros == True:
    print("Si hay ventas en cero")
else:
    print("No hay ventas en cero")