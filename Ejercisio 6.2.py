class ALumnos():
	name= None
	number= None
 

	def __init__(self, name ,number):
		self.name       = name
		self.number   = number
		
     

	def resultado(self):
		if self.number>70:
			return "Aprovado"
		else:
			return "Reprobado"

	def salida(self):

		return "El alumno: " + self.name +" obtuvo "+ str(self.number) 
		




x=ALumnos("Pedro",85)
print(x.salida())
print(x.resultado())




		

