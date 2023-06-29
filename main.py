import pygame
import target

WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 240, 0)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

pygame.font.init()
font = pygame.font.SysFont("Consolas", 23)

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

t = target.Target(WIDTH // 2, HEIGHT // 2, RED, 50)

def draw_crosshair():
	lenght = 20
	x, y = mouse_pos
	pygame.draw.line(window, GREEN, (x - lenght, y), (x + lenght, y), 3)
	pygame.draw.line(window, GREEN, (x, y - lenght), (x, lenght + y), 3)
	pygame.draw.line(window, BLACK, (x - lenght, y), (x + lenght, y), 1)
	pygame.draw.line(window, BLACK, (x, y - lenght), (x, lenght + y), 1)


def display_text(score, seconds):
	txt_score = font.render(f"score : {score}", True, (0, 0, 0))
	txt_seconds = font.render(f"seconds : {seconds}", True, (0, 0, 0))

	gap = 5
	window.blit(txt_score, (gap, gap))
	window.blit(txt_seconds, (gap, gap + txt_score.get_height())) 

def draw():
	if menu:
		txt = font.render("Press any key to play", True, (0, 0, 0))
		window.fill(WHITE)
		window.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2 - txt.get_height() // 2))

	else:
		window.fill(WHITE)
		t.draw(window)
		draw_crosshair()
		display_text(score, int(seconds))
	pygame.display.update()


def game_over():
	global seconds, score, menu
	if seconds > max_seconds:
		txt = font.render("Game Over!", True, (0, 0, 0))
		txt_score = font.render(f"Your score is {score}", True, (0, 0, 0))
		window.fill(WHITE)
		window.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2 - txt.get_height() // 2))
		window.blit(txt_score, (WIDTH // 2 - txt_score.get_width() // 2, HEIGHT // 2 + txt.get_height() // 2))
		pygame.display.update()
		pygame.time.wait(1500)
		t.x, t.y = WIDTH // 2, HEIGHT // 2
		seconds = 0
		score = 0
		menu = True


clock = pygame.time.Clock()
seconds = 0
max_seconds = 10
score = 0
FPS = 60
run = True
menu = True
while run:
	clock.tick(FPS)

	if not menu:
		seconds += 1 / FPS
	mouse_pos = pygame.mouse.get_pos()


	draw()
	

	game_over()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if t.is_target_killed(mouse_pos[0], mouse_pos[1], event):
			t.x, t.y = target.util_target.randomize_cords(WIDTH, HEIGHT, t.radius)
			score += 1

		if menu and (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN):
			menu = False


	#print(int(seconds))
pygame.quit()
