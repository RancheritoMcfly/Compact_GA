import numpy as np

def CGA(poblacion, dimension):
    
    """Se construyen las variables, el vector de probabilidad y los dos 
    vectores aleatorios"""   
    vector = np.full(dimension,0.5)
    adan = np.random.random(dimension)
    eva = np.random.random(dimension)
    """pondero al ganador y perdedor con esta función.
    El ganador es el que contiene menos cantidad de 1 dentro de su estructura."""
    ganador, perdedor = competir(adan, eva, vector)
    """Utilizo una banderita para poder tener el criterio de paro en el ciclo."""
    flag = True
   
    while(flag):
        """En este primer apartado reviso los valores de ganador y perdedor para
        compararlos entre ellos y poder realizar la actualización del vector de
        probabilidad
        
        """
        for index, (g, p) in enumerate(zip(ganador, perdedor)):
            if(g != p):
                if( g == 1):
                    vector[index] += 1/poblacion
            else: vector[index] -= 1/poblacion
        #print("Vector actualizado: ", vector) 
        
        """En este apartado hacemos la comprobación para saber si ya 
        los valores dentro del vector de probabilidad se encuentran fuera
        del rango de >0 y <1"""
        for i in vector:
            if(i > 0 and i < 1):
                adan = np.random.random(dimension)
                eva = np.random.random(dimension)
                ganador, perdedor = competir(adan, eva, vector)
            else: flag = False
 
    print("Vector final: ", vector)    
        
def competir(adan, eva, vector):
    """Utilizo los indices y los valores dentro de cada competidor
    para poder saber como sustituirlo, presenté algunos problemas por
    revisarlos en conjunto, por ello los maneje por separado.
    Recordando que la premisa es 'si es mayor al valor de probabilidad
    se sustituye por un 1 y por el contrario si es menor ó igual se sustituye por
    un 0'"""
    for index, (a, v) in enumerate(zip(adan, vector)):
        if (a <= v):
           adan[index] = 1
        else:
            adan[index] = 0
    for index, (e, v) in enumerate(zip(eva, vector)):
        if (e <= v):
           eva[index] = 1
        else:
            eva[index] = 0
    
    """La comparativa es sencilla, el de mayor cantidad de 1´s pierde.
    Si son iguales, no importa cual mande(o eso creo)."""
    if(np.sum(adan) >= np.sum(eva)):
        return eva, adan
    else:
        return adan, eva

CGA(12, 5) 
"""Parametros: 1.- Cantidad de individuos en la poblacion simulada y 
2.- cromosomas por individuo"""