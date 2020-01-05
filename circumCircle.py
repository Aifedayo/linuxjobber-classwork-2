# Calculating the circumference of a Circle

from math import pi

def circumCircle(radius):
	result = radius * 2 * pi
	print(format(result, '.2f'))

circumCircle(int(input("Enter the radius of the circle: ")))