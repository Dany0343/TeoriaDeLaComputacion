import random
from random import randint
import time
# Realizar un programa que simule el funcionamiento de un protocolo utilizando un AFD.

# 1. El programa debe funcionar automáticamente.
# 2. Debe de verificar si el protocolo está encendido o apagado y ejecutarse nuevamente si está encendido. El programa deberá determinar automáticamente para detenerse.
# 3. Generar 10^6 cadenas binarias aleatoriamente de longitud 64.
# 4. Hacer que el programa se espere 1 segundo.
# 5. Posteriormente validar cada una de las cadenas con el AFD de paridad.
# 6. Generar cuatro archivos de texto para las salidas. El primer archivo tendrá todas las cadenas generadas, el segundo archivo tendrá las cadenas aceptadas y el tercer archivo las cadenas rechazadas. Si el programa entra más de una vez, los archivos deben de almacenar los datos de todas las corridas. Un cuarto archivo debe de tener la historia de la evaluación de los autómatas, es decir, imprimir cada cambio de estado.
# 7. Tener la opción de graficar el AFD completo (protocolo y paridad en el mismo grafo).
# 8. En el reporte debe de estar también el código de la implementación.


#Generacion de 1 millon de cadenas binarias de 64 bits
k = 0 #iterador para mostrar las veces que el automata ha encendido

def cadenas():
    f = open("Programa3_Cadenas.txt", "a", encoding="utf-8") #Es importante poner el parametro 'a' para que añada al final y no sobreescriba todo.
    for i in range(0, 10000):
        for j in range(0, 6):
            aux = randint(0,1)
            f.write(str(aux))
        f.write('\n')
    f.close()

def afd_paridad():
    cadena = 0
    f = open("Programa3_Cadenas.txt", 'r')
    g = open("Programa3_CadenasAceptadas.txt", "a", encoding="utf-8")
    h = open("Programa3_CadenasRechazadas.txt", "a", encoding="utf-8")
    for i in f:
        if i != '\n':
            cadena = i
            estado = 'q0'
            for j in cadena:
                if estado == 'q0' and j == '\n': 
                    g.write(i)
                    #g.write('\n')
                    break
                elif j == '\n' and (estado == 'q1' or estado == 'q2' or estado == 'q3'):
                    h.write(i)
                    #h.write('\n')
                    break
                elif estado == 'q0' and j == '0':
                    estado = 'q2' 
                    continue
                elif estado == 'q0' and j == '1':
                    estado = 'q1'
                    continue
                #Termina primer fila
                elif estado == 'q1' and j == '0':
                    estado = 'q3'
                    continue
                elif estado == 'q1' and j == '1':
                    estado = 'q0'
                    continue
                #Termina segunda fila
                elif estado == 'q2' and j == '0': 
                    estado = 'q0'
                    continue
                elif estado == 'q2' and j == '1':
                    estado = 'q3'
                    continue
                #Termina tercer fila
                elif estado == 'q3' and j == '0':
                    estado = 'q1'
                    continue
                elif estado == 'q3' and j == '1':
                    estado = 'q2'
                    continue
        else:
            print("Espacio vacío")
    g.close()
    h.close()
    protocolo()

def protocolo():
    global k
    global estado
    estado = random.choice([True, False])
    if estado == True:
        k += 1
        print("Se inicia el Automata")
        print(f"Esta es la iteracion {k}")
        cadenas()
        time.sleep(1)
        afd_paridad()
    else: 
        print("El automata está apagado")


#Se manda a llamar a la funcion principal del automata
protocolo()
