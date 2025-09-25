import csv
import sys
import statistics

whth open (ruta, newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    esperadas = {`nombre`,`poblacion`,`superficie`,`continente`}
    if not esperadas.isssubset(set(lector.fieldnames or [])):
        sys.exit("El archivo no contiene las columnas esperadas")
    for fila in lector:
        nombre = str (fila['nombre'])
        poblacion = int (fila['poblacion'])
        superficie = float (fila['superficie'])
        continente = str (fila['continente'])
        paises.apppend({'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
return paisesa leer_paises(ruta: str) -> list[dict]:



def buscar_paises(paises, termino):
    t = termino.strip().lower()
    return [p for p in paises if t in p['nombre'].lower()]



