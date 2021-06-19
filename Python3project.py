import pygame 
import random
import time
pygame.init()

clock = pygame.time.Clock()

screen_width = 576
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

white = (255,255,255)
red = (255, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = player_img
        self.image.fill(white)

        self.rect = self.image.get_rect(center = (screen_width - 430, screen_height/2))

        self.x_speed = 0
        self.y_speed = 0
    
    def update(self):
        self.x_speed = 0
        self.y_speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
          self.y_speed -= 5
        elif keystate[pygame.K_DOWN]:
          self.y_speed += 5

        self.rect.x += self.x_speed 
        self.rect.y += self.y_speed

class Rectangle:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))



# floor_surface = pygame.image.load(".\\sprites\\floor-base.png").convert()
# floor_surface = pygame.transform.scale2x(floor_surface)
# floor_x_pos = 0

pipe_surface = pygame.image.load("D:\Python 3\python 3 project\sprites\pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)

player_img = pygame.image.load("D:\Python 3\python 3 project\sprites\luebird-midflap.png")

pipe_list = [] 

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)
pipe_height = [400,500,600,700]


# def draw_floor():
# 	screen.blit(floor_surface,(floor_x_pos,900))
# 	screen.blit(floor_surface,(floor_x_pos + 576,900))

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 150))
	return bottom_pipe,top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 1000:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe, pipe)

def remove_pipes(pipes):
	for pipe in pipes:
		if pipe.centerx == -100:
			pipes.remove(pipe)
	return pipes



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)







#game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    screen.fill((0,0,0))
    all_sprites.update() 
    all_sprites.draw(screen)

    pipe_list = move_pipes(pipe_list)
    pipe_list = remove_pipes(pipe_list)
    draw_pipes(pipe_list)

    # floor_x_pos -= 1
    # draw_floor()
    # if floor_x_pos <= -576:
	#     floor_x_pos = 0
       
    # white_rect.draw()
    # white_rect2.draw()
    
    # xcor += 1
    # xcor2 += 1

    # print (height, height2)
    
    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

