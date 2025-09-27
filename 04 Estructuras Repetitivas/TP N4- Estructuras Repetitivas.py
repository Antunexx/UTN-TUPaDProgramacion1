#Actividad 1

for i in range(0, 101):
    print(i)
    

#Actividad 2

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))  
print("El número tiene", cantidad_digitos, "dígitos")


#Actividad 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i

print("La suma es:", suma)


#Actividad 4
suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)


#Actividad 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0 a 9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Lo adivinaste en", intentos, "intentos")
        break


#Actividad 6
for i in range(100, -1, -2):
    print(i)


#Actividad 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

#Actividad 8
pares = impares = positivos = negativos = 0

for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Actividad 9
suma = 0
cantidad = 100

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad
print("La media es:", media)

#Actividad 10

num = input("Ingrese un número: ")
invertido = num[::-1]
print("Número invertido:", invertido)
