# -*- coding: utf-8 -*-
'''Script para hacer gráficas en python. 
Los argumentos de las funciones trigonométricas deben ser en radianes
Métodos la librería math:
1.	Valor absoluto -- math.fabs(num)
2.	Función exponencial -- math.exp(num)
3.	Potencia -- math.pow(base,exponente)
4.	raíz cuadrada -- math.sqrt(num)
5.	Coseno -- math.cos(num)
6.	Seno -- math.sin(num)
7.	Tangente -- math.tan(num)
8.	Conversión de radianes a grados math.degree(num)
9.	pi -- math.pi
10.	Número de euler -- math.e
11.	Arcoseno -- math.acos(num)
12.	Arcseno -- math.asin
'''


#Solo se importa el método pyplot, no toda la librería
#Además se renombra a una variable llamada plt
#Si se omitiera la parte 'as plt' no se podría llamar a grid, plot y show como están en las últimas
#tres líneas, sino que debería ponerse el nombre completo, ejemplo: matplotlib.pyplot.grid(True)
 
import matplotlib.pyplot as plt 
import math
import os
#Función y=f(x)
def fun(x):
	f=math.fabs(x)
	return f
os.system('clear')
n=float(input('Número de puntos = '))#Número de puntos del vector sin contar el punto inicial
a=float(input('a = '))#Límite inferior del intervalo
b=float(input('b = '))#Límite superior del intervalo

x=[a]#Primer elemento del vector x (abscisa)
y=[]
paso=(b-a)/n#Tamaño del incremento del vector x

bi=a #Acumulador para ir llenando el vector x

#Ciclo para llenar al vector x
while bi<b:
	x.append(bi+paso)
	bi=bi+paso

for i in x:
	y.append(fun(i))

#Ciclo para llenar al vector y
plt.grid(True)#Cuadrícula en la gráfica
plt.plot(x,y)#Añade las variables y los marcadores a los ejes
plt.title("Gráfica Principal")#Añade el título encima de los ejes
plt.legend(['Polinomio cuadrado'])
plt.show()#Muestra la figura
