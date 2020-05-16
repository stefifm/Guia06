#Ingresar de a uno una serie de números. Encontrar e imprimir el mayor de todos
# los números pares cuyo número de orden sea par, el proceso terminará cuando
# el número leído sea igual a cero


print("Numeros impares y pares")

#Datos
n = int(input("Ingrese un número (corta en 0): "))
orden = 0
mayor = None
#proceso
while n != 0:
    if orden % 2 == 0 and n % 2 == 0:
        if mayor is None or n > mayor:
            mayor = n
    orden += 1
    n = int(input("Ingrese un número (corta en 0): "))

if not mayor is None:
    print("Mayor par del orden es:",mayor)
else:
    print("No hay números pares")



