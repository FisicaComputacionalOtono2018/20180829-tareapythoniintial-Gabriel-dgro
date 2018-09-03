
# coding: utf-8

# In[1]:


#Autor: Gabriel Reyes
#Programa para calcular el producto punto entre dos vectores en 3 dimenciones

import math

va1=input('Inserte la componente x del primer vector: ')
va2=input('Inserte la componente y del primer vector: ')
va3=input('Inserte la componente z del primer vector: ')
vax=float(va1)
vay=float(va2)
vaz=float(va3)

vb1=input('Inserte la componente x del segundo vector: ')
vb2=input('Inserte la componente y del segundo vector: ')
vb3=input('Inserte la componente z del segundo vector: ')
vbx=float(vb1)
vby=float(vb2)
vbz=float(vb3)

productopunto=(float(vax*vbx)+float(vay*vby)+float(vaz*vbz))
print=('Producto:',productopunto)

