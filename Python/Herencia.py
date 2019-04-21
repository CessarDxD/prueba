#clase Herencia

class vehiculos():

	def __init__(self,marca1,modelo1):
		self.marca=marca1
		self.modelo=modelo1
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frenar=True
	def estado(self):
		print("Marca: ",self.marca, 
			"\nModelo: ",self.modelo,
			"\nEnmarcha: ",self.enmarcha,
			"\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena)
class furgoneta(vehiculos):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return 'La furgoneta esta cargada'
		else:
			return 'la furgoneta no esta cargada'



class moto(vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="voy haciendo el caballito"
	def estado(self):
		print("Marca: ",self.marca, 
			"\nModelo: ",self.modelo,
			"\nEnmarcha: ",self.enmarcha,
			"\nAcelerando: ",self.acelera,
			"\nFrenando: ",self.frena,
			"\n",self.hcaballito)

class vElectricos(vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100
	

	def cargarEnergia(self):
		self.cargando=True

	




moto1=moto("Honda","CBR")

#moto1.caballito()

moto1.estado()

furgoneta1=furgoneta('Renault','Kangoo')
furgoneta1.arrancar()
furgoneta1.estado()
print(furgoneta1.carga(True))

class biciElectrica(vElectricos,vehiculos,):
	pass

biciEle=biciElectrica("Orbea","Thj")

biciEle.estado()
