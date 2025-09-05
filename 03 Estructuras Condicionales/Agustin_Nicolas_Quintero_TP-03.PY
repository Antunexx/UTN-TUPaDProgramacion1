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
