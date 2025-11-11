import csv
import os

# ---------- Funciones de archivo ----------
def cargar_paises():
    lista_paises = []
    archivo = open("paises.csv", "r", encoding="utf-8")
    linea = archivo.readline()
    if linea == "":
        archivo.close()
        return lista_paises

    encabezado = linea.strip().split(",")
    if encabezado != ["nombre", "poblacion", "superficie", "continente"]:
        print("Encabezado incorrecto.")
        archivo.close()
        return lista_paises

    linea = archivo.readline()
    while linea != "":
        partes = linea.strip().split(",")
        if len(partes) == 4:
            nombre = partes[0].strip()
            poblacion = partes[1].strip()
            superficie = partes[2].strip()
            continente = partes[3].strip()

            if nombre.isdigit() == False and poblacion.isdigit() and superficie.isdigit():
                lista_paises.append({
                    "nombre": nombre,
                    "poblacion": int(poblacion),
                    "superficie": int(superficie),
                    "continente": continente
                })
        linea = archivo.readline()

    archivo.close()
    return lista_paises


def guardar_paises(lista_paises):
    archivo = open("paises.csv", "w", encoding="utf-8")
    archivo.write("nombre,poblacion,superficie,continente\n")
    for pais in lista_paises:
        archivo.write(pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n")
    archivo.close()


# ---------- Validaciones ----------
def es_numero_positivo(texto):
    if texto == "":
        return False
    for caracter in texto:
        if caracter not in "0123456789":
            return False
    return int(texto) >= 0


def normalizar_texto(texto):
    texto = texto.strip()
    while "  " in texto:
        texto = texto.replace("  ", " ")
    return texto


# ---------- CRUD ----------
def agregar_pais(lista_paises):
    nombre = input("Nombre del país: ")
    nombre = normalizar_texto(nombre)
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print("El país ya existe.")
            return

    poblacion = input("Población: ")
    if not es_numero_positivo(poblacion):
        print("Población inválida.")
        return

    superficie = input("Superficie (km²): ")
    if not es_numero_positivo(superficie):
        print("Superficie inválida.")
        return

    continente = input("Continente: ")
    continente = normalizar_texto(continente)
    if continente == "":
        print("El continente no puede estar vacío.")
        return

    lista_paises.append({
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    })
    print("País agregado correctamente.")
    guardar_paises(lista_paises)


def buscar_pais_por_nombre(lista_paises):
    texto = input("Texto a buscar: ")
    texto = normalizar_texto(texto).lower()
    paises_encontrados = []

    for pais in lista_paises:
        if texto in pais["nombre"].lower():
            paises_encontrados.append(pais)

    if len(paises_encontrados) == 0:
        print("No se encontraron coincidencias.")
    else:
        mostrar_paises(paises_encontrados)


def actualizar_pais(lista_paises):
    nombre = input("Nombre exacto del país a actualizar: ")
    nombre = normalizar_texto(nombre)
    indice = -1

    for i in range(len(lista_paises)):
        if lista_paises[i]["nombre"].lower() == nombre.lower():
            indice = i
            break

    if indice == -1:
        print("País no encontrado.")
        return

    print("Deje vacío si no desea cambiar el valor.")

    nueva_poblacion = input("Nueva población: ")
    if nueva_poblacion != "":
        if not es_numero_positivo(nueva_poblacion):
            print("Población inválida.")
            return
        lista_paises[indice]["poblacion"] = int(nueva_poblacion)

    nueva_superficie = input("Nueva superficie: ")
    if nueva_superficie != "":
        if not es_numero_positivo(nueva_superficie):
            print("Superficie inválida.")
            return
        lista_paises[indice]["superficie"] = int(nueva_superficie)

    print("Datos actualizados correctamente.")
    guardar_paises(lista_paises)


# ---------- Filtros ----------
def filtrar_por_continente(lista_paises):
    continente = input("Continente: ")
    continente = normalizar_texto(continente).lower()
    resultado = []

    for pais in lista_paises:
        if pais["continente"].lower() == continente:
            resultado.append(pais)

    if len(resultado) == 0:
        print("Sin coincidencias.")
    else:
        mostrar_paises(resultado)


def filtrar_por_rango_poblacion(lista_paises):
    print("Rango de población:")
    minimo = input("Mínimo: ")
    maximo = input("Máximo: ")

    minimo_valido = minimo == "" or es_numero_positivo(minimo)
    maximo_valido = maximo == "" or es_numero_positivo(maximo)

    if not minimo_valido or not maximo_valido:
        print("Valores inválidos.")
        return

    minimo = int(minimo) if minimo != "" else 0
    maximo = int(maximo) if maximo != "" else 999999999999

    if minimo > maximo:
        print("El mínimo no puede ser mayor que el máximo.")
        return

    resultado = []
    for pais in lista_paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)

    mostrar_paises(resultado)


def filtrar_por_rango_superficie(lista_paises):
    print("Rango de superficie:")
    minimo = input("Mínimo: ")
    maximo = input("Máximo: ")

    minimo_valido = minimo == "" or es_numero_positivo(minimo)
    maximo_valido = maximo == "" or es_numero_positivo(maximo)

    if not minimo_valido or not maximo_valido:
        print("Valores inválidos.")
        return

    minimo = int(minimo) if minimo != "" else 0
    maximo = int(maximo) if maximo != "" else 999999999999

    if minimo > maximo:
        print("El mínimo no puede ser mayor que el máximo.")
        return

    resultado = []
    for pais in lista_paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    mostrar_paises(resultado)


# ---------- Orden ----------
def ordenar_por_nombre(lista_paises):
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista_paises[i]["nombre"] > lista_paises[j]["nombre"]:
                lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]
    mostrar_paises(lista_paises)


def ordenar_por_poblacion(lista_paises):
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista_paises[i]["poblacion"] > lista_paises[j]["poblacion"]:
                lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]
    mostrar_paises(lista_paises)


def ordenar_por_superficie(lista_paises):
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista_paises[i]["superficie"] > lista_paises[j]["superficie"]:
                lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]
    mostrar_paises(lista_paises)


# ---------- Estadísticas ----------
def mostrar_estadisticas(lista_paises):
    if len(lista_paises) == 0:
        print("No hay datos.")
        return

    pais_mayor = lista_paises[0]
    pais_menor = lista_paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    paises_por_continente = {}

    for pais in lista_paises:
        if pais["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = pais
        if pais["poblacion"] < pais_menor["poblacion"]:
            pais_menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]
        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion // len(lista_paises)
    promedio_superficie = suma_superficie // len(lista_paises)

    print("País con mayor población:", pais_mayor["nombre"], "-", pais_mayor["poblacion"])
    print("País con menor población:", pais_menor["nombre"], "-", pais_menor["poblacion"])
    print("Promedio de población:", promedio_poblacion)
    print("Promedio de superficie:", promedio_superficie)
    print("Cantidad de países por continente:")
    for cont in paises_por_continente:
        print("  ", cont, ":", paises_por_continente[cont])


# ---------- Mostrar ----------
def mostrar_paises(lista_paises):
    if len(lista_paises) == 0:
        print("Lista vacía.")
        return

    print("NOMBRE".ljust(20), "POBLACIÓN".rjust(12), "SUPERFICIE".rjust(12), "CONTINENTE")
    print("-" * 60)
    for pais in lista_paises:
        print(pais["nombre"].ljust(20), str(pais["poblacion"]).rjust(12), str(pais["superficie"]).rjust(12), pais["continente"])


# ---------- Menú principal ----------
def menu():
    lista_paises = cargar_paises()
    while True:
        print("\n--- MENÚ DE PAISES ---")
        print("1) Agregar país")
        print("2) Actualizar país")
        print("3) Buscar país por nombre")
        print("4) Filtrar por continente")
        print("5) Filtrar por rango de población")
        print("6) Filtrar por rango de superficie")
        print("7) Ordenar por nombre")
        print("8) Ordenar por población")
        print("9) Ordenar por superficie")
        print("10) Mostrar estadísticas")
        print("11) Mostrar todos los países")
        print("0) Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(lista_paises)
        elif opcion == "2":
            actualizar_pais(lista_paises)
        elif opcion == "3":
            buscar_pais_por_nombre(lista_paises)
        elif opcion == "4":
            filtrar_por_continente(lista_paises)
        elif opcion == "5":
            filtrar_por_rango_poblacion(lista_paises)
        elif opcion == "6":
            filtrar_por_rango_superficie(lista_paises)
        elif opcion == "7":
            ordenar_por_nombre(lista_paises)
        elif opcion == "8":
            ordenar_por_poblacion(lista_paises)
        elif opcion == "9":
            ordenar_por_superficie(lista_paises)
        elif opcion == "10":
            mostrar_estadisticas(lista_paises)
        elif opcion == "11":
            mostrar_paises(lista_paises)
        elif opcion == "0":
            guardar_paises(lista_paises)
            print("Datos guardados correctamente. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


menu()
