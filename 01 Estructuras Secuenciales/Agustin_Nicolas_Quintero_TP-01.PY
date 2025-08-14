#Agustin Nicolas Quintero
#DNI 42258204


#Actividad 1
print ("Hola Mundo!")


#Actividad 2

nombre = str(input("Ingrese su nombre :"))

print(f"Hola {nombre} !")


#Actividad 3

Nombre = str(input("Ingrese su nombre :"))
apellido = str(input("Ingrese su Apellido :"))
edad = int(input("Ingrese su edad :"))
residencia = str(input("Ingrese el nombre del pais en el que reside :"))

print (f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia}")

#Actividad 4
pi= 3.14159
radio = float(input("Por favor ingrese el radio: "))

area = pi * radio**2
perimetro = 2 * pi * radio

print(f"El area es {area}")
print(f"El perimetro es {perimetro}")

#Actividad 5

segundos = int(input("Por favor ingrese los segundos: "))

horas = segundos / 3600

print(f"esto equivale a {horas} en horas")

#Actividad 6

numerobase = int(input("Ingrese el numero que le gustaria saber su tabla:"))

print(f"La tabla de multiplicar del {numerobase} es : ")
print( numerobase *  1 )
print( numerobase *  2 )
print( numerobase *  3 )
print( numerobase *  4 )
print( numerobase *  5 )
print( numerobase *  6 )
print( numerobase *  7 )
print( numerobase *  8 )
print( numerobase *  9 )
print( numerobase *  10 )

#Actividad 7

Numero1=int(input("Por favor un numero distinto de 0 : "))
Numero2=int(input("Por favor un numero distinto de 0 : "))

suma = Numero1 + Numero2
division= Numero1 / Numero2
multiplicacion= Numero1 * Numero2
resta= Numero1 - Numero2

print (f"El resultado de sumarlos es : {suma} ")
print (f"El resultado de dividirlos es : {division} ")
print (f"El resultado de multiplicarlos es : {multiplicacion} ")
print (f"El resultado de restarlos es : {resta} ")


#Actividad 8

altura = float(input("Ingrese su altura(Expresado en Metros) : "))
peso = float(input("Ingrese su peso (expresado en kilogramos): "))

IMC = peso / (altura**2)

print(f" Su IMC es : {IMC} ")

#Actividad 9


celsius = float(input("Por favor ingrese la tempratura medida en celsius: "))

fahrenheit = (9/5) * celsius + 32

print (f"La temperatura en Fahrenheit es de : {fahrenheit} ")


#Actividad 9

numero1=int(input("Por favor su primer numero : "))
numero2=int(input("Por favor su segundo numero : "))
numero3=int(input("Por favor su tercer numero  : "))

promedio = (numero1 + numero2 + numero3)/3

print(f"El promedio de los tres numeros ingresados es de {promedio} ")