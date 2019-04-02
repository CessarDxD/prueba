#print('Hellow world')

# codigo sencillo intrucir un numero e imprimirlo
# x=(int(input('Introdusca un numero entero')))
# print(x)

#Validacion sencilla
# N=(input('Ingresa el nombre: "cesar" '))
# C=(input('Ingresa la contrase;a "123"'))

# if N=='cesar':
# 	if C=="123":
# 		print('Usted introducio conrectamente los datos')
# 	else:
# 		print('contrase;a incorrecta')
# else:
# 	print('el nombre es incorrecto')

#Agregar cosas a una lista //manejo de list
#print(dir([1,2,3])) #codigo para ver metodo con list

# a=[] #codigo para ingresa un entero dentro de un list
# x=(int(input('Ingresa un numero: ')))

# a.insert(0,x)
# print(a)

#ingresar datos a una list mediante un ciclo for
a=[]
c=(int(input('ingres cantidad de datos: ')))
contador=0
for x in range(c):
	r=int(input('ingres un dato:'))
	a.insert(contador,r)
	contador=contador+1

print(a)


