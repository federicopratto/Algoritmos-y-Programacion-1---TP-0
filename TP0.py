#Pre: Recibe dos palabras previamente inicializadas.
#Post: Devuelve la cantidad de letras que suman ambas palabras.
def sumarLetras (palabra1, palabra2):
    suma = len(palabra1+palabra2)    
    return suma
    
#Pre: Recibe dos palabras previamente inicializadas.
#Post: Devuelve true en caso de que la palabra uno sea mas larga o de igual
#longitud que la dos, false en caso contrario.
def determinarPalabraMasLarga(palabra1, palabra2):
    if(len(palabra1)>=len(palabra2)):
        return True
    return False

#Pre: Recibe tres valores previamente inicializados: horas, minutos y segundos.
#Post: Devuelve la duracion en segundos del intervalo de tiempo que surge de la suma de la duracion
#en segundos de los tres parametros. EJ: horas: 1, minutos: 3, segundos: 117 devuelve: 3897
def cantidadDeSegundos(horas, minutos, segundos):
    return (segundos+minutos*60+horas*3600)

#Pre: Recibe un numero previamente inicializado.
#Post: Devuelve True si el numero es par, False en caso contrario.
def esPar(numero):
    if(numero%2==0):
        return True
    return False
    
#Pre: Recibe tres numeros previamente inicializados.
#Post: Devuelve el mayor producto entre dos de ellos
#EJ: Si recibe (5,3,8), debe devolver 40.
def mayorProducto(numeroUno, numeroDos, numeroTres):
    resultado1 = numeroUno*numeroDos
    resultado2 = numeroDos*numeroTres
    resultado3 = numeroTres*numeroUno
    
    if(resultado2<=resultado1>=resultado3):
        return resultado1
    elif(resultado1<=resultado2>=resultado3):
        return resultado2
    return resultado3