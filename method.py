from math import pi

class Circle:
	def __init__(self, radius, pi):
		self.ID = 2*radius*pi
		self.radius = radius
		self.pi = pi
	
a = Circle(int(input('Enter the radius here: ')),pi)
print(a.ID)