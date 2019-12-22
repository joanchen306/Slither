import pygame
def getScore(score):
	return("SCORE: " + str(score))


def addScore(score):
	score = score + 20
	return score
	
def getSpeed():
	return 15

def check_key_pressed(event, block):
	direction = ""
	xchange = 0
	ychange = 0
	if event.key == pygame.K_LEFT or event.key == pygame.K_a:
		direction = "left"
		xchange = -block
		ychange = 0
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		direction = "right"
		xchange = block
		ychange = 0
	if event.key == pygame.K_UP or event.key == pygame.K_w:
		direction = "up"
		xchange = 0
		ychange = -block
	if event.key == pygame.K_DOWN or event.key == pygame.K_s:
		direction = "down"
		xchange = 0
		ychange = block
	return direction,xchange,ychange

