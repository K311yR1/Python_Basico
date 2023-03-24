number = int(input('Digite un número '))
#*** OPERACIONES RELACIONALES O DE COMPARACIÓN***
print (number > 3) #pregunta si number es mayor que 3
print (number >= 3)#pregunta si number es mayor o igual que 3
print (number < 3)#pregunta si number es menor que 3
print (number >= 3)#pregunta si number es menor o igual que 3
print (number == 3)#pregunta si number es igual que 3
print (number != 3)#pregunta si number no es menor o igual que 3


print("OPERACIONES LÓGICAS")
#Solo entregan dos resultados de true (1) / false (0)
#*Operaciones basicas:
#(AND , &) Conjunción 
#(OR, |) Distunción
#(not, ~) Negación
#(^) Or exclusiva

print("AND , &) Conjunción")
#Valor 1 And Valor 2
print(True and True)
print(number>=3) and True
print(number>=3) and False
print(False and False)
print(number>=3 and False)
print(False and True and True)
print(number>=3 and False and True)
print(True & True)

print("(OR, |) Disyunción")
print(False or False)
print(False or True)
print(True or True)
print(False or True or False)
print(number >3 or True)
print(number >3 or number <10) #si number es mayor a 3 o menor que 10
print(number <= 3 | number >=10)

print("(not, ~) Negación")
print(not(True)) #arroja cual es la negacion de verdadero
print(not (False)) #arroja cual es la negacion de falso

print("(^) Or exclusiva")#El resultado sera falso cuando los dos valores son iguales y verdadero cuando los dos valores son diferentes.
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

#***OPERACIONES DE PERTENENCIA***
# operador in (si un valor se encuentra dentro de una variable)
print('OPERADORES DE PERTENENCIA (IN)')
nombre= 'Cesar Quintero'
print('Q' in nombre) #Si Q se encuentra en la varibale nombre
print('Z' in nombre)
#***Funcion len (permite contar los caracteres de una variable incluyendo los espacios)
print("función len")
print(len(nombre))
print('uso de loa métodos "upper","lowe", "tittle"')
#Un método es igual a una funcion
print(nombre.upper())#Pasa todos los caracteres de esa variable a mayusculas
print(nombre.lower())#pasa todos los caracteres a minuscula
print(nombre.title())#deja el primer caracter de una variable en mayuscula como nombre propio

#FUNCION DE CONTEO
print('Uso del metodo de conteo "count"')
print(nombre.count('e'))#cuenta cuantos caracteres voy a tener en una variable