#python 3
#Cleiton Piccini
#Algoritmo do metódo de Newton para encontrar raizes de funções.

import math

# Função
def funcao (x):
    #x = (x / (math.e**(10*x))) - (1 / (math.e ** 5))
    x = math.cos(50 * x + 10) - math.sin(50 * x - 10)
    return x

# Derivada da Função
def derivada (x):
    #x = (math.e**(-10*x)) * (1 - 10 * x)
    x = -50 * (math.sin(50 * x + 10) + math.cos(50 * x - 10))
    return x

# Metodo de Newton
def newton(x, i, erro):
	#
	i = i + 1
	x_funcao = funcao (x)
	x_derivada = derivada (x)
	x_novo = x - (x_funcao / x_derivada)
	#
	if abs((x_novo - x) / x_novo) < erro or x_derivada == 0.0:
		print("Iterações = ",i)
		return x_novo
	else :
		return newton (x_novo, i, erro)

#
'''_Main_'''
i = 0
x = -0.5
erro = 0.0000000001

x = newton (x, i, erro)

print("Raiz = ",x)