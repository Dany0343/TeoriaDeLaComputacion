from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer
import math
#Variables
opcion = 0
menu = 0
ntotal = []
nsimbolos = []
contador = 0
contadorUnos = 0
unos = []
k = 0
#Funciones
def primos(opcion):
    global contador
    global contadorUnos
    global k
    k = 0
    f = open("Programa2.txt", "w", encoding="utf-8")
    g = open("Programa2_1.txt", "w", encoding="utf-8")
    f.write('Conjunto decimal\nΣ^* = ' + '{')
    g.write('Conjunto Binario\nΣ^* = ' + '{')
    for i in range(1, opcion + 1):
        for j in range(2, (i//2) + 1):
            if i % j == 0:
                break
        else:
            aux = bin(i)[2:]
            contador = contador + len(aux)
            contadorUnos += aux.count('1')          
            nsimbolos.append(contador)
            unos.append(contadorUnos)
            g.writelines(aux + ',')
            f.writelines(str(i)+ ',')
            f.write("\n")
            g.write("\n")
            k+=1
        contador = 0
        contadorUnos = 0
    f.write('}')
    g.write('}')
    print("Revise el archivo llamado Programa2.txt y el programa llamado Programa2_1.txt\n")
    f.close()
    g.close()

def graficacion():
    plt.clf()
    i = 0
    for i in range(1, k + 1): #llenando la lista del eje x respecto a lo elegido por el usuario
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
while 1:
    print("Bienvenido a la calculadora de lenguaje binario definido por numeros primos, esperemos disfrute su estancia")
    menu = int(input("1.Ingresar numero\n2.Numero aleatorio\n3.Salir\n\n"))
    if menu == 1:
        opcion = int(input("Ingrese el numero hasta donde desea obtener los numeros primos: "))
        if opcion > 2 and opcion < 20000000:
            nsimbolos = []
            ntotal = []
            unos = []
            inicio = default_timer()
            primos(opcion)
            fin = default_timer()
            tiempo = fin - inicio
            if tiempo > 120:
                tiempo = tiempo / 60
                print(f"El tiempo de ejecucion fue: {tiempo} minutos\n")
            else:
                print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
            print(f"En el número que usted eligió hay {k} numeros primos\n")
            graficacion()
        else:
            print("Ingrese un numero valido")
    elif menu == 2:
        nsimbolos = []
        ntotal = []
        unos = []
        opcion = randint(2, 20000000)
        inicio = default_timer()
        primos(opcion)
        fin = default_timer()
        tiempo = fin - inicio
        if tiempo > 120:
            tiempo = tiempo / 60
            print(f"El tiempo de ejecucion fue: {tiempo} minutos\n")
        else:
            print(f"El tiempo de ejecucion fue: {tiempo} segundos\n")
        print(f"En el número que usted eligió hay {k} numeros primos\n")
        graficacion()
    elif menu == 3:
        print("Hasta pronto!")
        break;
    else: 
        print("Digite una opción correcta")
    menu = input("Desea calcular otro numero? [Si/No]: ").lower()
    if menu == 'no':
        print("Hasta pronto!")
        break