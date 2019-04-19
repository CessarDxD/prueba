#Excepciones 
# def suma(num1,num2):
# 	return num1+num2
# def resta(num1,num2):
# 	return num1-num2
# def divi(num1,num2):
# 	try:
# 		return num1/num2

# 	except ZeroDivisionError:
# 		print('Error de divicion sobre 0')
# 		return 'operacion erronea'
# def multi(num1,num2):
# 	 return num1*num2
# while True:
# 	try:
# 		numero1=(int(input('Ingresa un numero 1  ')))
# 		numero2=(int(input('Ingresa un numero 2  ')))
# 		break;
# 	except ValueError:
# 		print('Los valores introducidos no son correctos intenta de nuevo')


# op=input('Ingresa la operacion a realizar ')

# if op=='suma':
# 	print(suma(numero1,numero2))
# elif op=='resta':
# 	print(resta(numero1,numero2))
# elif op=='division':
# 	print(divi(numero1,numero2))
# elif op=='multiplicacion':
# 	print(multi(numero1,numero2))
# else:
# 	print('operecion no contemplada')

# print('fin del programa')

# def divide():
# 	try:
# 		num1=float(input('Ingresa el primer valor '))
# 		num2=float(input('Ingresa el segundo valor '))

# 		print(f'La division es: {num1/num2}')
# 	except ValueError:
# 		print('Valor no aceptado')
# 	except ZeroDivisionError:
# 		print('Error, no se puede dividir entre cero')
# 	finally:
# 		print('operacion realizada')

# divide()

# def evaluaEdad(edad):
# 	if edad<0:
# 		raise TypeError("No puedes tener una edad negativa")
# 	if edad<20:
# 		return('Eres muy joven')
# 	elif edad<40:
# 		return('Eres joven')
# 	elif edad<60:
# 		return('Eres maduro')
# 	elif edad<100:
# 		return('Cuidate')

# print(evaluaEdad(-1))

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError('El numero no puede ser negativo')
	else:
		return math.sqrt(num1)

op1=(int(input('Ingresa un numero  ')))
try:
	print(calculaRaiz(op1))
except ValueError as ErrorRaizNegativa:
	print(ErrorRaizNegativa)

print('Fin del programa')