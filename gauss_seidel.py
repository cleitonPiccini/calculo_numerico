#python 3
#Cleiton Piccini
# Algoritmo para resolução de sistemas lineares por Gauss-Seidel.

import numpy as np
#from numpy import linalg as LA

def  erro (x_anterior, x_atual, erro_value):
    
    #matriz_negativa = [-1,-1,-1]
    #x_negativo = np.multiply(matriz_negativa, x_anterior)

    erro_ = np.linalg.norm((x_atual - x_anterior)) / np.linalg.norm(x_atual)

    if erro_ > erro_value:
        return 1
    else:
        return 0

def diagonal_dominante(matriz):
    #
    if abs(matriz[0][0]) >= (abs(matriz[0][1]) + abs(matriz[0][2])) and abs(matriz[1][1]) >= (abs(matriz[1][0]) + abs(matriz[1][2])) and abs(matriz[2][2]) >= (abs(matriz[2][0]) + abs(matriz[2][1])):
        return 1
    else:
        return 0
#
def teste_sassenfeld(matriz):

    matriz_L = np.tril(matriz)
    matriz_U = matriz - matriz_L

    if (np.linalg.norm(np.dot(np.linalg.inv(matriz_L),matriz_U))) < 1 :
        return 1
    else :
        return 0

def seidel(matriz, matriz_result, x):

    #matriz_diagonal = np.diag(matriz)
    #matriz_restante = matriz - np.diagflat(matriz_diagonal)
    matriz_L = np.tril(matriz)
    matriz_U = matriz - matriz_L
    x_atual = x
    erro_ = 1
    aceitavel = float (0.00000000001)
    i = 0
    #Iterações
    while (erro_ == 1):
        x_anterior = x_atual
        #line_1 = (matriz_result[0] - (matriz[0][1] * x_atual[1]) - (matriz[0][2] * x_atual[2])) / matriz_diagonal[0]
        #line_2 = (matriz_result[1] - (matriz[1][0] * x_atual[0]) - (matriz[1][2] * x_atual[2])) / matriz_diagonal[1]
        #line_3 = (matriz_result[2] - (matriz[2][0] * x_atual[0]) - (matriz[2][1] * x_atual[1])) / matriz_diagonal[2]
        x_atual = np.dot(np.linalg.inv(matriz_L), matriz_result - np.dot(matriz_U,x_atual))
        #x_atual = np.array ([line_1,line_2,line_3])
        erro_ = erro(x_anterior,x_atual, aceitavel)
        i = i + 1
    print(i, "numero de execuções")
    return x_atual

'''___Main___'''

#matriz = np.array([[4.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 6.0, -2.0, 1.0, -1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 5.0, 0.0, -1.0, 0.0, 0.0, 0.0], [0.0, 2.0, 0.0, 5.0, -1.0, 1.0, -1.0, -1.0], [0.0, 0.0, -1.0, -1.0, 6.0, 0.0, 0.0, -1.0], [0.0, 0.0, -1.0, 0.0, -1.0, -1.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0, 0.0, 5.0, 4.0, -1.0], [0.0, 0.0, 0.0, -1.0, -1.0, 0.0, -1.0, 5.0]])
#matriz_resultados = np.array([-6.0, -5.0, 0.0, 1.0, 2.0, -12.0, -2.0, 10.0 ])
#x = np.array([[0, 0, 0, 0, 0, 0, 0, 0 ]])
matriz = np.array([[1, 2.4, (2.4**2), (2.4**3), (2.4**4)], [1, 2.8, (2.8**2), (2.8**3), (2.8**4)], [1, 3.2, (3.2**2), (3.2**3), (3.2**4)], [1, 3.4, (3.4**2), (3.4**3), (3.4**4)], [1, 3.8, (3.8**2), (3.8**3), (3.8**4)]])
matriz_resultados = np.array([11.02, 16.44, 24.53, 29.96, 44.70])
x = np.array([0, 0, 0, 0, 0])
#[, (**2), (**3), (**4), (**5)]
#, [3.8, (3.8**2), (3.8**3), (3.8**4), (3.8**5)]
#if teste_sassenfeld(matriz):
print( seidel(matriz, matriz_resultados, x))
#else:
#    print("matriz não converge.")

#print (x)