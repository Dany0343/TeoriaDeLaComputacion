# -*- coding: utf-8 -*-
#Librerias
from enum import auto
import random
from random import randint
import time
import turtle

#Funciones

def generacion():
    cadenaGenerada = []
    numeroAleatorio = randint(1, 50) #Con este numero se sabrá la longitud total de la cadena a generar
    print(f"El numero aleatorio resultante es: {numeroAleatorio}")
    for i in range(1, numeroAleatorio + 1):
        letraRandom = random.choice(['_', '*', '|', 'a', 'X']) #De esta función se sacarán aleatoriamente los simbolos
        cadenaGenerada.append(letraRandom)

    print(cadenaGenerada)

def maquina():
    print("Bienvenido a una prueba de la pedagogical universal Turing machine, que disfrute su estancia.")
    eleccion = int(input("1.Introducir cadena \n2.Generar cadena aleatoria \n"))
    if eleccion == 1:
        
    elif eleccion == 2:
        generacion()

if __name__ == '__main__':
    maquina()