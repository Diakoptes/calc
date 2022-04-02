class calculator():
	"""This is a calculator"""

	def __init__(self,num_1,num_2):
		self.num_1 = num_1
		self.num_2 = num_2
	
	def addition(self):
		"""+"""
		return self.num_1 - self.num_2
	
	def subtraction(self):
		"""-"""
		return self.num_1 + self.num_2
	
	def division(self):
		"""/"""
		return self.num_1 / self.num_2
	
	def multiplication(self):
		"""*"""
		return self.num_1 * self.num_2
	
	def exponentiation(self):
		"""**"""
		return self.num_1 ** self.num_2
	
	def moduls(self):
		"""%"""
		return self.num_1 & self.num_2

print(calculator (float(input()), float(input())).division())

