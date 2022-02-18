#Variables
from random import randint
i = 0
j = 0
decision = ""
opcion = 0
f = open("Programa1.txt", "w")
#Funciones
def binarios(): 
    cadenas = ['{', 'ε']
    opcion = int(input("Introduzca el numero de hasta donde desea obtener el universo de cadenas\n"))
    if opcion > 0 and opcion < 100: 
        for i in range(1, opcion + 1):
            for j in range(0, 2 ** i): #Recorrer y generar la cadena desde 0 hasta el numero especificado
                #Conversion a binario
                aux = str(bin(j))[2:]
                tam = len(aux)
                if tam < i: 
                    #modo manual
                    #zeros = '0' * i
                    #aux = zeros + aux
                    #function mode
                    aux = aux.zfill(i)
                    cadenas.append(aux)
                else: 
                    cadenas.append(aux)
        cadenas.append('}')
    else: 
        print("El numero está fuera del rango\n\n")
    
    #formateando
    i = 0
    for i in range(len(cadenas)):
        f.write(cadenas[i] + "\n")
    f.close()

    
    print(cadenas)

def binariosRandom():
    random = randint(1,10)
    print(random)
    cadenas = ['{', 'ε']
    if random > 0 and random < 100: 
        for i in range(1, random + 1):
            for j in range(0, 2 ** i): #Recorrer y generar la cadena desde 0 hasta el numero especificado
                #Conversion a binario
                aux = str(bin(j))[2:]
                tam = len(aux)
                if tam < i: 
                    #modo manual
                    #zeros = '0' * i
                    #aux = zeros + aux
                    #function mode
                    aux = aux.zfill(i)
                    cadenas.append(aux)
                else: 
                    cadenas.append(aux)
        cadenas.append('}')
    else: 
        print("El numero está fuera del rango\n\n")

    i = 0
    for i in cadenas:
        f.write(i + "\n")
    f.close()
    print(cadenas)
    

#Menu 
while decision != "no":
    print("Bienvenido a la calculadora de universos de cadenas binarias!")
    decision = int(input("1. Introducir numero\n2. Número aleatorio entre 1-1000\n3. Salir\n"))
    if decision == 1:
        binarios()
    elif decision == 2:
        binariosRandom()
    elif decision == 3: 
        break
    else:
        print("INGRESE UNA OPCION VALIDA \n\n")
    decision = input("Desea calcular de otro numero?\n[si/no] \n\n").lower()
    if decision != 'si' and decision != 'no':
        break