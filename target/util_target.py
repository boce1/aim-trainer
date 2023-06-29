from random import randint

def randomize_cords(width, height, radius):
	x = randint(radius, width - radius)
	y = randint(radius, height - radius)
	return (x, y)