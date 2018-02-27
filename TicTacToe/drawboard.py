# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:56:31 2018
This will draw the board for tic tac toe
@author: Gary
"""

import pygame
import numpy

#Colors used
WHITE = (255,255,255)
BLACK = (0,0,0)

class DrawBoard:
    
    tiles = numpy.zeros((3,3), dtype=tuple)
    print(tiles)
    
    #constructor
    def __init__(self, surface):
        #coordinates for the size of the board
        self.x, self.y = 240,180 #starting position for our tiles array
        self.surface = surface
        #note: our tiles are 80x80 px
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                if y == 0: #if we are at positions (0,0), (1,0), (2,0) we need to start over at 240
                    self.x = 240
                self.tiles[x][y] = (self.x, self.y)
                #self.circle(self.tiles[x][y]) #draw each circle on the board for testing
                #self.ex(self.tiles[x][y])     #draw each ex on the board for testing
                if y == 2: #after we have gone through three columns we need to increment y to the next row
                    self.y += 80
                self.x += 80
        print(self.tiles)
        
#draw menu
    #def drawMenu(self):
        
#initial draw of the board
    def draw(self):
        pygame.draw.line(self.surface, WHITE, (200,220), (440,220)) #top line
        pygame.draw.line(self.surface, WHITE, (200,300), (440,300)) #bottom line
        pygame.draw.line(self.surface, WHITE, (280,140), (280,380)) #left line
        pygame.draw.line(self.surface, WHITE, (360,140), (360,380)) #right line
        pygame.display.flip()
        
#render text
    #def textRender(self, txt):

#update board
    #def update(self):
        
#draw circle
    def circle(self, pos, radius = 35, width = 2):
        pygame.draw.circle(self.surface, WHITE, pos, radius, width)
#draw x
    def ex(self, pos):
        x, y = pos
        pygame.draw.line(self.surface, WHITE, (x-25, y-25), (x+25, y+25), 2)
        pygame.draw.line(self.surface, WHITE, (x-25, y+25), (x+25, y-25), 2)