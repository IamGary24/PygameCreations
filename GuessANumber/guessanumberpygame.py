# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:00:33 2018
Guess A Number using Pygame
@author: Gary
"""

import pygame
import random

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
    
    
    answer = None #the users guess
    GAMEGUESS = random.randint(-50,50)
    guess = " "
    
    def UserGuess(x):
        try:
            
            if x < GAMEGUESS:
                print("Too low")
                return "Too low: " + str(x)
            elif x > GAMEGUESS:
                print("Too high")
                return "Too high: " + str(x)
            elif x == GAMEGUESS:
                print("Correct!")
                return "Correct: " + str(x)
        except TypeError:
            print("Invalid Guess")
            pygame.quit()        
    
    info_text = ["Welcome to Guess", "A Number!","I am thinking of","a number between:","-50 and 50"]

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
                        answer = int(text)   #store the userguess
                        guess = UserGuess(answer)    #put this userguess through the function
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        screen.fill((30,30,30))
        
        #-- Render the text --
        
        #input text from user
        inputtxt_surface = font.render(text, True, color)
        #info text for game
        #the info text is too large for the window, this is toc reate new lines
        display = []
        for line in info_text:
            display.append(font.render(line, True, WHITE))
        # guess text
        guesstxt_surface = font.render(guess, True, WHITE)
       
        #--Blit the text --
        
        #input text from user
        screen.blit(inputtxt_surface, (input_box.x+5, input_box.y+5))
        #info text
        for line in range(len(display)):
            screen.blit(display[line],(display_box.x+5,display_box.y+5+(line*32)+(5*line)))
        #guess text
        screen.blit(guesstxt_surface, (display_box.x+5, display_box.y+200))
        
        #--Blit the input box rect--
        
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, INDIANRED, display_box, 2)
        
        pygame.display.flip()
        clock.tick(30)
    
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()

