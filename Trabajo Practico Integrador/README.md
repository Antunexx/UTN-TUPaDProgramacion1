📚 Aplicación de Biblioteca CSV


📝 Descripción

Este proyecto es un programa de consola en Python que posibilita administrar una pequeña base de datos de paises a través de un archivo CSV.  El programa posibilita la inclusión, enumeración, modificación, eliminación y análisis de los paises guardados, conservando la información en un archivo persistente.  Se creó como un trabajo práctico integrador para implementar los principios de programación estructurada, gestión de archivos y estructuras de datos en Python.


⚙️ Funcionalidades principales

Las siguientes acciones se pueden llevar a cabo desde el menú principal del programa: 

1.Agregar país:
    Permite ingresar un nuevo país con su nombre, población, superficie y continente.
    Los datos se validan antes de agregarse al archivo CSV.

2.Actualizar país:
    Permite modificar los datos de un país existente (población, superficie o continente).

3.Buscar país por nombre:
    Muestra la información completa de un país ingresado por el usuario.

4.Filtrar por continente:
    Lista todos los países pertenecientes a un continente específico.

5.Filtrar por rango de población:
    Muestra los países cuya población se encuentra dentro de un rango indicado.

6.Filtrar por rango de superficie:
    Similar a la anterior, pero según el tamaño territorial (superficie).

7.Ordenar por nombre:
    Ordena la lista de países alfabéticamente.

8.Ordenar por población:
    Ordena los países de menor a mayor (o viceversa) según su cantidad de habitantes.

9.Ordenar por superficie:
    Ordena los países por tamaño de territorio.

10.Mostrar estadísticas:
    Calcula e imprime información como:

        Promedio de población

        Promedio de superficie

        País más poblado y menos poblado

        País más grande y más pequeño

11.Mostrar todos los países:
    Lista completa con todos los países cargados en el sistema.

0.Guardar y salir:
    Guarda los cambios en el archivo paises.csv y finaliza el programa.



    
🧩 Conceptos aplicados


Los contenidos que se incluyen en este proyecto son: 
* Listas: para guardar de manera temporal los registros extraídos del archivo CSV. 
* Diccionarios: se utilizan para representar cada valor mediante claves y valores. 
* Funciones: Para modularidad, cada operación del menú se ha implementado como una función distinta. 
* Condicionales: a fin de regular el flujo del programa y verificar las opciones que el usuario introduzca. 
* Ordenamientos: posibilita la presentación de los valores en orden alfabético o por precio. 
* Estadísticas elementales: realiza cálculos de promedios, máximos/mínimos y totales. 
* Archivos CSV: lectura y escritura de datos mediante el módulo estándar csv de Python.


🧠 Requisitos previos

Python 3.10 o superior

🚀 Cómo ejecutar el programa

Clonar el repositorio o descargar los archivos.

Abrir una terminal en el directorio del proyecto.

Ejecutar el siguiente comando:

python gestor_paises.py


Seguir las instrucciones del menú.



🧾 Autor

Agustín Nicolás Quintero
Estudiante de la Tecnicatura en programacion en la Universidad Tecnológica Nacional Regional San Nicolas
📍 Córdoba, Argentina