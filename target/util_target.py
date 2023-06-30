from random import randint

def randomize_cords(width, height, radius):
	x = randint(radius, width - radius)
	y = randint(radius, height - radius)
	return (x, y)

def randomize_size(width, height, radius):
	min_size = 20
	max_size = 30
	minimum = min(width, height)
	maximum = max(width, height)
	ratio = maximum / minimum
	left = int(min_size * ratio)
	right = int(max_size * ratio)
	return randint(left, right)