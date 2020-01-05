class Rectangle:
	def __init__(self, height = 1, width = 2):
		self.height = height
		self.width = width
		
	def getArea(self):
		return self.height* self.width
		
	
	def getPerimeter(self):
		return self.height * self.width*2
		
a = Rectangle(int(input('enter the height here: ')), int(input('enter the width here: ')))

print("The Area of the rectangle is", a.getArea())
print("The Perimeter of the rectangle is", a.getPerimeter())