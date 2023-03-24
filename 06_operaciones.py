#***OPERACIONES ARITMETICAS***
#SUMA+, RESTA-, MULTI*, DIVI/, DIV ENtTERA //,
#RESIDUO O MODULO %, POTENCIA**
#Jerarquia de operaciones (), **, * /,+ -

number = int(input("Digite un número "))
print(f'La suma con 2 es: {number +2}')
print(f'La resta con 2 es: {number -2}')
print(f'La multiplicación con 2 es: {number *2}')
print(
  f'La división con 2 es: {number /2}'
)  #la división siempre entrga un dato de tipo flotante porque el resultado no siempre es entero
print(f'La división ENTERA con 2 es: {number //2}')
print(f'el residuo o modulo de la división es 2 es: {number %2}'
      )  #el residuo es lo que sobra de la división
print(f'La potencia con 2 es: {number **2}')

#***OPERACIONES DE ASIGNACION***
contador = 3
print(f'antes de (+=) es:{contador}')
contador = contador + 1  #sintansix para incrementar una variable entonces contador = 2
contador += 1  #(+= operacion de asignacion incrementar)
print(f'despues de (+=) es:{contador}')
contador = 9
print(f'antes de (-=)es: {contador}')
contador = contador - 1
contador -= 1  #(-= operacion de asignacion decremental)
print(f'despues de (-=)es: {contador}')

number += 1
print(f'al usar e operador incremental += resultado es {number}')
print(f'al usar e operador decremental -= resultado es {number}')
#multiplicación
number *= 2
print(f'al usar el operador multiplicación *= resultado es {number}')
number /= 2
print(f'al usar el operador división /= resultado es {number}')
number //= 2
print(f'al usar el operador división ENTERA //= resultado es {number}')
number %= 2
print(f'al usar el operador residuo %= resultado es {number}')
number **= 2
print(f'al usar el operador potenciación **= resultado es {number}')

#OPERACIONNES LÓGICAS


#OPERACIONES RELACIONALES O DE COMPARACIÓN
