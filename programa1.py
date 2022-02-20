#Variables
from random import randint
from timeit import default_timer
import matplotlib.pyplot as plt
i = 0
j = 0
decision = ""
opcion = 0
nsimbolos = []
ntotal = []
contador = 0
#Funciones

def binarios(opcion): 
    #cadenas = ['{', 'ε']
    global contador
    f = open("Programa1.txt", "w", encoding="utf-8")
    f.write('Σ^* = ' + '{' + 'ε' + ',' + "\n")
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
                    contador = contador + len(aux)
                    f.writelines(aux + ",")
                    #cadenas.append(aux) esto es usando una lista (mucha memoria)
                else: 
                    f.writelines(aux + ",")
                    contador = contador + len(aux)
                    #cadenas.append(aux)
            nsimbolos.append(contador)
            contador = 0
            f.write("\n\n")
        #cadenas.append('}')
        f.write('}')
        f.close()
    else: 
        print("El numero está fuera del rango\n\n")
    #formateando si se usara una lista
    # i = 0
    # for i in range(len(cadenas)):
    #     f.write(cadenas[i] + "\n")
    # f.close()


def graficacion(opcion):
    plt.clf()
    i = 0
    for i in range(1, opcion + 1): #llenando la lista del eje x respecto a lo elegido por el usuario
        ntotal.append(i)

    puntosx = ntotal
    puntosy = nsimbolos
    plt.plot(puntosx, puntosy)
    plt.xlabel("Numeros de cadenas")
    plt.ylabel("Numeros de simbolos por cadena")
    plt.show()
    


#Menu 
while decision != "no":
    print("Bienvenido a la calculadora de universos de cadenas binarias!")
    decision = int(input("1. Introducir numero\n2. Número aleatorio entre 1-1000\n3. Salir\n\n"))

    if decision == 1:
        opcion = int(input("Introduzca el numero de hasta donde desea obtener el universo de cadenas: "))
        #Mandando a llamar a la funcion y midiendo el tiempo
        inicio = default_timer()
        binarios(opcion)
        fin = default_timer()
        tiempo = fin - inicio
        print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
        print("Revise el archivo llamado Programa1.txt\n\n")
        graficacion(opcion)

    elif decision == 2:
        random = randint(1,1000)
        inicio = default_timer()
        binarios(random)
        fin = default_timer
        tiempo = fin - inicio
        print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
        print("Revise el archivo llamado Programa1.txt\n\n")
        graficacion()

    elif decision == 3: 
        print("Hasta pronto!")
        break
    else:
        print("INGRESE UNA OPCION VALIDA \n\n")
    decision = input("Desea calcular de otro numero? [si/no]: ").lower()
    if decision != 'si' and decision != 'no':
        print("Hasta pronto!")
        break