
cadena="cesar heranandez"
#isdigit: Devuelve un boolean que dice si el valor es numerico=True
#isalum: 
#isalpha: Devuelve un boolean que dice si el valor es string=True

edad=input('introduce tu edad: ')

while(edad.isdigit()==False):
	print('introduce un valor numerico')
	edad=input('introduce tu edad: ')

if(int(edad)<18):
	print('no pasas crack')
else:
	print('puedes pasar crack')

print(edad.isdigit())