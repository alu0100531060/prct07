#!usr/bin/python
#!encoding: UTF-8

import sys
import math

import modulo

#programa principal
tupla = (10, 20, 30, 40)
# el valor de la memoria es 1000000000   (mil millones, pero depende del hardware de la máquina)
#Se pueden proporcionar números en notación científica
# Cuando haces un python modulo.py en la consola  el ordenador coge el ejecutable de dentro del modulo y lo convierte a .pyc

lista = []
for i in tupla:
  valor_pi = modulo.calcular_pi (i)
  lista.append (valor_pi)
print lista  


pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT)
dif35 = []
for i in range (len(tupla)):
   dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i"
for i in range (len(tupla)):
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])
  
# esto seria para saber más
print "pasando la salida a una matriz..."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #
matriz = []
for i in range (len(tupla)):
  matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len(tupla)):
  print
  print matriz[i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #
  