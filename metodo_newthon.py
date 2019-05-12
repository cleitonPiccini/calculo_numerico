#Author Leonardo Lisboa
import math
print("Método de Newton")
print("Qual a aproximação inicial X0 e a precisão e?")
x0=float(input("Entre com x0"))
e=float(input("Entre com e"))
i=0
cd=30 #numero de casa decimais para arredondamento de Wx
def Fx(x):# Função
    Fx=math.exp(-x**2+1)+math.sin(x**2)-x
    return Fx
def Wx(x): # Função de interação
    Wx=x-(math.exp(-x**2+1)+math.sin(x**2)-x)/(-2*x*math.exp(-x**2+1)+math.cos(x**2)*2*x-1)
    return Wx
#Fazendo as iterações
while True:
    i+=1
    x=Wx(x0)
    if abs(Fx(x)) < e or abs(x-x0)<e:
        break
    else:
        x0=x
print("Raiz = ",x)
print("Iterações = ",i)