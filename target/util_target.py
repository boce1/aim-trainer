from random import randint

def randomize_cords(width, height, radius):
	x = randint(radius, width - radius)
	y = randint(radius, height - radius)
	return (x, y)

def randomize_size(width, height, radius):
	min_size = 0.5
	max_size = 2
	minimum = min(width, height)

	coef = minimum // 20
	left = int(min_size * coef)
	right = int(max_size * coef)

	return randint(left, right)