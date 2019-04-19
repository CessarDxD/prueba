# POO en python
#clase sencilla
class Coche():
	#Contructor / Estado inicial
	def __init__(self): 
		self.largoChasis=250
		self.anchoChasis=120
		self.__ruedas=4 # con 2 "_"antes de nombre objeto no permite modificar fuera de la clasa
		self.__enmarcha=False

	def arrancar(self,arrancamos):

		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			chequeo1=self.__chequeo()
		if self.__enmarcha and chequeo1:
			return "El coche esta en marcha"
		elif self.__enmarcha and chequeo1==False:
			return "Algo a ido mal en el chequeo"

		else:
			return "El coche no esta en marcha"
		self.__enmarcha=True

	def estado(self):
		print('El coche tiene: ',self.__ruedas,' ruedas, El coche tiene: ',self.anchoChasis,'cm de ancho, El coche tiene: ',self.largoChasis,'cm de largo')

	def __chequeo(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False
		

coche1=Coche()

print(coche1.arrancar(True))
coche1.estado()
print("-----------Segundo objeto--------------")
coche2=Coche()
print(coche2.arrancar(False))
coche2.ruedas=2
coche2.estado()

