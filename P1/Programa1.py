# -*- coding: utf-8 -*-
#Variables
# Teoría de la Computación - ESCOM IPN - Genaro Juarez

from random import randint
from timeit import default_timer
import matplotlib.pyplot as plt
import math

i = 0 #Iteradores
j = 0
decision = "" #Seleccionar el tipo de entrada. Automatica o manual
opcion = 0 #Dato entregado a binarios para proceder a generar la función
nsimbolos = [] #Lista que guarda el numero total de simbolos de cada cadena
ntotal = [] #Lista que guarda los numeros desde el 1 hasta la elección del usuario, haya sido automatica o manual
unos = [] #Lista que guarda el numero total de unos de cada cadena
contador = 0
contadorUnos = 0
#Funciones

def calcularLongitud(s):
    counter = 0
    for i in s:
        counter+=1
    return counter

def binarios(opcion): 
    #cadenas = ['{', 'ε']
    global contador
    global contadorUnos
    f = open("Programa1.txt", "w", encoding="utf-8")
    f.write('Σ^* = ' + '{' + 'ε' + ',' + "\n")
    for i in range(1, opcion + 1):
        for j in range(0, 2 ** i): #Recorrer y generar la cadena desde 0 hasta el numero especificado
            #Conversion a binario
            aux = str(bin(j))[2:]
            lenAux = calcularLongitud(aux)
            tam = lenAux
            if tam < i: 
                #modo manual
                #zeros = '0' * i
                #aux = zeros + aux
                #Modo con función
                aux = aux.zfill(i)
                lenAux = calcularLongitud(aux)
                contador = contador + lenAux
                contadorUnos += aux.count('1')
                f.writelines(aux + ",")
                #cadenas.append(aux) esto es usando una lista (mucha memoria)
            else: 
                f.writelines(aux + ",")
                contadorUnos +=  aux.count('1')
                lenAux = calcularLongitud(aux)
                contador = contador + lenAux
                #cadenas.append(aux)
        nsimbolos.append(contador)
        unos.append(contadorUnos)
        contador = 0
        contadorUnos = 0
        f.write("\n\n")
    #cadenas.append('}')
    f.write('}')
    f.close()

    #formateando si se usara una lista too fucking much memory
    # i = 0
    # for i in range(len(cadenas)):
    #     f.write(cadenas[i] + "\n")
    # f.close()


def graficacion(opcion):
    plt.clf()
    i = 0
    for i in range(1, opcion + 1): #llenando la lista del eje x respecto a lo elegido por el usuario
        ntotal.append(i)
    #Primera gráfica, numero de cadenas y numero total de simbolos
    puntosx = ntotal
    puntosy1 = nsimbolos
    puntosy1log = []
    puntosy2log = []

    plt.plot(puntosx, puntosy1, color = 'r')
    plt.xlabel("Numero de cadena")
    plt.ylabel("Numeros de simbolos por cadena")
    plt.ticklabel_format(style = 'plain')
    plt.title("Primera gráfica. Numero de cadena y numero total de simbolos")
    plt.grid()
    plt.show()
    
    #Primera gráfica con log10
    for numero in puntosy1:
        puntosy1log.append(math.log10(numero))
    plt.plot(puntosx, puntosy1log, color = 'y')
    plt.xlabel("Numero de cadena")
    plt.ylabel("Numeros de simbolos por cadena")
    plt.ticklabel_format(style = 'plain')
    plt.title("Primera gráfica con Log10")
    plt.grid()
    plt.show()



    #Segunda gráfica, numero de cadenas y numero total de unos
    puntosy2 = unos
    plt.plot(puntosx, puntosy2, color = 'b')
    plt.xlabel("Numero de cadena")
    plt.ylabel("Numeros de unos por cadena")
    plt.ticklabel_format(style = 'plain')
    plt.title("Segunda gráfica. Numero de cadena y numero total de unos")
    plt.grid()
    plt.show()

    #Segunda gráfica con log10
    for numero in puntosy2:
        puntosy2log.append(math.log10(numero))
    plt.plot(puntosx, puntosy2log, color = 'y')
    plt.xlabel("Numero de cadena")
    plt.ylabel("Numeros de unos por cadena")
    plt.ticklabel_format(style = 'plain')
    plt.title("Segunda gráfica con Log10")
    plt.grid()
    plt.show()

#Menu 
while decision != "no":
    print("Bienvenido a la calculadora de universos de cadenas binarias!")
    decision = int(input("1. Introducir numero\n2. Número aleatorio entre 1-1000\n3. Salir\n\n"))

    if decision == 1:
        nsimbolos = []
        ntotal = []
        unos = []
        opcion = int(input("Introduzca el numero de hasta donde desea obtener el universo de cadenas: "))
        if opcion > 0 and opcion < 1000:
            #Mandando a llamar a la funcion y midiendo el tiempo
            inicio = default_timer()
            binarios(opcion)
            fin = default_timer()
            tiempo = fin - inicio
            if tiempo > 120:
                tiempo = tiempo / 60
                print(f"El tiempo de ejecucion fue: {tiempo} minutos\n")
            else:
                print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
            print("Revise el archivo llamado Programa1.txt\n\n")
            graficacion(opcion)
        else:
            print("El numero está fuera de rango")

    elif decision == 2:
        nsimbolos = []
        ntotal = []
        unos = []
        opcion = randint(1,1000)
        print(f"El numero elegido automaticamente fue: {opcion}")
        #Mandando a llamar a la funcion y midiendo el tiempo
        inicio = default_timer()
        binarios(opcion)
        fin = default_timer()
        tiempo = fin - inicio
        if tiempo > 120:
            tiempo = tiempo / 60
            print(f"El tiempo de ejecucion fue: {tiempo} minutos\n")
        else:
            print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
        print("Revise el archivo llamado Programa1.txt\n\n")
        graficacion(opcion)

    elif decision == 3: 
        print("Hasta pronto!")
        break
    else:
        print("INGRESE UNA OPCION VALIDA \n\n")
    decision = input("Desea calcular de otro numero? [si/no]: ").lower()
    if  decision != 'si':
        print("Hasta pronto!")
        break
