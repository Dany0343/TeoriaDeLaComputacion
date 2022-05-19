import random
from random import randint
import time
from turtle import *
import turtle as tur

# Programar el autómata finito determinístico que reconozca las palabras:

# web, webpage, website, webmaster, ebay, page, site

# 1. Diseñar el NFA.
# 2. Realizar la conversión a DFA mostrando todo el proceso a través de los subconjuntos y tablas.
# 3. El programa deberá de leer un archivo de texto, podría ser de una página web.
# 4. El autómata deberá de identificar cada palabra reservada con el DFA, contarlas e indicar dónde las encontró (posición).
# 5. En un archivo imprimir la evaluación del autómata por cada carácter que lea y cambio de estado, es decir, toda la historia del proceso.
# 6. En otro archivo enumerar, contar y anotar donde están las palabras encontradas.
# 7. Tener una opción para ver el autómata, es decir, hay que graficarlo.
# 8. Incluir en el reporte el código fuente.

#Funciones
def graficacion():
    print("A graficar")


def main():
    global estado 
    estado = random.choice([True, True]) #Se inicializa el automata de forma automatica 
    if estado == True:
        print("Se inicia el Automata")
        automata() #Se manda a llamar al automata para revisar el archivo con las palabras
    else: 
        print("El automata está apagado")

def automata():
    opc = input("¿Deseas graficar? \n").lower()
    if opc == 'si':
        graficacion()
    #Archivos y variables
    a = open("Programa4_CambiosEstado.txt", "a", encoding="utf-8")
    b = open("Programa4_PalabrasEncontradas.txt", "a", encoding="utf-8")
    #Variables para contabilizar el numero de veces encontrada una variable
    web = 0
    webpage = 0
    website = 0
    webmaster = 0
    ebay = 0
    page = 0
    site = 0
    texto = []
    #Se lee el archivo
    f = open("textoPrueba.txt", "r")

    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            estado = 'A' #Se setea un estado inicial
            cadena = i.lower() #Se guarda el i actual en la variable cadena
            counter = 0 #Contador para obtener la posicion de la palabra
            for k in cadena: #Cada renglon se mete caracter por caracter a una lista para facilitar su uso
                texto.append(k)
            for index, j in enumerate(texto):
                if j == '\n': #Caso para terminar el ciclo
                    print("Se terminó las listas de palabras") 
                    break
                elif j =='w' and (estado == 'A' or estado == 'B'): #recursivo a si mismo si es el caso
                    estado = 'B'
                    continue
                elif j =='e' and estado == 'B':
                    estado = 'C'
                    continue
                elif j =='b' and estado == 'C':
                    estado = 'D'
                    if (str(texto[index+1]) != 'p' and str(texto[index+1]) != 'm' and str(texto[index+1]) != 's' and str(texto[index+1]) != 'e') and estado == 'D':
                        web = web + 1 #Se llega a un estado de transición
                        estado = 'A'
                    continue
                elif j =='w' and estado == 'D': #Se regresa por si vuelve a empezar la W
                    estado = 'B'
                    web = web + 1 
                #De aquí falta a R
                elif j == 'e'
                #Primera bifurcacion hacía arriba
                elif j == 'p' and estado == 'I': #recursivo a si mismo
                    estado = 'I'
                elif j =='p' and estado == 'D':
                    estado = 'I'
                    continue
                elif j =='a' and estado == 'I':
                    estado = 'J'
                    continue
                elif j =='g' and estado == 'J':
                    estado = 'K'
                    continue
                elif j =='e' and estado == 'K':
                    if str(texto[index-4] == 'b'):
                        webpage = webpage + 1
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    else:
                        page = page + 1
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    continue
                #Segunda bifurcacion hacía abajo
                elif j == 's' and estado == 'E': #recursivo a si mismo
                    estado = 'E'
                elif j =='s' and estado == 'D':
                    estado = 'E'
                    continue
                elif j =='i' and estado == 'E':
                    estado = 'F'
                    continue
                elif j =='t' and estado == 'F':
                    estado = 'G'
                    continue
                elif j =='e' and estado == 'G':
                    if str(texto[index-4] == 'b'):
                        website = website + 1
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    else:
                        site = site + 1
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    continue
                #Siguiendo con el flujo normal 
                elif j =='m' and estado == 'D':
                    estado = 'M'
                elif j =='a' and estado == 'M':
                    estado = 'N'
                elif j =='s' and estado == 'N':
                    estado = 'Ñ'
                elif j =='t' and estado == 'Ñ':
                    estado = 'O'
                elif j =='e' and estado == 'O':
                    estado = 'P'
                elif j =='r' and estado == 'P':
                    estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    webmaster = webmaster + 1 #Se llega a un estado de transición
                
            print(f"Los resultados para cada variable fueron: \n Web {web}\n WebPage {webpage}\n Website {website}\n Webmaster {webmaster}\n Ebay {ebay}\n page {page}\n site {site}")
        else:
            print("Espacio vacío")


if __name__ == '__main__':
    main()