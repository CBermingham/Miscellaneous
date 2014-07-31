class Calculator(object):

	def __init__(self, num1, num2):
		self.num1 = float(num1)
		self.num2 = float(num2)

	def add(self):
		result = self.num1 + self.num2
		print self.num1, " + ", self.num2, " = ", result

	def subtract(self):
		result = self.num1 - self.num2
		print self.num1, " - ", self.num2, " = ", result

	def multiply(self):
		result = self.num1 * self.num2
		print self.num1, " * ", self.num2, " = ", result

	def divide(self):
		result = self.num1 / self.num2
		print self.num1, " / ", self.num2, " = ", result

operation = Calculator(2, 4)
operation.add()
operation.subtract()
operation.multiply()
operation.divide()

