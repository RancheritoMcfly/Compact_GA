import numpy as np

def compact_ga(n, l):    
    #Apartado de construcción de vectores 
    vector = np.full(l, 0.5) 
    #ciclo
    while(((np.sum(vector)) <= l) and ((np.sum(vector)) > 0)):        
        eva_adan = np.random.random((2,l))
        eva_adan = (eva_adan <= vector).astype(int)
        if(np.sum(eva_adan[0]) <= np.sum(eva_adan[1])):
            for index, (i, j) in enumerate(zip(eva_adan[0], eva_adan[1])):
                if(i != j):
                    if(i == 1):
                        vector[index] += 1/n
                    else: vector[index] -= 1/n        
        else: 
            for index, (i, j) in enumerate(zip(eva_adan[1], eva_adan[0])):
                if(i != j):
                    if(i == 1):
                        vector[index] += 1/n
        vector = np.around(vector, decimals= l)   
    print(vector)

compact_ga(100,5)