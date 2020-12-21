import pygame
import random

# pygame go brrr
pygame.init()

# graphics go brrrr
width = 640
height = 480
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("longboi TM")

# define colors
colors = {
	"snake_brain": (228, 255, 69),
	"snake_ass": (228, 200, 69),
	"food": (255, 0, 0)
}

# snake position with offsets
snake_pos = {
	"x": width/2-10,
	"y": height/2-10,
	"x_shift": 0,
	"y_shift": 0
}

# snake el size
snake_size = (10, 10)

# u dum? his speed below
snake_speed = 10

# snake body
snake_asss = []

snake_pos["x_shift"] = -snake_speed
for i in range(75):
	snake_asss.append([snake_pos["x"] + 10*i, snake_pos["y"]])

# food
food_pos = {
	"x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
	"y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
}

food_size = (10, 10)
food_eaten = 0

# start suffery
game_end = False
clock = pygame.time.Clock()

while not game_end:
	# game sansara wheel
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_end = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and snake_pos["x_shift"] == 0:
				# move left
				snake_pos["x_shift"] = -snake_speed
				snake_pos["y_shift"] = 0

			elif event.key == pygame.K_RIGHT and snake_pos["x_shift"] == 0:
				# move right
				snake_pos["x_shift"] = snake_speed
				snake_pos["y_shift"] = 0

			elif event.key == pygame.K_UP and snake_pos["y_shift"] == 0:
				# move up
				snake_pos["x_shift"] = 0
				snake_pos["y_shift"] = -snake_speed

			elif event.key == pygame.K_DOWN and snake_pos["y_shift"] == 0:
				# move down
				snake_pos["x_shift"] = 0
				snake_pos["y_shift"] = snake_speed

	# clear screen bc yes
	display.fill((0,0,0))

	# move snake humongous booty
	ltx = snake_pos["x"]
	lty = snake_pos["y"]

	for i,v in enumerate(snake_asss):
		_ltx = snake_asss[i][0]
		_lty = snake_asss[i][1]

		snake_asss[i][0] = ltx
		snake_asss[i][1] = lty

		ltx = _ltx
		lty = _lty

	# draw snake boddyyy++
	for t in snake_asss:
		pygame.draw.rect(display, colors["snake_ass"], [
			t[0],
			t[1],
			snake_size[0],
			snake_size[1]])

	# draw snake
	snake_pos["x"] += snake_pos["x_shift"]
	snake_pos["y"] += snake_pos["y_shift"]

	# tp snake like pacman
	if(snake_pos["x"] < -snake_size[0]):
		snake_pos["x"] = width

	elif(snake_pos["x"] > width):
		snake_pos["x"] = 0

	elif(snake_pos["y"] < -snake_size[1]):
		snake_pos["y"] = height

	elif(snake_pos["y"] > height):
		snake_pos["y"] = 0

	pygame.draw.rect(display, colors["snake_brain"], [
		snake_pos["x"],
		snake_pos["y"],
		snake_size[0],
		snake_size[1]])

	# make me food
	pygame.draw.rect(display, colors["food"], [
		food_pos["x"],
		food_pos["y"],
		food_size[0],
		food_size[1]])

	# ohh food found
	if(snake_pos["x"] == food_pos["x"]
		and snake_pos["y"] == food_pos["y"]):
		food_eaten += 1
		snake_asss.append([food_pos["x"], food_pos["y"]])

		food_pos = {
			"x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
			"y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
		}

	# when bump in ass
	for i,v in enumerate(snake_asss):
		if(snake_pos["x"]+snake_pos["x_shift"] == snake_asss[i][0]
			and snake_pos["y"]+snake_pos["y_shift"] == snake_asss[i][1]):
			snake_asss = snake_asss[:i]
			break

	pygame.display.update()
	
	# FPS
	clock.tick(30)
	

#rage quit
pygame.quit()
quit()