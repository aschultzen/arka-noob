import pygame
import time
from random import randint

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()

#Sizes
ball_radius = 10
paddle_size_x = 50
paddle_size_y = 5
frame_x = 1080
frame_y = 476

# Positions
ball_x = 1
ball_y = 1
paddle_x = (frame_x / 2) - (paddle_size_x/2)
paddle_y = frame_y - 20

# Direction
turn_x = 0
turn_y = 0

# Speeds
paddle_speed = 3

screen = pygame.display.set_mode((frame_x, frame_y))
done = False
color = (255, 255, 255);
BackGround = Background('telenor.jpg', [0,0])

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT]:
                paddle_x += paddle_speed

        # Crash detection
        # Reached the wall
        if (ball_x >= frame_x):
                turn_x = 1 
        # Reached the other wall
        if(ball_x <= 0):
                turn_x = 0

        # Reached the wall
        if (ball_y >= frame_y):
                turn_y = 1
        
        # Reached the other wall
        if(ball_y <= 0):
                turn_y = 0
        # Moving box
        if(turn_x == 1):
                ball_x -= 1
        else:
                ball_x += 1 

        if(turn_y == 1):
                ball_y -= 1
        else:
                ball_y += 1

        screen.blit(BackGround.image, BackGround.rect)
        pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius, 0)
        pygame.draw.rect(screen, color, (paddle_x, paddle_y, paddle_size_x, paddle_size_y))
        pygame.display.flip()