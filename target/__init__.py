import target.util_target 
import pygame
from math import sqrt

class Target:
	def __init__(self, x, y, color, radius):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
		pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius, 2)

	def is_target_killed(self, mouse_x, mouse_y, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			x_distance = abs(self.x - mouse_x)
			y_distance = abs(self.y - mouse_y)

			if sqrt(x_distance**2 + y_distance**2) <= self.radius:
				return True

		return False