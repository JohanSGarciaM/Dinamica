
from fractions import Fraction
"""Función que recibe los parámetros necesarios para realizar la dinámica y
calcular el estado resultante del sistema despues de la cantidad de clicks indicados.
parámetros:
Matriz : Matriz booleana que indica la manera como se mueven las canicas
vector : Vector de estado principal que indica la cantidad de canicas que hay por vertice
t : Cantidad de clicks de tiempo que desea calcular
Retorno:
Resultado del sistema dinámico despues de una cantidad de clicks dada"""

def Booleana(matriz,vector,t):
    posible = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]!= 1 and matriz[i][j]!=0:
                posible = False
                break
    if posible:
        while t != 0:
            estado = [0 for i in range(len(vector))]
            for j in range(len(matriz)):
                for k in range(len(matriz[j])):
                    estado[j]= estado[j]+(matriz[j][k]*vector[k])
            vector = estado
            t-=1
        print(estado)
    else:
        print("No es una matriz de recorrido válida")

#Prueba Booleana([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]],[6,2,1,5,3,10],1)        
    

"""Función mejorada de la función Booleana cuyos valores son fracciones
parámetros:
Matriz : Matriz booleana que indica la manera como se mueven las canicas
vector : Vector de estado principal que indica la cantidad de canicas que hay por vertice
t : Cantidad de clicks de tiempo que desea calcular
Retorno:
Resultado del sistema dinámico despues de una cantidad de clicks dada"""            


#MATRIZ DOBLEMENTE ESTOCÁSTICA

def Fraccion(matriz,vector,t):
    posible = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]<0 or matriz[i][j]>1:
                posible = False
                break
    if posible:
        while t !=0:
            estado = [0 for i in range(len(vector))]
            for j in range(len(matriz)):
                for k in range(len(matriz[j])):
                    #Representación en Fracción de la libreria fractions
                    #estado[j]= Fraction(estado[j] + (matriz[j][k]*vector[k]))
                    #Representación en decimales
                    estado[j]= estado[j] + (matriz[j][k]*vector[k])
            vector = estado
            t-=1
        for i in range(len(estado)):
            estado[i]=round(estado[i],2)
        print(estado)
    else:
        print("No es una matriz de recorrido válida, no es doblemente estocastica")
                

# Prueba Fraccion([[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]],[1/6,1/6,2/3],1)



def multislit(slits,targets):
##    state = [[0 for i in range(slits+targets+1)]for j in range(slits+targets+1)]
##    for i in range(slits+targets+1):
##        for j in range(slits+targets+1):
##            value = input("Cuál es la probabilidad entre "+str(j)+" a "+str(i)+" : ")
##            if "/" in value:
##                numerador = int(value.split("/")[0])
##                denominador = int(value.split("/")[1])
##                state[i][j] =  round(numerador/denominador,2)
##            else:
##                state[i][j] = int(value)
    #Matriz estado multiplicada por si misma
    state = [[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]]
    statecopy = state
    new = [[0 for i in range(slits+targets+1)]for j in range(slits+targets+1)]
    for i in range(slits+targets+1):
        for j in range(slits+targets+1):
            suma = 0
            for k in range(slits+targets+1):
                suma+=state[j][k]*statecopy[k][i]
            new[j][i] = round(suma,2)
    

    for i in new : print(i)

    print("\n Vector resultante")

    #vector en punto inicial 0
    vector = [0 for i in range(slits+targets+1)]
    vector[0]=1
    
    Fraccion(new,vector,1)
    
            
        


# Matriz despues de dos clicks
#Fraccion([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1/6,1/3,0,1,0,0,0,0],[1/6,1/3,0,0,1,0,0,0],[1/3,1/3,1/3,0,0,1,0,0],[1/6,0,1/3,0,0,0,1,0],[1/6,0,1/3,0,0,0,0,1]],[1,0,0,0,0,0,0,0],1)

#Matriz inicial
#Fraccion([[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]],[1,0,0,0,0,0,0,0],1)


