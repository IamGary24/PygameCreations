# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:55:28 2018
The main controller for the tic tac toe game
@author: Gary
"""
import pygame
import drawboard


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
    boardContainers = gameBoard.tiles
    print("board containers: ", boardContainers)
    
    #-- MENU --
    doneInMenu = False
    while not doneInMenu:
        doneInMenu = True
    
    
    #-- GAME --
    donePlaying = False
    while not donePlaying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                donePlaying = True
            #if event.type == pygame.MOUSEBUTTONDOWN:
                
                
    
    
    
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()