PSEUDOCODIGO // TP N4 ESTRUCTURAS REPETITIVAS 
Actividad 1:
INICIO
  PARA i DESDE 0 HASTA 100 HACER
    MOSTRAR i
  FIN PARA
FIN


Actividad 2:
INICIO
  LEER numero
  convertir numero a texto
  contar cantidad de caracteres
  MOSTRAR cantidad
FIN

Actividad 3:
INICIO
  LEER numero1
  LEER numero2
  suma ← 0
  PARA i DESDE (min(numero1, numero2) + 1) HASTA (max(numero1, numero2) - 1) HACER
      suma ← suma + i
  FIN PARA
  MOSTRAR "La suma es:", suma
FIN


Actividad 4:
INICIO
  suma ← 0
  REPETIR
     LEER numero
     SI numero ≠ 0 ENTONCES
        suma ← suma + numero
     FIN SI
  HASTA QUE numero = 0
  MOSTRAR "La suma total es:", suma
FIN


Actividad 5:
INICIO
  numero_secreto ← ALEATORIO(0,9)
  intentos ← 0
  REPETIR
     LEER intento
     intentos ← intentos + 1
  HASTA QUE intento = numero_secreto
  MOSTRAR "¡Correcto! Lo adivinaste en", intentos, "intentos"
FIN

Actividad 6:
INICIO
  PARA i DESDE 100 HASTA 0 CON PASO -2 HACER
     MOSTRAR i
  FIN PARA
FIN

Actividad 7:
INICIO
  LEER n
  suma ← 0
  PARA i DESDE 0 HASTA n HACER
     suma ← suma + i
  FIN PARA
  MOSTRAR "La suma es:", suma
FIN

Actividad 8:
INICIO
  pares ← 0
  impares ← 0
  positivos ← 0
  negativos ← 0

  PARA i DESDE 1 HASTA 100 HACER
     LEER numero
     SI numero MOD 2 = 0 ENTONCES
        pares ← pares + 1
     SINO
        impares ← impares + 1
     FIN SI

     SI numero >= 0 ENTONCES
        positivos ← positivos + 1
     SINO
        negativos ← negativos + 1
     FIN SI
  FIN PARA

  MOSTRAR pares, impares, positivos, negativos
FIN

Actividad 9:
INICIO
  suma ← 0
  cantidad ← 100

  PARA i DESDE 1 HASTA cantidad HACER
     LEER numero
     suma ← suma + numero
  FIN PARA

  media ← suma / cantidad
  MOSTRAR "La media es:", media
FIN

Actividad 10:
INICIO
  LEER numero
  convertir numero a cadena
  invertido ← "" (cadena vacía)
  
  PARA i DESDE longitud(numero) HASTA 1 CON PASO -1 HACER
     invertido ← invertido + caracter_en_posicion(numero, i)
  FIN PARA

  MOSTRAR "Número invertido:", invertido
FIN
