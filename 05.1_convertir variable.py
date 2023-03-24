# convertir la variable var en un numero
var = input("señor usuario digite un numero: ")
print("usted acaba de digitar lo siguiente", var)
var = float(var)
print(var + 2) #decimal

numero = input("señor usuario digite un numero: ")
numero = int(numero)
#tambien se puede anidar las formulas asi:
numero = int(input("señor usuario digite un numero: "))

print(f'el numero que digitó fue: {numero}')
#convertir ahora a bool (verdadero/false)
numero = bool(input("señor usuario digite un numero: "))
print(f'el numero que digitó fue: {numero}')