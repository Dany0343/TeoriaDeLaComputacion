# -*- coding: utf-8 -*-
import random
from random import randint
import time
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
from automata.fa.nfa import NFA
from visual_automata.fa.nfa import VisualNFA

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
    opc = int(input("Cuál desea observar\n1.DFA\n2.NFA\n"))
    if opc == 1:
        dfa = VisualNFA(
        states={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U"},
        input_symbols={"w", "e", "b", "m", "a", "s", "t", "r", "p", "g", "i", "y", "Σ"},
        transitions={
        "A": {"w": {"B"}, "Σ": {"A"}, "p": {"I"}, "e": {"R"}, "s": {"E"}},
        "B": {"e": {"C"}, "w": {"B"}},
        "C": {"b": {"D"}, "e": {"R"}},
        "D": {"w": {"B"}, "p": {"I"}, "e": {"R"}, "s": {"E"}, "m": {"M"}},
        "M": {"m": {"M"}, "a": {"N"}},
        "N": {"s": {"Ñ"}},
        "Ñ": {"t": {"O"}},
        "O": {"e": {"P"}},
        "P": {"r": {"Q"}},
        "Q": {"Σ": {"A"}},
        "E": {"s": {"E"}, "w": {"B"}, "i": {"F"}},
        "F": {"w": {"B"}, "t": {"G"}},
        "G": {"w": {"B"}, "e": {"H"}},
        "H": {"w": {"B"}, "Σ": {"A"}},
        "I": {"p": {"I"}, "a": {"J"}},
        "J": {"g": {"K"}, "p": {"I"}},
        "K": {"e": {"L"}, "p": {"I"}},
        "L": {"Σ": {"A"}, "p": {"I"}},
        "R": {"e": {"R"}, "b": {"S"}},
        "S": {"e": {"R"}, "a": {"T"}},
        "T": {"e": {"R"}, "y": {"U"}},
        "U": {"e": {"R"}, "Σ": {"A"}}
        },
        initial_state="A",
        final_states={"Q", "L", "H", "U"},
        )
        dfa = VisualNFA(dfa)
        dfa.show_diagram(view = True)
    elif opc == 2:
        dfa = VisualNFA(
        states={"q0","q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20","q21"},
        input_symbols={"w", "e", "b", "m", "a", "s", "t", "r", "p", "g", "i", "y", "Σ"},
        transitions={
        "q0": {"Σ": {"q0"}, "e": {"q18"}, "w": {"q1"}},
        "q1": {"w": {"q1"}, "e": {"q18"}, "e": {"q2"}},
        "q2": {"b": {"q3"}},
        "q3": {"p": {"q8"}, "s": {"q4"}, "m": {"q12"}, "e": {"q18"}},
        "q12": {"a": {"q13"}},
        "q13": {"s": {"q14"}},
        "q14": {"t": {"q15"}},
        "q15": {"e": {"q16", "q18"}},
        "q16": {"r": {"q17"}},
        # "q17": {"Σ": {"A"}},
        "q4": {"s": {"q4"}, "i": {"q5"}},
        "q5": {"t": {"q6"}},
        "q6": {"e": {"q7"}},
        # "q7": {"w": {"B"}, "Σ": {"A"}},
        "q8": {"p": {"q8"}, "a": {"q9"}},
        "q9": {"g": {"q10"}},
        "q10": {"e": {"q11"}},
        # "q11": {"Σ": {"A"}, "p": {"I"}},
        "q18": {"e": {"q18"}, "b": {"q19"}},
        "q19": {"a": {"q20"}},
        "q20": {"y": {"q21"}},
        # "q21": {"e": {"R"}, "Σ": {"A"}}
        },
        initial_state="q0",
        final_states={"q17", "q11", "q7", "q21"},
        )
        dfa = VisualNFA(dfa)
        dfa.show_diagram(view = True)
    else:
        print("No se eligió una opción correcta")
        graficacion()


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
                elif (j != 'w' and j !='e' and j !='b' and j != 'm' and j !='a' and j != 's' and j != 't' and j != 'r' and j != 'p' and j != 'i' and j !='y') and estado == 'A':
                    edoanterior = estado
                    estado = 'A'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
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
                    if str(texto[index+1]) != 'e':
                        estado = 'A'
                        continue
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
                    elif (str(texto[index+1]) == 'b' and str(texto[index+2]) == 'a' and str(texto[index+3]) == 'y') and estado == 'B':
                        edoanterior = estado
                        if index == 1:
                            web.append(0)
                            ebay.append(0)
                        else:
                            web.append(index - 2)
                            ebay.append(index - 3)
                        estado = 'A'
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    elif str(texto[index+1]) != 'b':
                        estado = 'A'
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
                    if str(texto[index+1]) != 'b':
                        estado = 'A'
                        continue
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
                    elif str(texto[index+1]) != 'a':
                        estado = 'A'
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
                    elif str(texto[index+1]) != 'y':
                        estado = 'A'
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
                    if str(texto[index+1]) != 'g':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'J'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='g' and estado == 'J':
                    if str(texto[index+1]) != 'e':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'K'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'K':
                    if str(texto[index-4]) == 'b' and str(texto[index-5]) == 'e' and str(texto[index-6]) == 'w':
                        if (str(texto[index+1]) == 'b' and str(texto[index+2]) == 'a' and str(texto[index+3]) == 'y') and estado == 'K':
                            edoanterior = estado
                            estado = 'A'
                            ebay.append(index - 2)
                            webpage.append(index - 3)
                            a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                            continue
                        edoanterior = estado
                        webpage.append(index - 6)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        continue
                    else:
                        if (str(texto[index+1]) == 'b' and str(texto[index+2]) == 'a' and str(texto[index+3]) == 'y') and estado == 'K':
                            edoanterior = estado
                            estado = 'A'
                            page.append(index - 3)
                            ebay.append(index - 2)
                            a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                            continue
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
                    elif str(texto[index+1]) != 't':
                        estado = 'A'
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
                    elif str(texto[index+1]) != 'e':
                        estado = 'A'
                        continue
                    estado = 'G'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'G':
                    edoanterior = estado
                    if str(texto[index-4]) == 'b' and str(texto[index-5]) == 'e' and str(texto[index-6]) == 'w':
                        if(str(texto[index+1]) == 'b' and str(texto[index+2]) == 'a' and str(texto[index+3]) == 'y') and estado == 'G' and str(texto[index-4]) == 'b':
                            edoanterior = estado
                            website.append(index - 6)
                            ebay.append(index - 3)
                            estado = 'A'
                            a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                            continue
                        website.append(index - 6)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    else:
                        if (str(texto[index+1]) == 'b' and str(texto[index+2]) == 'a' and str(texto[index+3]) == 'y') and estado == 'G':
                            edoanterior = estado
                            site.append(index - 3)
                            ebay.append(index - 3)
                            estado = 'A'
                            a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                        site.append(index - 3)
                        estado = 'A' #Se setea el estado inicial para reconocer una nueva cadena
                        a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue

                #Siguiendo con el flujo normal 
                elif j =='m' and estado == 'D':
                    if str(texto[index+1]) != 'a':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'M'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='a' and estado == 'M':
                    if str(texto[index+1]) != 's':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'N'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='s' and estado == 'N':
                    if str(texto[index+1]) != 't':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'Ñ'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='t' and estado == 'Ñ':
                    if str(texto[index+1]) != 'e':
                        estado = 'A'
                        continue
                    edoanterior = estado
                    estado = 'O'
                    a.write(f"[δ : {edoanterior} X {j} -> {estado}]\n")
                    continue
                elif j =='e' and estado == 'O':
                    if str(texto[index+1]) != 'r':
                        estado = 'A'
                        continue
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