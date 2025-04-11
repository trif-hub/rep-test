import math

def area(a, b, c):
	p = (a+b+c)/2
	s = math.sqrt(p*(p-a)*(p-b)*(p-c))
	print ('площадь треугольника ', s)

area (10,5,6)