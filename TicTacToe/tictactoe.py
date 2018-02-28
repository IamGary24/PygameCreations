# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:55:28 2018
The main controller for the tic tac toe game
@author: Gary
"""
import pygame
import drawboard
import menu
import computer
import numpy
    
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
    
    #screen and containers
    size = (640,400)
    screen = pygame.display.set_mode(size)
    
    #necessary pygame variables
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tic-Tac-Toe")

    #-- initial menu draw --
    gameMenu = menu.Menu(screen)
    gameMenu.draw()

    #-- MENU --
    doneInMenu = False
    donePlaying = False
    circlesContainer = pygame.Rect(270, 100, 105, gameMenu.fontsize)
    exesContainer = pygame.Rect(270, 150, 105, gameMenu.fontsize)
    quitContainer = pygame.Rect(270, 200, 105, gameMenu.fontsize)
    menuContainer = pygame.Rect(250, 90, 200, 200)
    while not doneInMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneInMenu, donePlaying = True, True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitContainer.collidepoint(event.pos):
                    screen.fill(WHITE, quitContainer)
                    gameMenu.textRender("Quit", (300, 205), BLACK)
                    doneInMenu, donePlaying = True, True
                if circlesContainer.collidepoint(event.pos):
                    screen.fill(WHITE, circlesContainer)
                    humanToken = "circles"
                    computerToken = "exes"
                    gameMenu.textRender("Circles", (285, 105), BLACK)
                    doneInMenu = True
                    pygame.time.wait(1000) #in ms
                if exesContainer.collidepoint(event.pos):
                    screen.fill(WHITE, exesContainer)
                    humanToken = "exes"
                    computerToken = "circles"
                    gameMenu.textRender("Exes", (300, 155), BLACK)
                    doneInMenu = True
                    pygame.time.wait(1000) #in ms
        screen.fill(BLACK, menuContainer)

    #-- initial board draw --
    gameBoard = drawboard.DrawBoard(screen)
    gameBoard.draw()

    #-- use the initialized gameboard to provide containers
    boardContainers = numpy.zeros((3,3), dtype=pygame.Rect)
    print("board containers: ", boardContainers)
    rectWallSize = 40 #our tiles are 80x80 and we have the pos for the center 
    #initialize our array holding the containers for the board
    for i in range(len(gameBoard.tiles)):
        for j in range(len(gameBoard.tiles[i])):
            x,y = gameBoard.tiles[i][j]            #left wall,      top,         right wall,     bottom
            boardContainers[i][j] = pygame.Rect(x-rectWallSize, y-rectWallSize, x+rectWallSize, y+rectWallSize)      
    print("new board containers: ", boardContainers)

    #-- initialize our AI --
    theComputerPlayer = computer.Computer(computerToken)
    
    #-- GAME --
    #exes go first
    if humanToken == "exes":
        playerTurn = True
    else:
        playerTurn = False
    while not donePlaying:
        
        if playerTurn:
            player = "human"
        else:
            player = "computer"
        
        update = False #whether or not the board updates
        
        if player == "computer":
            print(player, computerToken, gameBoard.victoryTiles)
            gameBoard.victoryTiles, boardContainerIndex = theComputerPlayer.turn(gameBoard.victoryTiles)
            print("index to play", boardContainerIndex)
            i,j = boardContainerIndex
            gameBoard.update(boardContainers[i][j], computerToken)
            gameBoard.victoryTracker(boardContainerIndex, player, computerToken)
            playerTurn = True
        
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
                            update = True
                if update:
                    gameBoard.update(activeContainer, humanToken)
                    gameBoard.victoryTracker(coords,player,humanToken)
                    playerTurn = False
                
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()