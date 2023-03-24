#TIPOS DE ARREGLOS (se toman valores en conjunto)
#list, se utiliza el separador []
#tuple ()
#dict {}
#set {}

#List (puede agrupar datos str, int, float, bool)
primera_lista =["Manzana", "banano"]
print(primera_lista)
nombres =["Cesar", "Octavio","Luisa"]
print(nombres)

lista1 = [2, 4, 89, 100, 3.14]
print(lista1)
lista2 = ['a', 123, 'A', 3.1416, 'palabra', True, 1000]
print(lista2)
#Tamaño de una lista (len)
print('Tamaño Lista:')
print(len(lista1))
print(len(lista2))
#Tipo de dato lista:
print('TIPO DE DATO LISTA:')
print(type(lista1))
print(type(lista2))

#Otra lista.
print('Función list():')
num = [1, 2, 3, 4, 5]
print(num)
num2 = list((1, 2, 3, 4, 5))
print(num2)
num3 = list({1, 2, 3, 4, 5})
print(num3)
#Las listas permiten cambiar valores de datos, agregar, quitar, cambiar.

print("Index list: ")
print(num[0])
print(num[0:4])
print(num[-1::-1])
print("Uso de la función IN")
print(3 in num)
print(10 in num)
print(num is num2)
