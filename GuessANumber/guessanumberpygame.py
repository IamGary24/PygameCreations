# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:00:33 2018
Guess A Number using Pygame
@author: Gary
"""

import pygame

WHITE = (255,2555,255)
BLACK = (0,0,0)

pygame.init()

size = (640,400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Guess A Number")

done = False

clock = pygame.time.Clock()

# -- Main Program Loop --
while not done:
    #-- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #-- Game Logic
    
    #-- Drawing Code
    screen.fill(WHITE)
    
    pygame.display.flip()
    
    #60 fps
    clock.tick(60)
    
pygame.quit()

