
# coding: utf-8

# In[3]:


#Autor: Gabriel Reyes
#programa que imprime el número mayor dado 4 numeros

x=input('Primer numero: ')
y=input('Segundo numero: ')
z=input('Tercer numero: ')
xx=input('Cuarto numero: ')

if x>y:
    if x>z:
        if x>xx:
            print('El numero mayor es: ',x)
if y>x:
    if y>z:
        if y>xx:
            print('El numero mayor es: ',y)         
if z>y:
    if z>x:
        if z>xx:
            print('El numero mayor es: ',z)
if xx>y:
    if xx>z:
        if xx>x:
            print('El numero mayor es: ',xx)

