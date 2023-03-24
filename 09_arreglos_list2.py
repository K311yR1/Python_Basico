num = [99, 34, 25, 56, 72]
print(num)
#modificar la lista
num[1] = 88
print(num)
num[2:3] = 22, 54
print(num)

#FUNCION INSERT
print('Función Insert')
num.insert(
  1, 77
)  # el uno indica que celda quiero cambiar y el 77 por el que lo voy a cambiar
print(num)

#FUNCIÓN APPEND
print('Función Append')
num.append(100)  # permite agrgar un dato a la lista
print(num)

#FUNCIÓN Extend
print('Función Extend')  #permite unir dos listas
list1 = ["Kelly", "Rincon"]
list2 = ["Liam", "Marín"]
list1.extend(list2)
print(list1)

#FUNCION REMOVE
print('Función Removed')  #permite eliminar elementos de una lista
list1.remove("Rincon")
print(list1)

#FUNCION POP
print(
  'Función Pop'
)  #Permite eliminar elemtos de una lista indicandole el carcter que corresponde
list1.pop(2)
print(list1)

#FUNCION DEL
print('Función Del')  #Permite eliminar el primer elemto de la lista
del list1[0]
print(list1)

#FUNCION CLEAR
print('Función Clear')  #Elimina todos los elemtos de la lista
list2.clear()
print(list2)
