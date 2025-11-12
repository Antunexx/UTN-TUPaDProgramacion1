


# ---------- Ruta del archivo CSV ----------
def ruta_csv_local():
    # Construye la ruta del CSV situada en la misma carpeta que este script,
    # Si por algún motivo __file__ no está definido, devuelve "paises.csv".
    if "__file__" not in globals():
        return "paises.csv"
    ruta = __file__
    sep = "\\"
    if "/" in ruta and "\\" not in ruta:
        sep = "/"
    if sep in ruta:
        partes = ruta.rsplit(sep, 1)
        if len(partes) == 2:
            carpeta = partes[0]
            return carpeta + sep + "paises.csv"
    return "paises.csv"


# ---------- Normalización / validación ----------
def quitar_tildes(texto):
    # reemplaza vocales acentuadas y la ñ por su equivalente simple
    texto = texto.replace("Á", "A")
    texto = texto.replace("É", "E")
    texto = texto.replace("Í", "I")
    texto = texto.replace("Ó", "O")
    texto = texto.replace("Ú", "U")
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("Ñ", "N")
    texto = texto.replace("ñ", "n")
    texto = texto.replace("ü", "u")
    texto = texto.replace("Ü", "U")
    return texto


def normalizar_texto(texto):
    texto = texto.strip()
    # reducir múltiples espacios a uno solo
    while "  " in texto:
        texto = texto.replace("  ", " ")
    return texto


def normalizar_para_buscar(texto):
    texto = normalizar_texto(texto)
    texto = quitar_tildes(texto)
    texto = texto.lower()
    return texto


def es_numero_entero_valido(texto):
    # Acepta números escritos con puntos como separador de miles o espacios:
    # "1.234.567" o "1 234 567" o "1234567"
    if texto == "":
        return False
    s = texto.strip()
    s = s.replace(".", "")
    s = s.replace(" ", "")
    if s == "":
        return False
    for c in s:
        if c not in "0123456789":
            return False;
    return True


def convertir_entero(texto):
    s = texto.strip()
    s = s.replace(".", "")
    s = s.replace(" ", "")
    # asumimos que se llamó convertidor solo después de validar con es_numero_entero_valido
    return int(s)


# ---------- Funciones de archivo ----------
def cargar_paises():
    lista_paises = []
    ruta = ruta_csv_local()
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read().splitlines()
    archivo.close()

    if len(contenido) == 0:
        # archivo vacío
        return lista_paises

    primera = contenido[0].strip()
    primera_minus = primera.lower()

    tiene_encabezado = False
    # consideramos que hay encabezado si contiene las palabras esperadas
    if "nombre" in primera_minus and "poblacion" in primera_minus and "superficie" in primera_minus:
        tiene_encabezado = True

    if tiene_encabezado:
        lineas_datos = contenido[1:]
    else:
        # consideramos que la primera línea es dato normal
        lineas_datos = contenido

    for linea in lineas_datos:
        if linea.strip() == "":
            continue
        partes = linea.split(",")
        # aceptar si hay al menos 4 columnas; tomar las primeras 4
        if len(partes) >= 4:
            raw_nombre = partes[0].strip()
            raw_poblacion = partes[1].strip()
            raw_superficie = partes[2].strip()
            raw_continente = partes[3].strip()

            # validar números 
            if es_numero_entero_valido(raw_poblacion) and es_numero_entero_valido(raw_superficie):
                pobl = convertir_entero(raw_poblacion)
                sup = convertir_entero(raw_superficie)
                lista_paises.append({
                    "nombre": raw_nombre,
                    "poblacion": pobl,
                    "superficie": sup,
                    "continente": raw_continente
                })
            else:
                
                pass
        else:
            pass

    return lista_paises


def guardar_paises(lista_paises):
    ruta = ruta_csv_local()
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("nombre,poblacion,superficie,continente\n")
    for pais in lista_paises:
        linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"
        archivo.write(linea)
    archivo.close()


# ---------- CRUD ----------
def agregar_pais(lista_paises):
    nombre = input("Nombre del país: ")
    nombre = normalizar_texto(nombre)
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

        # verificar si ya existe (comparación exacta normalizada)
    nombre_busq = normalizar_para_buscar(nombre)
    for p in lista_paises:
        if normalizar_para_buscar(p["nombre"]) == nombre_busq:
            print("El país ya existe (coincidencia encontrada).")
            return

    poblacion = input("Población: ")
    if not es_numero_entero_valido(poblacion):
        print("Población inválida.")
        return

    superficie = input("Superficie (km²): ")
    if not es_numero_entero_valido(superficie):
        print("Superficie inválida.")
        return

    continente = input("Continente: ")
    continente = normalizar_texto(continente)
    if continente == "":
        print("El continente no puede estar vacío.")
        return

    lista_paises.append({
        "nombre": nombre,
        "poblacion": convertir_entero(poblacion),
        "superficie": convertir_entero(superficie),
        "continente": continente
    })
    print("País agregado correctamente.")
    guardar_paises(lista_paises)


def buscar_pais_por_nombre(lista_paises):
    texto = input("Texto a buscar: ")
    texto = normalizar_para_buscar(texto)
    encontrados = []
    for p in lista_paises:
        if texto in normalizar_para_buscar(p["nombre"]):
            encontrados.append(p)
    if len(encontrados) == 0:
        print("No se encontraron coincidencias.")
    else:
        mostrar_paises(encontrados)


def actualizar_pais(lista_paises):
    nombre = input("Nombre exacto del país a actualizar: ")
    nombre = normalizar_texto(nombre)
    if nombre == "":
        print("Nombre vacío.")
        return

    # buscar índice
    indice = -1
    nombre_busq = normalizar_para_buscar(nombre)
    for i in range(len(lista_paises)):
        if normalizar_para_buscar(lista_paises[i]["nombre"]) == nombre_busq:
            indice = i
            break

    if indice == -1:
        print("País no encontrado.")
        return

    print("Deje vacío si no desea cambiar el valor.")
    nueva_poblacion = input("Nueva población: ")
    if nueva_poblacion != "":
        if not es_numero_entero_valido(nueva_poblacion):
            print("Población inválida.")
            return
        lista_paises[indice]["poblacion"] = convertir_entero(nueva_poblacion)

    nueva_superficie = input("Nueva superficie: ")
    if nueva_superficie != "":
        if not es_numero_entero_valido(nueva_superficie):
            print("Superficie inválida.")
            return
        lista_paises[indice]["superficie"] = convertir_entero(nueva_superficie)

    print("Datos actualizados correctamente.")
    guardar_paises(lista_paises)


# ---------- Filtros ----------
def filtrar_por_continente(lista_paises):
    continente = input("Continente: ")
    continente_norm = normalizar_para_buscar(continente)
    resultado = []
    for p in lista_paises:
        if normalizar_para_buscar(p["continente"]) == continente_norm:
            resultado.append(p)
    if len(resultado) == 0:
        print("Sin coincidencias.")
    else:
        mostrar_paises(resultado)


def filtrar_por_rango_poblacion(lista_paises):
    print("Rango de población:")
    minimo = input("Mínimo: ")
    maximo = input("Máximo: ")

    min_ok = minimo == "" or es_numero_entero_valido(minimo)
    max_ok = maximo == "" or es_numero_entero_valido(maximo)

    if not min_ok or not max_ok:
        print("Valores inválidos.")
        return

    min_val = convertir_entero(minimo) if minimo != "" else 0
    max_val = convertir_entero(maximo) if maximo != "" else 999999999999

    if min_val > max_val:
        print("El mínimo no puede ser mayor que el máximo.")
        return

    resultado = []
    for p in lista_paises:
        if min_val <= p["poblacion"] <= max_val:
            resultado.append(p)
    mostrar_paises(resultado)


def filtrar_por_rango_superficie(lista_paises):
    print("Rango de superficie:")
    minimo = input("Mínimo: ")
    maximo = input("Máximo: ")

    min_ok = minimo == "" or es_numero_entero_valido(minimo)
    max_ok = maximo == "" or es_numero_entero_valido(maximo)

    if not min_ok or not max_ok:
        print("Valores inválidos.")
        return

    min_val = convertir_entero(minimo) if minimo != "" else 0
    max_val = convertir_entero(maximo) if maximo != "" else 999999999999

    if min_val > max_val:
        print("El mínimo no puede ser mayor que el máximo.")
        return

    resultado = []
    for p in lista_paises:
        if min_val <= p["superficie"] <= max_val:
            resultado.append(p)
    mostrar_paises(resultado)


# ---------- Orden----------
def ordenar_por_nombre(lista_paises):
    n = len(lista_paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if normalizar_para_buscar(lista_paises[i]["nombre"]) > normalizar_para_buscar(lista_paises[j]["nombre"]):
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

    mayor = lista_paises[0]
    menor = lista_paises[0]
    suma_pob = 0
    suma_sup = 0
    por_cont = {}

    for p in lista_paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p
        suma_pob += p["poblacion"]
        suma_sup += p["superficie"]
        cont = p["continente"]
        if cont in por_cont:
            por_cont[cont] += 1
        else:
            por_cont[cont] = 1

    prom_pob = suma_pob // len(lista_paises)
    prom_sup = suma_sup // len(lista_paises)

    print("País con mayor población:", mayor["nombre"], "-", mayor["poblacion"])
    print("País con menor población:", menor["nombre"], "-", menor["poblacion"])
    print("Promedio de población:", prom_pob)
    print("Promedio de superficie:", prom_sup)
    print("Cantidad de países por continente:")
    for c in por_cont:
        print("  ", c, ":", por_cont[c])


# ---------- Mostrar ----------
def mostrar_paises(lista_paises):
    if len(lista_paises) == 0:
        print("Lista vacía.")
        return
    print("NOMBRE".ljust(25), "POBLACIÓN".rjust(12), "SUPERFICIE".rjust(12), "CONTINENTE")
    print("-" * 70)
    for p in lista_paises:
        print(p["nombre"].ljust(25), str(p["poblacion"]).rjust(12), str(p["superficie"]).rjust(12), p["continente"])


# ---------- Menú ----------
def menu():
    lista_paises = cargar_paises()
    while True:
        print("\n--- MENÚ DE PAÍSES ---")
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


# Punto de entrada
menu()
