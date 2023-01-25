# -*- coding: utf-8 -*-
# Teoría de la Computación - ESCOM IPN - Genaro Juarez
# Librerias
from datetime import timedelta
from enum import auto
import random
from random import randint
import string
import time
import turtle

# Esta maquina de turing está basada en la máquina de la tabla 1 del siguiente paper (página 2).
# Paper: https://arxiv.org/abs/2110.08511

# Instrucciones de desarrollo dadas por el Doctor Genaro Juarez de la Escuela Superior de Computo del Instituto Politécnico Nacional en la materia de Teoría de la Computación

# Un input de entrada podría ser: "*|*|*". Funciona para cualquier m y n que se sumarán y entregarán un resultado en modo gráfico

# Autor: Oscar Bucio

# 1. La máquina se tiene que animar para cadenas pequeñas (menor igual a 10 caracteres).
# 2. Puede recibir la cadena por parte del usuario o aleatoriamente con un máximo de 50 caracteres.
# 3. Mandar la salida a un archivo de texto que muestre las descripciones instantáneas (IDs) por renglón en cada iteración.
# 4. En el reporte deben de estar pantallas del programa en ejecución de todas las características solicitadas.
# 5. En el reporte debe de estar también el código de la implementación en latex, no en imágenes.

#Funciones
def generacion():
    cadenaGenerada = ['*', '*', '*'] #Donde se guardará el conjunto de simbolos aleatorios generados
    numeroAleatorio = randint(2, 50) #Con este numero se sabrá la longitud total de la cadena a generar
    print(f"El numero aleatorio resultante es: {numeroAleatorio}")
    suma = 0
    while suma != numeroAleatorio - 3:
        n = randint(1, 50)
        m = randint(1, 50)
        suma = n + m
        if suma == numeroAleatorio - 3:
            break
        else: 
            continue
    print(f"n numero de pipas es: {n}")
    print(f"m numero de pipas es: {m}")

    #Insertando 
    for i in range(m):
        cadenaGenerada.insert(2, '|')
    i = 0
    for i in range(n):
        cadenaGenerada.insert(1, '|')
    print(f"La cadena generada aleatoriamente es: {cadenaGenerada}")
    return cadenaGenerada

def revision(cadena):
    estado = 1 #Variable implicita de la MT, se inicializa con el primer estado (1)
    posicionCadena = 0
    a = open("Programa7_DescripcionesInstantaneas.txt", "w", encoding="utf-8")
    longitudCadena = len(cadena)
    if len(cadena) <= 10:
        #Tortugas fijas
        t = turtle.Turtle() #Es para generar la cuadricula inicial
        t2 = turtle.Turtle() #Generar el cabezal
        t3 = turtle.Turtle() #Generar los cuadros nuevos
        t4 = turtle.Turtle() #Cambiar el texto
        
        turtle.title("Maquina de Turing")
        coordenadasX = 0 #Para setear la cinta en 0 de X
        
        t.up()
        t.goto(0,0)
        t.down()
        #Generación de la cuadricula o tape (cinta)
        for i in range(0, longitudCadena): 
            t.speed(0)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            coordenadasX = coordenadasX + 50
            t.up()
            t.goto(coordenadasX,0)
            t.down()
        t.hideturtle()
        #Generacion de cabezal
        t2.up()
        t2.speed(0)
        t2.goto(0,100)
        t2.down()
        t2.forward(50)
        t2.right(90)
        t2.forward(50)
        t2.right(90)
        t2.forward(50)
        t2.right(90)
        t2.forward(50)
        #flecha de abajo
        t2.up()
        t2.goto(25,50)
        t2.down()
        t2.bk(30)
        #texto en el centro
        t2.up()
        t2.goto(25,70)
        t2.down()
        t2.write('q', align="center", font=('Arial', 16, 'normal'))
        t2.hideturtle()
        
        #Metiendo la cadena en la cinta
        ejeXCinta = 25
        for i in range(0, longitudCadena):
            t4.up()
            t4.goto(ejeXCinta, -35)
            t4.down()
            t4.write(f'{cadena[i]}', align="center", font=('Arial', 16, 'bold'))
            t4.hideturtle()
            ejeXCinta = ejeXCinta + 50

        while(True):
                if cadena[posicionCadena] == '*' and estado == 1:
                    estado = 2
                    cadena[posicionCadena] = 'X'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    #Graficacion en este punto del computo
                    t2.clear()
                    t2.reset()
                    t2.speed(0)
                    t2.up()
                    t2.speed(0)
                    t2.goto(posicionCadena * 50, 100)
                    t2.down()
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    # flecha de abajo
                    t2.up()
                    t2.goto(posicionCadena * 25 + 25, 50)
                    t2.right(180)
                    t2.down()
                    t2.forward(30)
                    #texto en el centro
                    t2.up()
                    t2.goto(posicionCadena * 25 + 25, 70)
                    t2.down()
                    t2.write('q', align="center", font=('Arial', 16, 'normal'))
                    t2.hideturtle()
                    time.sleep(1)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('X', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('X', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
    
                    posicionCadena = posicionCadena + 1 
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.hideturtle()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue
                elif cadena[posicionCadena] == '*' and estado == 2:
                    #Graficacion en este punto del computo
                    t2.clear()
                    t2.reset()
                    t2.speed(0)
                    t2.speed(0)
                    t2.up()
                    t2.goto(posicionCadena * 50,100)
                    t2.right(0)
                    t2.down()
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    t2.right(90)
                    t2.forward(50)
                    # flecha de abajo
                    t2.up()
                    t2.goto(posicionCadena * 50 + 25, 50)
                    t2.right(180)
                    t2.down()
                    t2.forward(30)
                    #texto en el centro
                    t2.up()
                    t2.goto(posicionCadena * 50 + 25, 70)
                    t2.down()
                    t2.write('q', align="center", font=('Arial', 16, 'normal'))
                    t2.hideturtle()
                    time.sleep(1)
                    posicionCadena = posicionCadena + 1
                    estado = 3
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 2:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 3:
                    cadena[posicionCadena] = 'X'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('X', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('X', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()                       
                    posicionCadena = posicionCadena - 1
                    estado = 4
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 3:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 4:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 4:
                    estado = 5
                    cadena[posicionCadena] = 'a'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('a', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('a', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 4:
                    estado = 7
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 1)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '_' and estado == 5:
                    estado = 6
                    cadena[posicionCadena] = '|'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('|', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('|', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 5:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 5:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 5:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.hideturtle()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 6:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 6:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == 'a' and estado == 6:
                    estado = 4
                    cadena[posicionCadena] = '|'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('|', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('|', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()

                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 6:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 7:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    estado = 8
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 7:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '_' and estado == 8:
                    cadena[posicionCadena] = '*'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()

                    posicionCadena = posicionCadena - 1
                    estado = 9
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 8:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 8:
                    cadena[posicionCadena] = '*'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '*' and estado == 9:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue

                elif cadena[posicionCadena] == '|' and estado == 9:
                    cabezal(t2, posicionCadena)
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                        t3.up()
                        t3.setheading(360)
                        t3.goto(coordenadasX, 0)
                        t3.down()
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.right(90)
                        t3.forward(50)
                        t3.up()
                        t3.goto(posicionCadena * 50 + 25, -35)
                        t3.write('_', align="center", font=('Arial', 16, 'bold'))
                        coordenadasX = coordenadasX + 50
                    continue
                #Estados para salir del bucle infinito
                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|') and estado == 2:
                    print("Esta cadena no fue aceptada")
                    break

                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|') and estado == 3:
                    print("Esta cadena no fue aceptada")
                    break

                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X') and estado == 4:
                    print("Esta cadena no fue aceptada")
                    break
                
                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X' and cadena[posicionCadena] != '_') and estado == 5:
                    print("Esta cadena no fue aceptada")
                    break

                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X' and cadena[posicionCadena] != 'a') and estado == 6:
                    print("Esta cadena no fue aceptada")
                    break
                
                elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' ) and estado == 7:
                    print("Esta cadena no fue aceptada")
                    break

                elif (cadena[posicionCadena] != '_' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X') and estado == 8:
                    print("Esta cadena no fue aceptada")
                    break
                elif cadena[posicionCadena] == 'X' and estado == 9:
                    cadena[posicionCadena] = '*'
                    a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                    cabezal(t2, posicionCadena)
                    #Cambio de simbolo
                    t4.up()
                    if posicionCadena == 0:
                        t4.goto(25, -35)
                        limpiar(25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()
                    else:
                        t4.goto(posicionCadena * 50 + 25, -35)
                        limpiar(posicionCadena * 50 + 25, -35)
                        t4.down()
                        t4.write('*', align="center", font=('Arial', 16, 'bold'))
                        t4.hideturtle()

                    print("La cadena llegó al estado HALTED, concluyo satisfactoriamente. Se para la computación")
                    print(f"La cadena final es: {cadena}")
                    break
        turtle.exitonclick()
        a.close()
    else:
        print("La cadena es mayor o igual a 10, no se grafica")
        a = open("Programa7_DescripcionesInstantaneas.txt", "w", encoding="utf-8")
        while(True):
            if cadena[posicionCadena] == '*' and estado == 1:
                estado = 2
                cadena[posicionCadena] = 'X'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1 
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue
            elif cadena[posicionCadena] == '*' and estado == 2:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                estado = 3
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 2:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 3:
                cadena[posicionCadena] = 'X'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                estado = 4
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 3:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 4:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 4:
                estado = 5
                cadena[posicionCadena] = 'a'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 4:
                estado = 7
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '_' and estado == 5:
                estado = 6
                cadena[posicionCadena] = '|'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 5:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 5:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 5:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 6:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 6:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'a' and estado == 6:
                estado = 4
                cadena[posicionCadena] = '|'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 6:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 7:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                estado = 8
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 7:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '_' and estado == 8:
                cadena[posicionCadena] = '*'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                estado = 9
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 8:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 8:
                cadena[posicionCadena] = '*'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 9:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 9:
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue
            #Estados para salir del bucle infinito
            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|') and estado == 2:
                print("Esta cadena no fue aceptada")
                break

            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|') and estado == 3:
                print("Esta cadena no fue aceptada")
                break

            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X') and estado == 4:
                print("Esta cadena no fue aceptada")
                break
            
            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X' and cadena[posicionCadena] != '_') and estado == 5:
                print("Esta cadena no fue aceptada")
                break

            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X' and cadena[posicionCadena] != 'a') and estado == 6:
                print("Esta cadena no fue aceptada")
                break
            
            elif (cadena[posicionCadena] != '*' and cadena[posicionCadena] != '|' ) and estado == 7:
                print("Esta cadena no fue aceptada")
                break

            elif (cadena[posicionCadena] != '_' and cadena[posicionCadena] != '|' and cadena[posicionCadena] != 'X') and estado == 8:
                print("Esta cadena no fue aceptada")
                break
            elif cadena[posicionCadena] == 'X' and estado == 9:
                cadena[posicionCadena] = '*'
                a.write(f"{cadena[:posicionCadena], estado, cadena[posicionCadena:]}|-\n")
                print("La cadena llegó al estado HALTED, concluyo satisfactoriamente. Se para la computación")
                print(f"La cadena final es: {cadena}")
                break
    a.close()

def limpiar(x,y):
    t5 = turtle.Turtle() #Cambiar el texto
    t5.hideturtle()
    t5.speed(0)
    t5.up()
    x = x - 15
    y = y + 25
    t5.goto(x,y)
    t5.color("white", "white")
    t5.down()
    t5.begin_fill()
    for i in range(4):
        t5.forward(25)
        t5.right(90)
    t5.end_fill()

def cabezal(t2, posicionCadena):
    #Graficacion en este punto del computo
    t2.clear()
    t2.reset()
    t2.speed(0)
    t2.up()
    t2.speed(0)
    t2.goto(posicionCadena * 50, 100)
    t2.down()
    t2.forward(50)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(50)
    # flecha de abajo
    t2.up()
    t2.goto(posicionCadena * 50 + 25, 50)
    t2.right(180)
    t2.down()
    t2.forward(30)
    #texto en el centro
    t2.up()
    t2.goto(posicionCadena * 50 + 25, 70)
    t2.down()
    t2.write('q', align="center", font=('Arial', 16, 'normal'))
    t2.hideturtle()
    time.sleep(1)
    

def maquina():
    print("Bienvenido a una prueba de la pedagogical universal Turing machine, que disfrute su estancia.")
    eleccion = input("1.Introducir cadena \n2.Generar cadena aleatoria \n")
    warn = True
    cadena = []
    if eleccion == '1':
        cadena = input("Ingrese la cadena: ")
        cadena = list(cadena) #Convirtiendo el string en una lista uno por uno
        print(cadena)
        for i in cadena:
            if i != '_' and i != '*' and i != '|':
                print("La cadena tiene simbolos distintos a los propuestos, ingrese una nueva cadena")
                warn = False
        if warn == True: 
            print("Los simbolos son los correctos, procedemos")
            revision(cadena)
    elif eleccion == '2':
        cadena = generacion()
        cadena = list(cadena)
        revision(cadena)
    else:
        print("Introduzca un numero correcto, intente otra vez")

if __name__ == '__main__':
    maquina()
