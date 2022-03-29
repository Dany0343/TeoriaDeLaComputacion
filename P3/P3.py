# -*-coding: utf-8 -*-
import random
from random import randint
import time
#from turtle import *
import turtle as tur

#Generacion de 1 millon de cadenas binarias de 64 bits
k = 0 #iterador para mostrar las veces que el automata ha encendido
c = 0 #contador para mostrar referencia del numero de cadena actual en el archivo de estados

def graficacion(): 
    tgraph = tur.Turtle()
    radius = 50
    font_size = 18
    x = (0, 100)
    y = (0, 100)
    font = ("Arial", font_size, "normal")

    #Primer nodo
    tur.up()
    tur.goto(-250, 100 - font_size // 2)
    tur.write("Start", align="center", font=font)

    #Linea de primer a segundo
    tur.up()
    tur.fillcolor('black')
    tur.goto(-220, 100)
    tur.pendown()
    tur.goto(-150, 100)
    tur.penup()

    #Segundo nodo
    tur.up()
    tur.goto(-100, 100 - radius)
    tur.down()
    tur.circle(radius)
    tur.up()
    tur.goto(-100, 100 - font_size // 2)
    tur.write("Ready", align="center", font=font)
    
    #Linea de segundo a tercero
    tur.up()
    tur.fillcolor('black')
    tur.goto(-50, 100)
    tur.pendown()
    tur.goto(50, 100)
    tur.penup()

    #tercer nodo
    tur.up()
    tur.goto(100, 100 - radius)
    tur.down()
    tur.circle(radius)
    tur.up()
    tur.goto(100, 100 - font_size // 2)
    tur.write("Sending", align="center", font=font)
    tur.exitonclick()

def cadenas():
    f = open("Programa3_Cadenas.txt", "a", encoding="utf-8") #Es importante poner el parametro 'a' para que añada al final y no sobreescriba todo.
    for i in range(0, 10000): #Numero de cadenas
        for j in range(0, 64): #Numero de bits
            aux = randint(0,1)
            f.write(str(aux))
        f.write('\n')
    f.close()

def afd_paridad():
    opc = input("¿Deseas graficar? \n").lower()
    if opc == 'si':
        graficacion()
    cadena = 0
    e = open("Programa3_CambiosEstado.txt", "a", encoding="utf-8")
    f = open("Programa3_Cadenas.txt", 'r')
    g = open("Programa3_CadenasAceptadas.txt", "a", encoding="utf-8")
    h = open("Programa3_CadenasRechazadas.txt", "a", encoding="utf-8")

    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            cadena = i #Se guarda i actual en la variable cadena
            estado = 'q0' #Se inicializa el estado inicial q0
            global c
            c += 1
            e.write("El numero de cadena es: " + str(c) + '\n')
            for j in cadena:
                if estado == 'q0' and j == '\n': 
                    g.write(i)
                    e.write(str(estado) + '\n')
                    break #Se rompe el ciclo ya que se llegó a un estado de transición
                elif j == '\n' and (estado == 'q1' or estado == 'q2' or estado == 'q3'):
                    h.write(i)
                    e.write(str(estado) + '\n')
                    break #Se rompe el ciclo ya que se llegó a un estado de transición
                elif estado == 'q0' and j == '0':
                    estado = 'q2' #Se actualiza el estado
                    e.write(str(estado) + '\n')
                    continue
                elif estado == 'q0' and j == '1':
                    estado = 'q1'
                    e.write(str(estado) + '\n')
                    continue
                #Termina primer fila
                elif estado == 'q1' and j == '0':
                    estado = 'q3'
                    e.write(str(estado) + '\n')
                    continue
                elif estado == 'q1' and j == '1':
                    estado = 'q0'
                    e.write(str(estado) + '\n')
                    continue
                #Termina segunda fila
                elif estado == 'q2' and j == '0': 
                    estado = 'q0'
                    e.write(str(estado) + '\n')
                    continue
                elif estado == 'q2' and j == '1':
                    estado = 'q3'
                    e.write(str(estado) + '\n')
                    continue
                #Termina tercer fila
                elif estado == 'q3' and j == '0':
                    estado = 'q1'
                    e.write(str(estado) + '\n')
                    continue
                elif estado == 'q3' and j == '1':
                    estado = 'q2'
                    e.write(str(estado) + '\n')
                    continue
        else:
            print("Espacio vacío")
    g.close()
    h.close()
    e.close()
    protocolo() #Se manda a llamar de nuevo al automata de protocolo

def protocolo():
    global k
    global estado
    estado = random.choice([True, False])
    if estado == True:
        k += 1
        print("Se inicia el Automata")
        print(f"Esta es la iteracion {k}")
        cadenas() #Se generan las cadenas
        time.sleep(1) #Se espera 1 segundo
        afd_paridad() #Se manda a llamar al automata de paridad para revisar las cadenas
    else: 
        print("El automata está apagado")


protocolo() #Se inicializa el automata de protocolo solo una vez, cuando se ejecute el programa