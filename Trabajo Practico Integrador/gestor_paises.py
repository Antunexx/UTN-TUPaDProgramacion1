import csv
import os
from collections import Counter
from typing import List, Dict, Optional, Tuple

ARCHIVO_CSV = "paises.csv"
CAMPOS_CSV = ["nombre", "poblacion", "superficie", "continente"]





def menu_principal():
    try:
        paises = cargar_paises()
    except ValueError as e:
        print("Error al leer el CSV:", e)
        return

    while True:
        print("\n--- GESTIÓN DE PAÍSES (TPI) ---")
        print("1) Agregar país")
        print("2) Actualizar población/superficie")
        print("3) Buscar país por nombre")
        print("4) Filtrar países")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("7) Mostrar todos")
        print("0) Guardar y salir")
        opcion = input("Seleccione una opción: ").strip()

