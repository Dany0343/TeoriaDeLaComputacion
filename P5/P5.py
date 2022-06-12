import random
from time import sleep
import pygame

#Tabla de estados que contiene los posibles resultados
tablaEstados = {
        'a' : {'B': 'be', 'R': 'f'},
        'b' : {'B': 'eg', 'R': 'acf'},
        'c' : {'B': 'bdg', 'R': 'fh'},
        'd' : {'B': 'g', 'R': 'ch'},
        'e' : {'B': 'bj', 'R': 'afi'},
        'f' : {'B': 'ebjg', 'R': 'acik'},
        'g' : {'B': 'bdjl', 'R': 'cfik'},
        'h' : {'B': 'gdl', 'R': 'ck'},
        'i' : {'B': 'ejm', 'R': 'gn'},
        'j' : {'B': 'egmo', 'R': 'fikn'},
        'k' : {'B': 'jglo', 'R': 'fhnp'},
        'l' : {'B': 'go', 'R': 'hkp'},
        'm' : {'B': 'j', 'R': 'in'},
        'n' : {'B': 'mjo', 'R': 'ik'},
        'o' : {'B': 'jl', 'R': 'nkp'},
        'p' : {'B': 'ol', 'R': 'k'}
}

def cadenaRandom(numero): #Genera un string de forma random 
    auxiliar = "" #Variable auxiliar
    for i in range(numero):
        x = random.randint(1, 2) #Función para generar un resultado random de una lista
        if x % 2 == 0:
            auxiliar = auxiliar + "R"
        else:
            auxiliar = auxiliar + "B"
    return auxiliar

def ajedrez(ruta, inicio): #Recibe una ruta y la personaliza ya sea para el jugador uno o dos
    rutas = open("Practica5Rutas"+inicio+".txt", "w+")
    for i, j in enumerate(revRutas(inicio, ruta), 1):
        rutas.write(''.join(j))
        rutas.write("\n")
    print(f"Todas las rutas encontradas: {str(i)}")

def revRutas(inicio, ruta): #Toma el inicio y la ruta y devuelve el inicio con yield, así cada iteración
    if not ruta: #Revisa si la ruta no está vacía 
        yield (inicio,)
        return
    primero, *nuevaRuta = ruta # unpacking, el primer elemento se guarda en la variable primero y luego lo demás se guarda en nueva ruta
    for estado in tablaEstados[inicio][primero]:
        for ruta in revRutas(estado, nuevaRuta):
            yield (inicio,) + ruta

def mejRutas(posibles,ultimo): #Obtiene un archivo y su nombre del ultimo para poder distinguirlo
    
    rutasGanadoras = open("Practica5RutasGanadoras"+ultimo+".txt", "w+")
    with open(posibles) as openfileobject:
        i = 0
        tablero = []
        for renglon in openfileobject:
            if ultimo in renglon: 
                limpiar = limpiarRutas(ultimo, renglon)
                rutasGanadoras.write(renglon)
                rutasGanadoras.write("\n")
                tablero.append(limpiar)
                i = i + 1
        #Remueve duplicados
        duplicados = list(dict.fromkeys(tablero))
        #ordena
        tableroF = sorted(duplicados, key=lambda x: len(x)) #Se usa una función anonima para tener menos codigo
        print("Las rutas ganadoras encontradas:" + str(i))
        print("Las mejores rutas: ")
        print(tableroF[-5:])
    return tableroF[-5:] #Devuelve las mejores rutas

def limpiarRutas(ultimo, ruta):
    index = ruta.index(ultimo) #Encuentra el indice del ultimo caracter de la ruta
    return ruta[0:index+1]

class ficha(): #Clase ficha donde cada moneda obtendrá estas propiedades
    def __init__(self, image): #Se manda a si mismo (.image) para pygame
        self.image = image
    
    def convertidor(self,ruta, tamano): #Toma una cadena y lo convierte en un conjunto de tuplas
        tablaCoordenadas = {
        'a' : (1*tamano, 1*tamano), 'b' : (2*tamano, 1*tamano), 'c' : (3*tamano, 1*tamano), 'd' : (4*tamano, 1*tamano),
        'e' : (1*tamano, 2*tamano), 'f' : (2*tamano, 2*tamano), 'g' : (3*tamano, 2*tamano), 'h' : (4*tamano, 2*tamano),
        'i' : (1*tamano, 3*tamano), 'j' : (2*tamano, 3*tamano), 'k' : (3*tamano, 3*tamano), 'l' : (4*tamano, 3*tamano),
        'm' : (1*tamano, 4*tamano), 'n' : (2*tamano, 4*tamano), 'o' : (3*tamano, 4*tamano), 'p' : (4*tamano, 4*tamano)
        }
        rutaL = []
        for i in ruta:
            rutaL.append(tablaCoordenadas.get(i)) #Retorna el valor especificado del diccionario
        self.route = rutaL

def recalcularRutas(ruta1:list, ruta2:list, intento:int, inicio:int):
    try: #Se utiliza un try catch para poder revisar el ciclo for y con la excepcion de un indexerror el cual devuelve false y las dos rutas
        for i in range( len(ruta1) ):
            if(ruta1[i]==ruta2[i]):
                if intento == 2:
                    if inicio == 1:
                        ruta2.insert(i,ruta2[i-1])
                    else:
                        ruta1.insert(i,ruta1[i-1])
                    return False, ruta1, ruta2
                else:
                    return True, ruta1, ruta2
        return False, ruta1, ruta2
    except IndexError:
        return False, ruta1, ruta2

def juego():
    while True:
        eleccion = input("1.Modo automatico\n2.Modo manual \n")
        if eleccion == "1":
            jugadores = random.choice([1, 2])
            ruta = cadenaRandom(random.randint(1,10)) #Se genera de forma aleatoria del 1-10

        elif eleccion == "2":    
            jugadores = int(input("Numero de jugadores\n1 o 2: \n"))
            if jugadores < 1:
                print(f"No se puede tener un numero de jugadores de {jugadores}")
                break
            elif jugadores > 2:
                print("No se pueden tener más de 2 jugadores")
                break
            ruta = input("Ingrese la cadena usando R y B\n1. Para generarla de forma aleatoria \n").upper()
            
            if ruta == "0":
                ruta = cadenaRandom(random.randint(1,10)) #Se genera de forma aleatoria del 1-10
        
            if len(ruta) >= 100:
                print("No es posible introducir más de 100 caracteres")
                break
        else:
            print("Elija un numero correcto")
            break

        print(f"La ruta a evaluar es: {ruta}")
        
        #Calculo de las rutas de ambos jugadores
        print("Calculando rutas del primer jugador")
        ajedrez(ruta, 'a')
        ruta1 = mejRutas("Practica5Rutasa.txt", 'p') #Se le manda un archivo de texto de las rutas 1 y el parametro a
        j1ficha = ficha('P5/p5j1.png')
        j1 = pygame.image.load(j1ficha.image)
        j1 = pygame.transform.scale(j1, [50,50])
        
        #Para 2 jugadores
        if jugadores >= 2: 
            print("Calculando rutas del segundo jugador")
            ajedrez(ruta, 'd')
            ruta2 = mejRutas("Practica5Rutasd.txt", 'm')
            j2ficha = ficha('P5/p5j2.png')
            j2 = pygame.image.load(j2ficha.image)
            j2 = pygame.transform.scale(j2, [50,50])
        
        #Salidas
        try:
            if jugadores >= 2:
                inicio = random.choice([1, 2])
                print(f"Inicio: {str(inicio)}")
                #Convierte en lista el primer elemento de la ruta 1 y ruta 2
                aceptado, rutafinal1, rutafinal2 = recalcularRutas(list(ruta1[0]), list(ruta2[0]), 1, inicio)
                if aceptado: #Si el valor de aceptado es True entra en el if
                    if inicio == 1:
                        #Convierte en lista el primer elemento de la ruta 1 y ruta 2
                        aceptado, rutafinal1, rutafinal2 = recalcularRutas(list(ruta1[0]), list(ruta2[0]), 2, inicio)
                    else:
                        #Convierte en lista el primer elemento de la ruta 1 y ruta 2
                        aceptado, rutafinal1, rutafinal2 = recalcularRutas(list(ruta1[1]), list(ruta2[0]), 2, inicio)
                rf1 = ''.join(rutafinal1)
                rf2 = ''.join(rutafinal2)
                # print(rf1)
                # print(rf2)
            else:
                rf1 = ruta1[0]
                # print(rf1)
            pygame.display.init()
            
            #colores               
            negro = (28,27,23)  
            rojo = (255,0,0)
            #set display
            gameDisplay = pygame.display.set_mode((600,600))
            pygame.display.set_caption("Ajedrez")
            
            #Cuadros
            tcuadros = 100

            longitudA = 4
            gameDisplay.fill('white')
            counter = 0
            #Se dibuja la cuadricula y se pinta
            for i in range(1,longitudA + 1):
                for j in range(1,longitudA + 1):
                #revisa si es par
                    if counter % 2 == 0:
                        pygame.draw.rect(gameDisplay, negro,[tcuadros*j, tcuadros*i,tcuadros,tcuadros])
                    else:
                        pygame.draw.rect(gameDisplay, rojo, [tcuadros*j,tcuadros*i,tcuadros,tcuadros])
                    counter = counter + 1

                counter = counter -1

            pygame.draw.rect(gameDisplay,negro,[tcuadros,tcuadros,longitudA*tcuadros,longitudA*tcuadros],1)
            gameDisplay.blit(j1,[tcuadros,tcuadros])
            j1ficha.convertidor(rf1, tcuadros)
            
            if jugadores >= 2 :
                gameDisplay.blit(j2,[4 * tcuadros, tcuadros])
                j2ficha.convertidor(rf2, tcuadros)

            #Muestra a los jugadores en la cuadricula
            pygame.display.update()
            
            if jugadores >= 2:
                if len(j1ficha.route) > len(j2ficha.route):
                    movimientos = len(j2ficha.route)
                else:
                    movimientos = len(j1ficha.route)
                try:
                    if inicio == 1:
                        for i in range(movimientos):
                            gameDisplay.blit(j1,list(j1ficha.route[i]))
                            pygame.display.update()
                            sleep(3)
                            gameDisplay.blit(j2,list(j2ficha.route[i]))
                            pygame.display.update()
                            sleep(3)
                    else:
                        for i in range(movimientos):
                            gameDisplay.blit(j2,list(j2ficha.route[i]))
                            pygame.display.update()
                            sleep(3)
                            gameDisplay.blit(j1,list(j1ficha.route[i]))
                            pygame.display.update()
                            sleep(3) 
                    print("La partida ha terminado")
                    sleep(10)
                    pygame.display.quit()
                except IndexError:
                    print("La partida ha terminado")
                    sleep(10)
                    pygame.display.quit()
            else:
                for i in j1ficha.route:
                    gameDisplay.blit(j1,list(i))
                    pygame.display.update()
                    sleep(3)
                print("La partida ha terminado")
                sleep(10)
                pygame.display.quit()
        
        except IndexError:
            print("No hay rutas ganadoras")
        
        opc = int(input("1.Salir\n2.Volver a empezar\n"))
        if opc != 2:
            print("Hasta pronto!")
            pygame.display.quit()
            break
            quit() #Se sale completamente de python
#Entry point del programa
if __name__ == "__main__":
    juego()