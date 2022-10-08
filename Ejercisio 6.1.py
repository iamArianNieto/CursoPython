class Vehiculo():

	def Color(self):
		pass

	def Ruedas(self):
		pass

	def Puertas(self):
		pass

class Coche(Vehiculo):
	def Velocidad(self):
		print("60km/h")

	def Cilindrada(self):
		print("4 Cilindros")

	def Color(self):
		print("Azul")

	def Ruedas(self):
		print("4 Ruedas")

	def Puertas(self):
		print("4 Puertas")


nuevo = Coche()
nuevo.Color()
nuevo.Ruedas()
nuevo.Color()
nuevo.Velocidad()
nuevo.Cilindrada()




		

