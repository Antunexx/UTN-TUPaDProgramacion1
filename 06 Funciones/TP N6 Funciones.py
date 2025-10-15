#Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Actividad 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# Actividad 3

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))

# Actividad 4
def calcular_area_circulo(radio):
    return 3.1416 * radio * radio
pass
def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio   
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese el número de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# Actividad 6   

def tabla_multiplicar(numero):
    return [numero * i for i in range(1, 11)]
numero = int(input("Ingrese un número para ver su tabla de multiplicar: ")) 
print(f"Tabla de multiplicar del {numero}: {tabla_multiplicar(numero)}")

# Actividad 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return suma, resta, multiplicacion, division
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Actividad 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc}")

# Actividad 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

# Actividad 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingrese la primera nota: "))
b = float(input("Ingrese la segunda nota: "))
c = float(input("Ingrese la tercera nota: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de las notas es: {promedio}")