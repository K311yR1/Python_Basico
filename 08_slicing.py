nombre = 'Cesar Quintero'
#***INDEXING***:
#Posición indice de la letra 'C' es cero
print(nombre[0])  #Trae el caracter que se le indique de la variable
print(nombre[4])

#SLICING: trae una fraccion de la variable
print(
  nombre[1:4]
)  #qioero que me traiga esa, pero en el ultimo valor se coloca un numeor de más
print(nombre[2:7])
print(nombre[7:12])
#Para imprimir letras intercaldas CsrQ
print(nombre[0:7:2])  #el 2 indica que va a ir saldando de 2 en
print(nombre[7::2])
#para imprimir toda la variable
print(nombre[7:])

#REGRESIVO
print("Regresivo")
print(nombre[-14:-1])
print(nombre[-1:-9:-1]) #para escribir el nombre al reves
print(nombre[-1::-1])