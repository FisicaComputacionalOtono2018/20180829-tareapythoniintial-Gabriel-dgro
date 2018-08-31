#Autor: Gabriel Reyes
#Fecha: 29/08/2018
#Prgorama que calcula el angulo entre 2 vectores

import math

vax=input('Inserte la componente x del primer vector: ')
vay=input('Inserte la componente y del primer vector: ')
vaz=input('Inserte la componente z del primer vector: ')

vbx=input('Inserte la componente x del segundo vector: ')
vby=input('Inserte la componente y del segundo vector: ')
vbz=input('Inserte la componente z del segundo vector: ')

magnitudva=math.sqrt((vax**2)+(vay**2)+(vaz**2))
#magnitudva=math.sqrt(math.pow(vax,2)+math.pow(vay,2)+math.pow(vaz,2))
magnitudvb=math.sqrt((vbx**2)+(vby**2)+(vbz**2))

pmagnitudes=(magnitudva*magnitudvb)
producto=float((vax*vbx)+(vay*vby)+(vaz*vbz))

angulo=float(math.acos((producto / pmagnitudes)))
angulo2=float(math.degrees(angulo))
print('Angulo: ',angulo2)
