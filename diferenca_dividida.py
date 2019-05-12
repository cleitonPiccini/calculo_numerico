#PYTHON 3

#Algoritimo para interpolação, OPERADOR DE DIFERENÇA DIVIDADA

def calc_f (vetor_f, vetor_x, k):
	ordem = 0
	valor = 0
	k_aux = k
	result = []
	anterior = vetor_f
	while (ordem <= k):
		i = 0
		if (ordem == 0):
				#anterior[i] = valor
				result.append(vetor_f[0])
				ordem+=1
				k_aux-=1
				continue
		#anterior[i] = valor
		while (i < k_aux):
			anterior[i] = (anterior[i+1] - anterior[i]) / (vetor_x[i+1] - vetor_x[i])
			#result.append(valor)
			#valor_1 = (valor - anterior) / (vetor_x[i] - vetor_x[0])
			#print (valor_1, "teste calc_f", valor, anterior)
			i+=1
		result.append(anterior[0])
		ordem+=1
		k_aux-=1
	return result

def calc_x (vetor_x, x, k):
	i = 0
	valor = 1
	while (i <= k):
		valor = (x - vetor_x[i]) * valor
		i+=1
	print (valor, "teste calc_x")
	return valor


def diferenca_dividida (vetor_x, vetor_f, x):
	i = 0
	valor = 1
	f_x = calc_f(vetor_f, vetor_x, len (vetor_f))
	if (len (vetor_x) == len (vetor_f)):
		while (i < len(vetor_x)):
			print ("valor antes da conta, ", valor)
			valor = valor * (f_x[i] + calc_x(vetor_x, x, i))
			print ("resultado,", valor ," f de x, ", f_x[i], " e x ", (x - vetor_x[i]))
			i+=1
	else :
		print("Vetores com tamanho incorreto.")
	return valor

'''__main__'''
vetor_x = [2.6, 3.2, 3.4, 3.8]
vetor_f = [13.46, 24.53, 29.96, 44.70]
x = 3.14
print (diferenca_dividida(vetor_x, vetor_f, x))