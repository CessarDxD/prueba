#heren2
class persona():

	def __init__(self,nombre,edad,lugarDeRecidencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_Recidencia=lugarDeRecidencia
	def descripcion(self):
		print('Nombre:',self.nombre,' Edad: ',self.edad,' Lugar recidencia: ',self.lugar_Recidencia)

class empleado(persona):
	def __init__(self,salario1,antiguedad1,nombre_empleado,edad_empleado,residencia_empleado):
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		self.salario=salario1
		self.antiguedad=antiguedad1
	def descripcion(self):
		super().descripcion()
		print('salario: ',self.salario,'antiguedad:',self.antiguedad)


#persona1=persona('cesar',21,'micasa')

#Cesar=empleado(1500,5,"cesar",21,"micasa")
Cesar=persona('Cesar',21,'micasa')
Cesar.descripcion()

print(isinstance(Cesar,empleado))

