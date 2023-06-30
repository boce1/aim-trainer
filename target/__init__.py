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
		pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius, 1)

	def is_mouse_inside(self, mouse_x, mouse_y):
		x_distance = abs(self.x - mouse_x)
		y_distance = abs(self.y - mouse_y)
		return sqrt(x_distance**2 + y_distance**2) <= self.radius

	def is_target_killed(self, mouse_x, mouse_y, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.is_mouse_inside(mouse_x, mouse_y):
				return True

		return False

	def is_target_missed(self, mouse_x, mouse_y, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if not self.is_mouse_inside(mouse_x, mouse_y):
				return True
		return False