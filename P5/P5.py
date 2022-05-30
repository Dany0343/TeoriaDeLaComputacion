# -*- coding: utf-8 -*-
#Librerias
from enum import auto
import random
from random import randint
import time

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
   
    print("Bienvenidx al automata de pila")
    print("El lenguaje del automata es {0^n 1^n | n >= 1}")
    #Se manda a generar la cadena con restricciones para poder operarla aquí
    cadena = proceso()
    if cadena == False:
        print("Se termina el programa")
    else:
        for i in cadena: 
            if i == '0':
                pila.append('0')
                continue
            elif i == '1':
                if pila[-1] == '0':
                    pila.pop()
                elif pila[-1] == 'z0' and i == '1':
                    print("Se terminó la cadena pero la pila sigue con algo, por lo tanto la cadena que ingresó no es valida y no sigue al lenguaje {0^n 1^n | n >= 1}")
                    break
                continue
            elif i == '\n':
                if pila[-1] == 'z0':
                    print("Se ha llegado a z0, la cadena es correcta!")
                break #Se termina el ciclo ya que se terminó de leer la cadena
        if len(cadena) <= 10:
            print("Si se puede graficar")
        else:
            print("La cadena es mayor a 10 caracteres, así que no hay graficación")
        # print(f"La cadena es: {cadena}")

def generacion():
    cadena = "" #Donde se guardará la cadena aleatoria
    numeroAleatorio = randint(1, 100001) #Mayor a uno
    numeroAleatorioMitad = numeroAleatorio // 2
    for i in range(1, numeroAleatorioMitad + 1): #Numero de cadenas a generar
        if numeroAleatorio == 1:
            cadena = cadena + '0'
        cadena = cadena + '0'
    for i in range(numeroAleatorioMitad, numeroAleatorio):
        if numeroAleatorio == 1:
            cadena = cadena + '1'
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