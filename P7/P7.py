# -*- coding: utf-8 -*-
#Librerias
from enum import auto
import random
from random import randint
from re import X
import string
import time
import turtle

#Funciones

def generacion():
    cadenaGenerada = ['*', '*', '*'] #Donde se guardará el conjunto de simbolos aleatorios generados
    numeroAleatorio = randint(2, 50) #Con este numero se sabrá la longitud total de la cadena a generar
    print(f"El numero aleatorio resultante es: {numeroAleatorio}")
    suma = 0
    while suma != numeroAleatorio:
        n = randint(1 , 50)
        m = randint(1, 50)
        suma = n + m
        if suma == numeroAleatorio:
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
    if len(cadena) <= 10:
        t = turtle.Turtle()
        turtle.title("Maquina de Turing")
        coordenadasX = 0
        t.goto(0,0)
        for i in range(len(cadena)):
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            coordenadasX = coordenadasX + 150
            t.goto(coordenadasX, 0)
        while(True):
                if cadena[posicionCadena] == '*' and estado == 1:
                    estado = 2
                    cadena[posicionCadena] = 'X'
                    posicionCadena = posicionCadena + 1 
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue
                elif cadena[posicionCadena] == '*' and estado == 2:
                    posicionCadena = posicionCadena + 1
                    estado = 3
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 2:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 3:
                    cadena[posicionCadena] = 'X'
                    posicionCadena = posicionCadena - 1
                    estado = 4
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 3:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 4:
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 4:
                    estado = 5
                    cadena[posicionCadena] = 'a'
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 4:
                    estado = 7
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '_' and estado == 5:
                    estado = 6
                    cadena[posicionCadena] = '|'
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 5:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 5:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 5:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 6:
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 6:
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == 'a' and estado == 6:
                    estado = 4
                    cadena[posicionCadena] = '|'
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 6:
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 7:
                    posicionCadena = posicionCadena + 1
                    estado = 8
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 7:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '_' and estado == 8:
                    cadena[posicionCadena] = '*'
                    posicionCadena = posicionCadena - 1
                    estado = 9
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 8:
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == 'X' and estado == 8:
                    cadena[posicionCadena] = '*'
                    posicionCadena = posicionCadena + 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '*' and estado == 9:
                    posicionCadena = posicionCadena - 1
                    if posicionCadena > len(cadena) - 1:
                        cadena.append("_")
                    continue

                elif cadena[posicionCadena] == '|' and estado == 9:
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
                    print("La cadena llegó al estado HALTED, concluyo satisfactoriamente. Se para la computación")
                    print(f"La cadena final es: {cadena}")
                    break
        turtle.exitonclick()
    else:
        while(True):
            if cadena[posicionCadena] == '*' and estado == 1:
                estado = 2
                cadena[posicionCadena] = 'X'
                posicionCadena = posicionCadena + 1 
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue
            elif cadena[posicionCadena] == '*' and estado == 2:
                posicionCadena = posicionCadena + 1
                estado = 3
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 2:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 3:
                cadena[posicionCadena] = 'X'
                posicionCadena = posicionCadena - 1
                estado = 4
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 3:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 4:
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 4:
                estado = 5
                cadena[posicionCadena] = 'a'
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 4:
                estado = 7
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '_' and estado == 5:
                estado = 6
                cadena[posicionCadena] = '|'
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 5:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 5:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 5:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 6:
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 6:
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'a' and estado == 6:
                estado = 4
                cadena[posicionCadena] = '|'
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 6:
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 7:
                posicionCadena = posicionCadena + 1
                estado = 8
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 7:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '_' and estado == 8:
                cadena[posicionCadena] = '*'
                posicionCadena = posicionCadena - 1
                estado = 9
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 8:
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == 'X' and estado == 8:
                cadena[posicionCadena] = '*'
                posicionCadena = posicionCadena + 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '*' and estado == 9:
                posicionCadena = posicionCadena - 1
                if posicionCadena > len(cadena) - 1:
                    cadena.append("_")
                continue

            elif cadena[posicionCadena] == '|' and estado == 9:
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
                print("La cadena llegó al estado HALTED, concluyo satisfactoriamente. Se para la computación")
                print(f"La cadena final es: {cadena}")
                break
    a.close()

def maquina():
    print("Bienvenido a una prueba de la pedagogical universal Turing machine, que disfrute su estancia.")
    eleccion = int(input("1.Introducir cadena \n2.Generar cadena aleatoria \n"))
    warn = True
    cadena = []

    if eleccion == 1:
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
    elif eleccion == 2:
        cadena = generacion()
        cadena = list(cadena)
        revision(cadena)

if __name__ == '__main__':
    maquina()