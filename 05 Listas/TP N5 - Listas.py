# Actividad 1

notas = [7, 8, 5, 10, 6, 4, 9, 7, 8, 6]

#lista con for
print("Notas de los estudiantes:")
for n in notas:
    print(n)

# Se muestra el promedio
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)


print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


# Actividad 2
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

# Muestra la lista ordenadanda alfabéticamente
print("Productos ordenados:")
for p in sorted(productos):
    print(p)

# Elimina un producto de la lista
eliminar = input("¿Qué producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
print("Lista actualizada:", productos)

# Actividad 3
import random

numeros = [random.randint(1, 100) for _ in range(15)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

#Muestra los numeros pares e impares
print("Total de pares:", len(pares))
print("Total de impares:", len(impares))

# Actividad 4
lista = [1, 2, 2, 3, 4, 4, 5]
sin_repetidos = list(set(lista))

print("Lista sin repetidos:", sin_repetidos)

# Actividad 5
estudiantes = ["Ana", "Juan", "Pedro", "Lucía", "Marta", "Sofía", "Pablo", "Diego"]

accion = input("¿Quiere agregar (a) o eliminar (e) un estudiante?: ")

if accion == "a":
    nuevo = input("Nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
elif accion == "e":
    borrar = input("Nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)

print("Lista final:", estudiantes)

# Actividad 6
numeros = [1, 2, 3, 4, 5, 6, 7]
rotada = [numeros[-1]] + numeros[:-1]

print("Lista rotada:", rotada)

# Actividad 7
temperaturas = [
    [10, 20], [12, 25], [8, 18],
    [11, 24], [9, 19], [13, 27], [7, 17]
]

prom_min = sum(dia[0] for dia in temperaturas) / 7
prom_max = sum(dia[1] for dia in temperaturas) / 7
print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)

amplitudes = [dia[1] - dia[0] for dia in temperaturas]
dia_max = amplitudes.index(max(amplitudes)) + 1
print("Mayor amplitud térmica en el día:", dia_max)

# Actividad 8
notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [8, 9, 7]
]

# Promedio por estudiante
for i, est in enumerate(notas):
    print(f"Promedio estudiante {i+1}: {sum(est)/len(est)}")

# Promedio por materia
for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    print(f"Promedio materia {j+1}: {sum(materia)/len(materia)}")

# Actividad 9
tablero = [["-"]*3 for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))

for turno in range(5):  # Máx. 5 jugadas
    mostrar_tablero()
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    jugador = "X" if turno % 2 == 0 else "O"
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada, pierdes turno")

# Actividad 10
ventas = [
    [10, 20, 15, 30, 25, 18, 22],  # Producto 1
    [5, 8, 12, 10, 14, 9, 11],     # Producto 2
    [7, 6, 5, 8, 9, 7, 6],         # Producto 3
    [20, 18, 25, 22, 24, 19, 21]   # Producto 4
]

# Total por producto
for i, prod in enumerate(ventas):
    print(f"Producto {i+1}: {sum(prod)} vendidos")

# Día con mayores ventas totales
totales_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = totales_dias.index(max(totales_dias)) + 1
print("Día con mayores ventas:", dia_max)

# Producto más vendido en la semana
totales_prod = [sum(prod) for prod in ventas]
prod_max = totales_prod.index(max(totales_prod)) + 1
print("Producto más vendido:", prod_max)

