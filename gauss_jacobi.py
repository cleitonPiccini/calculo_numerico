#python 3
#Cleiton Piccini
# Algoritmo para resolução de sistemas lineares por Gauss-Jacobi.

import numpy as np
from numpy import linalg as LA

def  erro (x_anterior, x_atual, erro_value):

	erro_ = LA.norm((x_atual - x_anterior)) / LA.norm(x_atual)

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

def teste_sassenfild (matriz):
    
    matriz_diagonal = np.diag(matriz)
    matriz_restante = matriz - np.diagflat(matriz_diagonal)
    print (np.linalg.inv( np.tril(matriz)),"tril na matriz")

    print (np.diagflat(matriz_diagonal), "diagflat()")
    print (matriz_diagonal)
    print (matriz_restante)   
    print (abs(np.nansum(matriz_restante,axis=1)), "sum()")# / matriz_diagonal)

def jacobi(matriz, matriz_result, x):

    matriz_diagonal = np.diag(matriz)
    matriz_restante = matriz - np.diagflat(matriz_diagonal)
    x_atual = x
    erro_ = 1
    aceitavel = float (0.000000001)
    i = 0
    while (erro_ == 1):
        x_anterior = x_atual
        x_atual = (matriz_result - np.dot(matriz_restante, x_atual)) / matriz_diagonal
        erro_ = erro(x_anterior,x_atual, aceitavel)
        i = i + 1
    print(i, "numero de execuções")
    return x_atual

'''___Main___'''

matriz = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
matriz_resultados = np.array([1.0, 2.0, 3.0])
x = np.array([0, 0, 0])
teste_sassenfild(matriz)
print (jacobi(matriz, matriz_resultados, x))