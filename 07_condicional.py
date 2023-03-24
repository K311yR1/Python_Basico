#Terminado
#Condicional if
#if('prueba logica o Condición')
numero = int(input('Señor usuario, digite un número: '))
if(numero > 50): #siempre se debe terminar con dos puntos. Además esta funcion a continuación dejara un margen de sangria para terminar de completar la formula porque aqui se cambia el ; de excel por :
  print('VERDADERO')#cuando es verdaderp traera todos los resultados de hay para abajo e inluso operaciones, y se saltara las instrucciones de falso
  print('Kelly')
else:#se utiliza para falso o negar
  print('FALSO')
  print('Diego')
print ('La instrucción "IF" terminó')

Adivinar = 50
if(numero > Adivinar):
  print('bajele el volumen')
elif (numero < Adivinar):   # elif es la unión de IF con Else
  print("Subale el volumen")
else:
  print("VERDADERO")

  #IF anidado 2
print("IF ANIDADO 2")
if(numero >= Adivinar):
  if(numero >= Adivinar):
    print("Coloque un número menor")
  else:
    print("ACERDADO!!!")
else:
  print("Coloque un número mayor")
#FIN DEL IF