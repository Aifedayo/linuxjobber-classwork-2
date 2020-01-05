class Fan:
	
	def __init__(self, slow= 1, medium = 2, fast = 3,speed = "slow", radius = 5, color = "blue", on = False):
		self.__slow = slow
		self.__medium = medium
		self.__fast = fast
		self.__speed = speed
		self.__radius = radius
		self.__color = color
		self.__on = on
		
	#Accessor Methods
	
	def get_speed(self):
		return self.__speed
		
	def get_on(self):
		return self.__on
		
	def get_radius(self):
		return self.__radius
		
	def get_color(self):
		return self.__color
	
	#Mutator Methods
	
	def set_speed(self, speed):
		self.__speed = speed
	
	def set_on(self, on):
		self.__on = on
	
	def set_radius(self, radius):
		self.__radius = radius
		
	def set_color(self, color):
		self.__color = color	

a = Fan()
print(a)