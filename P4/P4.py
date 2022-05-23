from calendar import c
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
    a = open("Programa4_CambiosEstado.txt", "w", encoding="utf-8")
    b = open("Programa4_PalabrasEncontradas.txt", "w", encoding="utf-8")
    #Variables para contabilizar el numero de veces encontrada una variable
    web = []
    webpage = []
    website = []
    webmaster = []
    ebay = []
    page = []
    site = []

    #Para guardar letra por letra del archivo en una lista
    texto = []
    #Se lee el archivo
    f = open("textoPrueba.txt", "r")

    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            estado = 'A' #Se setea un estado inicial
            cadena = i.lower() #Se guarda el i actual en la variable cadena
            for k in cadena: #Cada renglon se mete caracter por caracter a una lista para facilitar su uso
                texto.append(k)
            for index, j in enumerate(texto):
                if j == '\n': #Caso para terminar el ciclo
                    print("Se terminó las listas de palabras") 
                    break
                #Del primer estado a todos los demás
                elif j == 'e' and estado == 'A':
                    edoanterior = estado
                    if str(texto[index+1]) != 'b':
                        estado = 'A'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'R'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 'p' and estado == 'A':
                    edoanterior = estado
                    if str(texto[index+1]) != 'a':
                        estado = 'A'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'I'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 's' and estado == 'A':
                    edoanterior = estado
                    if str(texto[index+1]) != 'i':
                        estado = 'A'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'E'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue

                #Reconocimiento de web
                elif j =='w' and (estado == 'A' or estado == 'B'): #recursivo a si mismo
                    edoanterior = estado
                    estado = 'B'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'B':
                    edoanterior = estado
                    if str(texto[index+1]) == 'e':
                        estado = 'R'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'C'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='b' and estado == 'C':
                    edoanterior = estado
                    estado = 'D'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    if (str(texto[index+1]) != 'p' and str(texto[index+1]) != 'm' and str(texto[index+1]) != 's') and estado == 'D':
                        web.append(index - 2) #Se llega a un estado de transición
                        estado = 'A'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='w' and estado == 'D': #Se regresa por si vuelve a empezar la W
                    edoanterior = estado
                    estado = 'B'
                    web.append(index - 2) 
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")

                #De aquí falta a R para ebay
                elif j == 'e' and estado == 'R': #recursivo a si mismo
                    edoanterior = estado
                    estado = 'R'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 'e' and estado == 'D':
                    edoanterior = estado
                    estado = 'R'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 'b' and estado == 'R':
                    edoanterior = estado
                    if str(texto[index+1]) == 'e':
                        estado = 'R'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'S'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 'a' and estado == 'S':
                    edoanterior = estado
                    if str(texto[index+1]) == 'e':
                        estado = 'R'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'T'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j == 'y' and estado == 'T':
                    edoanterior = estado
                    ebay.append(index - 3)
                    if str(texto[index+1]) == 'e':
                        estado = 'R'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue

                #Primera bifurcacion hacía arriba
                elif j == 'p' and estado == 'I': #recursivo a si mismo
                    edoanterior = estado
                    estado = 'I'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='p' and estado == 'D':
                    edoanterior = estado
                    if str(texto[index+1]) != 'a':
                        estado = 'A'
                        web.append(index - 2)
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'I'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='a' and estado == 'I':
                    edoanterior = estado
                    estado = 'J'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='g' and estado == 'J':
                    edoanterior = estado
                    estado = 'K'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'K':
                    if str(texto[index-4]) == 'b':
                        edoanterior = estado
                        webpage.append(index - 6)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    else:
                        edoanterior = estado
                        page.append(index - 3)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue

                #Segunda bifurcacion hacía abajo
                elif j == 's' and estado == 'E': #recursivo a si mismo
                    edoanterior = estado
                    estado = 'E'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='s' and estado == 'D':
                    edoanterior = estado
                    if str(texto[index+1]) == 'w':
                        estado = 'B'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    elif str(texto[index+1]) != 'i':
                        estado = 'A'
                        web.append(index - 2)
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'E'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='i' and estado == 'E':
                    edoanterior = estado
                    if str(texto[index+1]) == 'w':
                        estado = 'B'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'F'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='t' and estado == 'F':
                    edoanterior = estado
                    if str(texto[index+1]) == 'w':
                        estado = 'B'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    estado = 'G'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'G':
                    edoanterior = estado
                    if str(texto[index-4]) == 'b':
                        website.append(index - 6)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    else:
                        site.append(index - 3)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue

                #Siguiendo con el flujo normal 
                elif j =='m' and estado == 'D':
                    edoanterior = estado
                    estado = 'M'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='a' and estado == 'M':
                    edoanterior = estado
                    estado = 'N'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='s' and estado == 'N':
                    edoanterior = estado
                    estado = 'Ñ'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='t' and estado == 'Ñ':
                    edoanterior = estado
                    estado = 'O'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'O':
                    edoanterior = estado
                    estado = 'P'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='r' and estado == 'P':
                    edoanterior = estado
                    estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                    webmaster.append(index - 8) #Se llega a un estado de transición
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
        else:
            print("Espacio vacío")

    #llenado de archivo de palabras encontradas
    b.write(f"1. Las palabras encontradas para web fueron: {len(web)} y sus respectivas posiciones son {web}\n")
    b.write(f"2. Las palabras encontradas para webpage fueron: {len(webpage)} y sus respectivas posiciones son {webpage}\n")
    b.write(f"3. Las palabras encontradas para website fueron: {len(website)} y sus respectivas posiciones son {website}\n")
    b.write(f"4. Las palabras encontradas para webmaster fueron: {len(webmaster)} y sus respectivas posiciones son {webmaster}\n")
    b.write(f"5. Las palabras encontradas para ebay fueron: {len(ebay)} y sus respectivas posiciones son {ebay}\n")
    b.write(f"6. Las palabras encontradas para page fueron: {len(page)} y sus respectivas posiciones son {page}\n")
    b.write(f"7. Las palabras encontradas para site fueron: {len(site)} y sus respectivas posiciones son {site}\n")

    a.close()
    b.close()
    f.close()
    print("Revise el archivo 'Programa4_CambiosEstado.txt' para consultar los cambios de estados del automata")
    print("Revise archivo 'Programa4_PalabrasEncontradas.txt' para información de las palabras encontradas")

if __name__ == '__main__':
    main()