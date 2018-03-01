# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:56:31 2018
This will draw the board for tic tac toe
@author: Gary
"""

import pygame
import numpy
import menu

#Colors used
WHITE = (255,255,255)
BLACK = (0,0,0)

class DrawBoard:
    
    fontsize = 32
    tiles = numpy.zeros((3,3), dtype=tuple)
    victoryTiles = None
    victory = False
    
    #constructor
    def __init__(self, surface):
        #coordinates for the size of the board
        self.x, self.y = 240,180 #starting position for our tiles array
        self.surface = surface
        self.player = "default"
        self.victoryTiles = numpy.array([['d','n','f'],['g','h','j'],['u','i','o']])
        #note: our tiles are 80x80 px
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                if y == 0: #if we are at positions (0,0), (1,0), (2,0) we need to start over at 240
                    self.x = 240
                self.tiles[x][y] = (self.x, self.y)
                if y == 2: #after we have gone through three columns we need to increment y to the next row
                    self.y += 80
                self.x += 80
        
#draw menu
    #def drawMenu(self):
        
#initial draw of the board
    def draw(self):
        pygame.draw.line(self.surface, WHITE, (200,220), (440,220)) #top line
        pygame.draw.line(self.surface, WHITE, (200,300), (440,300)) #bottom line
        pygame.draw.line(self.surface, WHITE, (280,140), (280,380)) #left line
        pygame.draw.line(self.surface, WHITE, (360,140), (360,380)) #right line
        pygame.display.flip()

#update board
    #player is either circles or exes
    def update(self, rect, token):
        if token == "circles":
            self.circle(rect)
        elif token == "exes":
            self.ex(rect)
#draw circle
    def circle(self, rect, radius = 35, width = 2):
        pygame.draw.circle(self.surface, WHITE, (rect.left+40,rect.top+40), radius, width)
        pygame.display.flip()
#draw x
    def ex(self, rect):
        pygame.draw.line(self.surface, WHITE, (rect.x+5, rect.y+5), (rect.x+75, rect.y+75), 2)
        pygame.draw.line(self.surface, WHITE, (rect.x+5, rect.y+75), (rect.x+75, rect.y+5), 2)
        pygame.display.flip()
        
    def victoryTracker(self, index, player, token):
        #our 3,3 array looks like a tictactoe board
        #first the index location gets the token: 'circle' or 'ex'
        i,j = index
        self.victoryTiles[i][j] = token
        self.player = player
        print("victory tiles: ",self.victoryTiles,"victory: ", self.victory)
        #now we want to track victory or if there are no more options
        #first we will see if anyone won
        if ((self.victoryTiles[0][0] == self.victoryTiles[0][1] and self.victoryTiles[0][1] == self.victoryTiles[0][2]) or
            (self.victoryTiles[1][0] == self.victoryTiles[1][1] and self.victoryTiles[1][1] == self.victoryTiles[1][2]) or
            (self.victoryTiles[2][0] == self.victoryTiles[2][1] and self.victoryTiles[2][1] == self.victoryTiles[2][2]) or
            (self.victoryTiles[0][0] == self.victoryTiles[1][0] and self.victoryTiles[1][0] == self.victoryTiles[2][0]) or
            (self.victoryTiles[0][1] == self.victoryTiles[1][1] and self.victoryTiles[1][1] == self.victoryTiles[2][1]) or
            (self.victoryTiles[0][2] == self.victoryTiles[1][2] and self.victoryTiles[1][2] == self.victoryTiles[2][2]) or
            (self.victoryTiles[0][0] == self.victoryTiles[1][1] and self.victoryTiles[1][1] == self.victoryTiles[2][2]) or
            (self.victoryTiles[2][0] == self.victoryTiles[1][1] and self.victoryTiles[1][1] == self.victoryTiles[0][2])):
                self.victory = True
        print(self.victory, ", ", player)
    
    def drawVictoryScreen(self):
        self.surface.fill(BLACK)
        victoryMenu = menu.Menu(self.surface)
        victoryMenu.textRender((self.player.title() + " wins!"), (250,105), WHITE)
        self.victory = False
        self.victoryTiles = None
        print(self.victoryTiles)
        self.player = "default"
        
    def __del__ (self):
        print("gameboard died")

        
        
        
        