#Generadores

# def pares(limite):
# 	num=1
# 	lista=[]
# 	while num<limite:
# 		lista.append(num*2)
# 		num+=1

# 	return lista

# print(pares(10))

# generador

# def genearadorPares(limite):
# 	num=1

# 	while num<limite:
# 		yield num*2
# 		num+=1
# devuelvePares=genearadorPares(10)
# # for i in devuelvePares:
# # 	print(i)
# print(next(devuelvePares))

# print(next(devuelvePares))

# print(next(devuelvePares))

# def ciudades(*ciudades):
# 	for elemento in ciudades:
# 		for SubElemento in elemento
# 			yield SubElemento

# totalCiudades=ciudades('madrid','barcelona','Valecia')

# print(next(totalCiudades))

# def devuelve_ciudades(*ciudades):
# 	for elemento in ciudades:
# 		for subElemento in elemento:
# 			yield  subelemento #yield from elemento

# ciudes_devueltas=devuelve_ciudades('CDMX','Chihuahua','Monterey')

# print(next(ciudes_devueltas))
# print(next(ciudes_devueltas))

