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
    estado = random.choice([True, False]) #Se inicializa el automata de forma automatica 
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
    #Se lee el archivo
    f = open("textoPrueba.txt", "r")
    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            estado = 'q0' #Se setea un estado inicial
            cadena = i.lower() #Se guarda el i actual en la variable cadena
            counter = 0 #Contador para obtener la posicion de la palabra
            for j in cadena:
                if j == '\n': #Caso para terminar el ciclo
                    print("Se terminaron las listas de palabras") 
                    break
                elif j =='w' and (estado == 'A' or estado == 'B'):
                    estado = 'B'
                    continue
                elif j =='e' and estado == 'B':
                    estado = 'C'
                    continue
                elif j =='b' and estado == 'C':
                    estado = 'D'
                    continue
                elif (j != 'p' or j != 's' or j != 'm' or j != 'w' or j != 'e') and estado == 'D':
                    web = web + 1 #Se llega a un estado de transición
                    estado = 'A' #Seguimos en duda aqui
                    continue
                elif j =='w' and estado == 'D': #Se regresa por si vuelve a empezar la W
                    estado = 'B'
                    web = web + 1 
                    continue
                #De aquí falta a R

                #Primera bifurcacion
                #Sin web
                elif j == 'p' and estado != 'D':
                    estado = 'Ie'
                    continue
                elif j =='p' and estado == 'I':
                    estado = 'Ie'
                    continue
                elif j == 'a' and estado == 'Ie':
                    estado == 'J'
                    continue
                elif j == 'g' and estado == 'J':
                    estado = 'K'
                    continue
                elif j == 'e' and estado == 'K':
                    estado = 'L'
                    page = page + 1
                    continue
                #Viene junto con web
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
                    estado = 'L'
                    webpage = webpage + 1
                    continue


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
                    estado = 'Q'
                    webmaster = webmaster + 1 #Se llega a un estado de transición
                
            print(f"Los resultados para cada variable fueron: \n Web {web}\n WebPage {webpage}\n Website {website}\n Webmaster {webmaster}\n Ebay {ebay}\n page {page}\n site {site}")
        else:
            print("Espacio vacío")


if __name__ == '__main__':
    main()