# -*- coding: utf-8 -*-
# Teoría de la Computación - ESCOM IPN - Genaro Juarez
#Librerias
from enum import auto
import random
from random import randint
import time
import turtle
# Programar un autómata de pila que sirva para reconocer el lenguaje libre de contexto {0^n 1^n | n >= 1}.

# Adicionalmente, el programa debe de contar con las siguientes características:

# 1. La cadena puede ser ingresada por el usuario o automáticamente. Si es aleatoriamente, la cadena no podrá ser mayor a 100,000 caracteres.
# 2. Mandar a un archivo y en pantalla la evaluación del autómata a través de descripciones instantáneas (IDs).
# 3. Animar el autómata de pila, solo si la cadena es menor igual a 10 caracteres.
# 4. En el reporte deben de estar pantallas del programa en ejecución de todas las características solicitadas.
# 5. En el reporte debe de estar también el código de la implementación en latex, no en imágenes.

#Funciones
def automata():
    cadena = "" #Donde se guardará la cadena
    pila = ['z0'] #La pila del automata, inicializada con el ultimo elemento, para saber si se alcanzó el final de la pila
    a = open("Programa6_DescripcionesInstantaneas.txt", "w", encoding="utf-8")
    print("Bienvenidx al automata de pila")
    print("El lenguaje del automata es {0^n 1^n | n >= 1}")
    #Se manda a generar la cadena con restricciones para poder operarla aquí
    cadena = proceso()
    if cadena == False:
        print("Se termina el programa")
    else:
        if len(cadena) <= 11:
            t = turtle.Turtle()
            turtle.title("Automata de pila")
            # turtle.getscreen().bgcolor("black")
            # turtle.color("red")
            # turtle.pencolor("purple")
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(100)
            #flecha de arriba
            t.goto(50,0)
            t.fd(70)
            t.up()
            #flecha de abajo
            t.goto(50,-100)
            t.down()
            t.bk(70)
            t.up()
            #Escribir texto
            t.goto(50,-50)
            t.down()
            t.write('q', align="center", font=('Arial', 16, 'normal'))
            
            #Segunda tortuga
            t2 = turtle.Turtle()
            #Tercera tortuga
            t3 = turtle.Turtle()
            
            time.sleep(1)
            t3.clear()
            t3.up()
            t3.goto(50, -195)
            t3.down()
            t3.write(pila[::-1], font=('Arial', 16, 'normal'))

            t.hideturtle()
            t2.hideturtle()
            t3.hideturtle()
            for index, i in enumerate(cadena): 
                if i == '0':
                    pila.append('0')
                    print(f"<q2, {cadena[index:-1]}, {pila[::-1]}>")
                    a.write(f"<q2, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                    time.sleep(1)
                    t2.clear()
                    t2.up()
                    t2.goto(50, 45)
                    t2.down()
                    t2.write(cadena[index:], font=('Arial', 16, 'normal'))

                    time.sleep(1)
                    t3.clear()
                    t3.up()
                    t3.goto(50, -195)
                    t3.down()
                    t3.write(pila[::-1], font=('Arial', 16, 'normal'))

                    continue
                elif i == '1':
                    if pila[-1] == '0':
                        pila.pop()
                        print(f"<q3, {cadena[index:-1]}, {pila[::-1]}>")
                        a.write(f"<q3, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                        time.sleep(1)
                        t2.clear()
                        t2.up()
                        t2.goto(50, 45)
                        t2.down()
                        t2.write(cadena[index:], font=('Arial', 16, 'normal'))
                        
                        time.sleep(1)
                        t3.clear()
                        t3.up()
                        t3.goto(50, -195)
                        t3.down()
                        t3.write(pila[::-1], font=('Arial', 16, 'normal'))
                    elif pila[-1] == 'z0' and i == '1':
                        print(f"<q3, {cadena[index:-1]}, {pila[::-1]}>")
                        a.write(f"<q3, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                        print("Se terminó la cadena pero la pila sigue con algo, por lo tanto la cadena que ingresó no es valida y no las reglas {0^n 1^n | n >= 1}")
                        time.sleep(1)
                        t2.clear()
                        t2.up()
                        t2.goto(50, 45)
                        t2.down()
                        t2.write(cadena[index:], font=('Arial', 16, 'normal'))

                        time.sleep(1)
                        t3.clear()
                        t3.up()
                        t3.goto(50, -195)
                        t3.down()
                        t3.write(pila[::-1], font=('Arial', 16, 'normal'))
                        break
                    continue
                elif i == '\n':
                    if pila[-1] == 'z0':
                        print(f"<q4, \ n, {pila[::-1]}>")
                        a.write(f"<q4, \ n, {pila[::-1]}>\n")
                        print("Se ha llegado a z0, la cadena es correcta!")
                        time.sleep(1)
                        t2.clear()
                        t2.up()
                        t2.goto(50, 45)
                        t2.down()
                        t2.write(cadena[index:], font=('Arial', 16, 'normal'))

                        time.sleep(1)
                        t3.clear()
                        t3.up()
                        t3.goto(50, -195)
                        t3.down()
                        t3.write(pila[::-1], font=('Arial', 16, 'normal'))
                    else:
                        print("Se terminó la cadena pero la pila sigue con algo, por lo tanto la cadena que ingresó no es valida y no las reglas {0^n 1^n | n >= 1}")
                    break #Se termina el ciclo ya que se terminó de leer la cadena
            # print(f"La cadena es: {cadena}")
            a.close()
            turtle.exitonclick()
        else: 
            for index, i in enumerate(cadena):
                if i == '0':
                    pila.append('0')
                    print(f"<q2, {cadena[index:-1]}, {pila[::-1]}>")
                    a.write(f"<q2, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                    continue
                elif i == '1':
                    if pila[-1] == '0':
                        pila.pop()
                        print(f"<q3, {cadena[index:-1]}, {pila[::-1]}>")
                        a.write(f"<q3, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                    elif pila[-1] == 'z0' and i == '1':
                        print(f"<q3, {cadena[index:-1]}, {pila[::-1]}>")
                        a.write(f"<q3, {cadena[index:-1]}, {pila[::-1]}>|-\n")
                        print("Se terminó la cadena pero la pila sigue con algo, por lo tanto la cadena que ingresó no es valida y no las reglas {0^n 1^n | n >= 1}")
                        break
                    continue
                elif i == '\n':
                    if pila[-1] == 'z0':
                        print(f"<q4, \ n, {pila[::-1]}>")
                        a.write(f"<q4, \ n, {pila[::-1]}>\n")
                        print("Se ha llegado a z0, la cadena es correcta!")
                    else:
                        print("Se terminó la cadena pero la pila sigue con algo, por lo tanto la cadena que ingresó no es valida y no las reglas {0^n 1^n | n >= 1}")
                    break #Se termina el ciclo ya que se terminó de leer la cadena
            # print(f"La cadena es: {cadena}")
            a.close()

def generacion():
    cadena = "" #Donde se guardará la cadena aleatoria
    numeroAleatorio = randint(1, 100000) #Mayor a uno
    numeroAleatorioMitad = numeroAleatorio // 2
    if numeroAleatorio == 1:
            cadena = cadena + '0'
            cadena = cadena + '1'
            cadena = cadena + '\n'
            return cadena
    for i in range(1, numeroAleatorioMitad + 1): #Numero de cadenas a generar
        cadena = cadena + '0'
    i = 0
    for i in range(numeroAleatorioMitad, numeroAleatorio):
        cadena = cadena + '1'
        if i == numeroAleatorio - 1:
            cadena = cadena + '\n'
    print(f"El numero aleatorio es: {numeroAleatorio}")
    return cadena

def proceso():
    cadena = ""
    counter = 0 #Variable para saber el estado de la cadena, si será admitida o no
    eleccion = int(input("1.Generación aleatoria\n2.Ingresar manualmente\n"))
    if eleccion == 1:
        cadena = generacion()
        return cadena
    elif eleccion == 2:
        cadena = input("Ingrese la cadena: ")
        cadena = cadena + '\n'
        if not cadena: #Se revisa si la cadena no está vacía
            print("El formato que usted proporcionó no es correcto, la cadena está vacía y n debe ser mayor o igual a 1")
        else:
            #Se revisará la integridad de la cadena
            #Se revisan los simbolos de la cadena
            for i in cadena:
                if i != '0' and i != '1' and i != '\n':
                    print("La cadena tiene simbolos distintos a 0 y 1, ingrese una nueva cadena")
                    counter = counter + 1
                    return False
            if counter == 0:
                confirmacion = validacionDeCadena(cadena) #Aqui se manda la cadena al proceso de validación para revisar si en cada extremo de la cadenas hay solo 0 y 1 respectivamente
                if confirmacion == True:
                    return cadena
                else:
                    print("La cadena no tiene una proporción simetrica de 0 en el lado izquierdo y 1 en el derecho")
                    return False
    else:
        print("Ingrese un numero correcto")
        return False

def validacionDeCadena(cadena):
    counterizq = 0
    counterder = 0
    longitudCadena = len(cadena) - 1 #Se le resta uno debido al caracter que ayudará a saber si la cadena ha terminado
    longitudCadenaMitad = (len(cadena) // 2)
    #Revisa el lado izquierda para ver si solo hay 0's 
    for i in range(0 , longitudCadenaMitad):
        if cadena[i] != '0':
            counterizq = counterizq + 1
            break

    #Revisa el lado izquierda para ver si solo hay 1's 
    i = 0
    for i in range(longitudCadenaMitad, longitudCadena):
        if cadena[i] != '1':
            counterder = counterder + 1
            break
    
    if counterizq == 0 and counterder == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    automata()
