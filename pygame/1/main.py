background_image_filename = 'resources/background.png'
sprite_image_filename = 'resources/big.png'
 
import pygame
from pygame.locals import *
from sys import exit
from vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((480, 640), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()
destination = Vector2()
speed = 200
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    pressed_mouse = pygame.mouse.get_pressed()
    if pressed_mouse[2]:
        destination = Vector2( *pygame.mouse.get_pos() ) - Vector2( *sprite.get_size() )/2
        vector_to_mouse = Vector2.from_points(position, destination)
        vector_to_mouse.normalize()
        heading = (vector_to_mouse * speed)
    
    if destination.eq(position):
        heading = Vector2()
    screen.blit(background, (0,0))
    screen.blit(sprite, position)

    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0
    position += heading * time_passed_seconds
    pygame.display.update()