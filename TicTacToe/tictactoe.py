# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:55:28 2018
The main controller for the tic tac toe game
@author: Gary
"""
import pygame
import drawboard
import numpy
    

def main():

    
    #fonts and text
    fontsize = 32
    font = pygame.font.Font(None, fontsize)
    
    #screen and containers
    size = (640,400)
    screen = pygame.display.set_mode(size)
    
    #necessary pygame variables
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tic-Tac-Toe")


    #-- initial board draw --
    gameBoard = drawboard.DrawBoard(screen)
    gameBoard.draw()
    
    #-- use the initialized gameboard to provide containers
    boardContainers = numpy.zeros((3,3), dtype= pygame.Rect)
    print("board containers: ", boardContainers)
    rectWallSize = 40 #our tiles are 80x80 and we have the pos for the center 
    #initialize our array holding the containers for the board
    for i in range(len(gameBoard.tiles)):
        for j in range(len(gameBoard.tiles[i])):
            x,y = gameBoard.tiles[i][j]            #left wall,      top,         right wall,     bottom
            boardContainers[i][j] = pygame.Rect(x-rectWallSize, y-rectWallSize, x+rectWallSize, y+rectWallSize)      
    print("new board containers: ", boardContainers)
    
    #-- MENU --
    doneInMenu = False
    while not doneInMenu:
        doneInMenu = True
    
    
    #-- GAME --
    donePlaying = False
    player = "human"
    token = "circles"
    while not donePlaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #iterate through our boardcontainers and determine which container is active
                for i in range(len(boardContainers)):
                    for j in range(len(boardContainers[i])):
                        if boardContainers[i][j].collidepoint(event.pos):
                            activeContainer = boardContainers[i][j] #denote this container as the active one
                            coords = i,j
                gameBoard.update(activeContainer, token)
                gameBoard.victoryTracker(coords,player,token)
                
                
                
                
                
                
    
    
    
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()