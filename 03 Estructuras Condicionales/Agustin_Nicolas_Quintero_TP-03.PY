Edad_Usuario = int(input("Ingrese su edad: "))
if Edad_Usuario >= 18:
    print("Usted es mayor de edad")
else:
    pass

# Fin del Programa

# ACTIVIDAD 2
Nota_Usuario = int(input("Ingrese su nota: "))
if Nota_Usuario >= 6:
    print("aprobado")
elif Nota_Usuario < 6:
    print("desaprobado")
else:
    pass

# ACTIVIDAD 3
Numero_PAR = int(input("Ingrese un numero: "))
if Numero_PAR % 2 == 0:
    print("El numero es PAR")
elif Numero_PAR % 2 != 0:
    print("El numero es IMPAR")
else:
    pass

# Actividad 4
Edad = int(input("Ingrese su edad: "))
if Edad < 12:
    print("Usted es un niño")
elif Edad >= 12 and Edad < 18:
    print("Usted es un adolescente")
elif Edad >= 18 and Edad < 30:
    print("Usted es un adulto joven")
elif Edad >= 30 :
    print("Usted es un adulto")
else:
    pass

# ACTIVIDAD 5
contraseña = input("Ingrese su contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña valida")
else:
    print("Contraseña invalida")

# ACTIVIDAD 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1 , 100) for i in range(50)]

mean(numeros_aleatorios)
median(numeros_aleatorios)
mode(numeros_aleatorios)
print("El promedio es: ", mean(numeros_aleatorios))
print("La mediana es: ", median(numeros_aleatorios))
print("La moda es: ", mode(numeros_aleatorios))


# ACTIVIDAD 7
frase = input("Ingrese una frase: ")
if frase and frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# ACTIVIDAD 8

Nombre = input("Ingrese su nombre: ")
print("Opción 1: Su nombre en mayúsculas")
print("Opción 2: Su nombre en minúsculas")
print("Opción 3: Su nombre con la primera letra mayúscula")
      
opcion = input("Ingrese una opcion (1, 2 o 3): ")
if opcion == "1":
    print(Nombre.upper())
elif opcion == "2":
    print(Nombre.lower())   
elif opcion == "3":
    print(Nombre.title())
else:
    print("Opción inválida")


# ACTIVIDAD 9

terremoto = float(input("Ingrese la magnitud del terremoto: "))
if terremoto < 3.0:
    print("Muy leve(imperceptible)")
elif terremoto >= 3.0 and terremoto < 4.0:
    print("Leve(ligeramente perceptible)")
elif terremoto >= 4.0 and terremoto < 5.0:
    print("Moderado(sentido por personas, perogeneralmente no causan daños)")
elif terremoto >=5.0 and terremoto <6.0:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif terremoto >=6.0 and terremoto <7.0:
    print("Muy Fuerte (puede causar daños significativos).")
elif terremoto >=7.0:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    pass


# ACTIVIDAD 10
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

if hemisferio == "N":
    print("La estación es:", estacion_norte)
elif hemisferio == "S":
    print("La estación es:", estacion_sur)
else:
    print("Hemisferio inválido")