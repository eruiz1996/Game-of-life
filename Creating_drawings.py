import pygame
import sys

pygame.init()
WIDTH, HEIGHT = (500, 500)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Creating rectangles')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(BLACK)
	# SYNTAX: pygame.Rect(left, top, width, height)
	cell = pygame.Rect(250, 200, 100, 50)
	# SYNTAX: pygame.draw.rect(surface, color, rect, width=0)
	pygame.draw.rect(surface, WHITE, cell)
	#pygame.draw.rect(surface, WHITE, (0, 0, 0, 0))
	pygame.display.update()