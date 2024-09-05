
'''
-----------------------------------------
Comentado la secuencias de If/ Elif/ Else
-----------------------------------------
x= int(input('Please enter an integer'))

if x<0:
    x=0
    print('Negative chage to zero')

elif x==0:
    print('Zero')

elif x==1:
    print('Single')

else: print('More')

'''
nombre= str(input('Ingrese su nombre'))
print ('Usted se llama ' + nombre +' ?'+ 'Si su nombre es Correcto Ingrese (si), de lo contrario (no)')
respuesta=str(input())
if respuesta=='si':
    print('Bienvenido '+ nombre)

else: nombre= str(input('Ingrese su nombre'))
print ('Bienvenido '+ nombre)

