#PYTHON3

#Algoritmo de LaGrange para cálculo de interpolação.


# Função que cálcula o Li(x), para aplicar o valor no algoritmo de Lagrange.
def Lx (vetor_x, k, x):
	i = 0
	valor1 = 1
	valor2 = 1
	while (i < len(vetor_x)):
		# Garantindo que algum número seja subtraido por ele mesmo, assim garante que não exista divisão por zero.
		if (i != k):
			valor1 = (x - vetor_x[i]) * valor1
			valor2 = (vetor_x[k] - vetor_x[i]) * valor2
		i+=1
	return valor1 / valor2


# Função que executa o algoritmo de LaGrange.
def lagrange (vetor_f,vetor_x, x) : 
	k = 0
	valor = 0
	if (len (vetor_f) == len (vetor_x)) :
		while (k < len(vetor_x)):
			valor = valor + (vetor_f[k] * Lx(vetor_x,k,x))
			k+=1
	else:
		print ("Erro no tamanho dos vetores.")
	return valor

'''___main___'''

vetor_f = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
vetor_x = [2, 20, 25, 40, 63, 110, 160, 202, 250, 280]
x = 165

print (lagrange(vetor_f, vetor_x, x))