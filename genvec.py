# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------------------------------
Script para generar un vector de números igualmente espaciados
entre dos valores reales de un intervalo: a y b. La utilidad de este
script se hace evidente a la hora de realizar una gráfica con la librería matplot.

Ejemplo:

--Entrada--
a=0; b=5; n=5

--Salida--
x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

Luis Javier Zuluaga Betancur - septiembre 26 de 2017
---------------------------------------------------------------------------------------
'''
import os#Importar la librería para I/O 
os.system('clear')#Limpiar la terminal
n=int(input('Número de puntos = '))#Número de puntos del vector sin contar el punto inicial
a=float(input('a = '))#Límite inferior del intervalo
b=float(input('b = '))#Límite superior del intervalo

x=[a]#Primer elemento del vector
y=[]
paso=(b-a)/n#Tamaño del incremento del vector x

bi=a #Acumulador para ir llenando el vector x

#Ciclo para llenar al vector x
while bi<b:
	x.append(bi+paso)
	bi=bi+paso
print(x)
