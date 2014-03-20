#!usr/bin/python
#!encoding: UTF-8

import sys
import math

# def calcular_xi (n, i):
#xi = (i -1.0/2.0) / n               # Esta es una función que podemos emplear.
#return xi
def calcular_pi(n):
    PI35 = 3.1415926535897931159979634685441852    #Muestra el valor real de la constante pi.
    sumatorio = 0.0
    ini = 0
    intervalos = 1.0 / float (n)
    for i in range (n):
       x_i = ((i+1) - 1.0/2.0) / n  # Aquí se puede utilizar la funcion def que hemos puesto antes.
       fx_i = 4.0 / (1+x_i * x_i)
       ini += intervalos
       sumatorio += fx_i
    valor_pi = sumatorio / n
    return (valor_pi)

argumentos = sys.argv[1:]

if (len(argumentos) == 2):           #Si la lista tiene un elemento se ejecuta el if, en caso contrario te lo pide por pantalla.
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
else:
    print"Introduzca el nº de intervalos (n>0): "
    n = int (raw_input());
    print "Introduzca el numero de aproximaciones: "
    aproximaciones = int (raw_input());
    
if (n>0): 
    PI35DT = PI35 = 3.1415926535897931159979634685441852
    intervalo = n
    lista = []
    for i in range (aproximaciones):
      valor = calcular_pi (intervalo)
      lista.append (valor)
      intervalo += n
    print lista
    diferencia = []
    for i in range (aproximaciones):
      dif = abs(PI35DT - lista[i])
      diferencia.append (dif)
    print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
    for i in range (aproximaciones):
      print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista[i],diferencia[i])
else:
    print "El valor de los intervalos debe ser mayor que 0"