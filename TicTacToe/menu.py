# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:47:46 2018
this holds the main menu for the tic tac toe game
@author: Gary
"""
import pygame

WHITE = (255,255,255)

class Menu:

    fontsize = 32
    
    def __init__(self, screen):
        self.screen = screen
        self.menuContainer = pygame.Rect(240, 10, 160, 150)
        self.width = 2 #width of our menu buttons
    
#initial draw of the menu
    def draw(self):
        self.textRender("Tic-Tac-Toe", (self.menuContainer.x+20,self.menuContainer.y+20), WHITE)
        pygame.draw.rect(self.screen, WHITE, self.button(270,100), self.width) #circles
        self.textRender("Circles", (285, 105), WHITE)
        pygame.draw.rect(self.screen, WHITE, self.button(270,150), self.width) #exes
        self.textRender("Exes", (300, 155), WHITE)
        pygame.draw.rect(self.screen, WHITE, self.button(270,200), self.width) #quit
        self.textRender("Quit", (300, 205), WHITE)
        pygame.display.flip()
        
#render text
    def textRender(self, text, pos, color):
        pygame.font.init()
        font = pygame.font.Font(None, self.fontsize)
        txt_surface = font.render(text, True, color)
        self.screen.blit(txt_surface, pos)
        pygame.display.flip()
        pygame.font.quit()
        
    def button(self, left, top):
        return pygame.Rect(left, top, 105, self.fontsize)
    
    def __del__ (self):
        print("menu died")

