# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:00:33 2018
Guess A Number using Pygame
@author: Gary
"""

import pygame
import random
import textwrap

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTSKYBLUE = (135,206,250)
DEEPSKYBLUE = (0,191,255)
INDIANRED = (205,92,92)

def main():
    
    size = (640,400)
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    display_box = pygame.Rect(200,50, 240, 250)
    input_box = pygame.Rect(200,300,240,32)
    color_inactive = DEEPSKYBLUE
    color_active = LIGHTSKYBLUE
    color = color_inactive
    active = False
    text = ''
    done = False

    pygame.display.set_caption("Guess A Number")

    # -- Main Program Loop --
    while not done:
        #-- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #user clicked on the input box
                if input_box.collidepoint(event.pos):
                    #toggle the active variable.
                    active = not active
                else:
                    active = False
                #change the current color of the input box
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
                
        screen.fill((30,30,30))
        #Render the current text
        inputtxt_surface = font.render(text, True, color)
        displaytxt_surface = font.render("Welcome to Guess A Number!", True, WHITE)
        #Blit the text
        screen.blit(inputtxt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(displaytxt_surface, (display_box.x+5, display_box.y+5))
        #Blit the input box rect
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, INDIANRED, display_box, 2)
        
        pygame.display.flip()
        clock.tick(30)
    
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()

