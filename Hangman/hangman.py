# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:33:28 2018

@author: Gary
"""

import worddatabase
import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)
DEEPSKYBLUE = (0,191,255)
INDIANRED = (205,92,92)

def main():
    
    #fonts and text
    fontsize = 32
    font = pygame.font.Font(None, fontsize)
    color_active = DEEPSKYBLUE
    color_inactive = INDIANRED
    choiceColor = color_inactive
    choiceText = ' '
    
    #screen and containers
    size = (640,400)
    screen = pygame.display.set_mode(size)
    boardContainer = pygame.Rect(240, 10, 160, 150)
    choiceContainer = pygame.Rect(100, 360, 440, fontsize) 
    
    clock = pygame.time.Clock()
    done = False
    active = False
    wordToGuess = " "
    countIncorrect = 0      #store number of incorrects
    countGuess = 0          #store total guesses
    possibleGuess = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    currentGuess = None     #track the current guess from user
    pygame.display.set_caption("Hangman")
    
    #-- hold information for the topic menu and draw it
    def topicMenu():
        #display possible topics
        topic_text = "Choose a topic: Person, Place, Thing"
        drawTopicChoice(topic_text)
        #receive input
        
        #hold users choice
        #check choice against possible topics
        #when topic is legal, choose random word within topic
        #remove text from game
        
    #--- Draw Functions ---
    
    #draw board
    def drawBoard():
        pygame.draw.rect(screen, WHITE, boardContainer, 2)
        pygame.draw.rect(screen, choiceColor, choiceContainer, 2)
        pygame.draw.line(screen, WHITE, (290,50), (290,30))
        pygame.draw.line(screen, WHITE, (290,30), (350,30))
        pygame.draw.line(screen, WHITE, (350,30), (350,140))
        pygame.display.flip()
        
    #draw topic choice menu
    def drawTopicChoice(txt):
        #draw text below hangman board
        topictext_surface = font.render(txt, True, WHITE)
        screen.blit(topictext_surface, (100, 320))
        pygame.display.flip()
    
    #-- update the board with each incorrect guess
    #def updateBoard(x):
    
    #-- receive the topic choice and choose a random word
    def receiveTopicChoice(s):
        s = s.lower()
        if s == " person":
            newWord = worddatabase.Person()
        elif s == " place":
            newWord = worddatabase.Place()
        elif s == " thing":
            newWord = worddatabase.Thing()
            
        return newWord.random_word()
        
        
     
    #-- check the guess against the chosen word    
    #def guessCheck():
        
    #-- main game loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #user clicked on the choiceContainer
                if choiceContainer.collidepoint(event.pos):
                    #toggle the active variable.
                    active = not active
                else:
                    active = False
                #change choiceContainer color to indicate active
                choiceColor = color_active if active else color_inactive
            #read text from user
            if event.type == pygame.KEYDOWN:
                if active: #only if text box is selected
                    if event.key == pygame.K_RETURN:
                        print(choiceText)
                        wordToGuess = receiveTopicChoice(choiceText)
                        print(wordToGuess)
                        choiceText = ''
                    elif event.key == pygame.K_BACKSPACE:
                        choiceText = choiceText[:-1]
                    else:
                        choiceText += event.unicode
       
        clock.tick(30)
        
        #draw board or update board
        if countGuess == 0:
            topicMenu()
            drawBoard()
        #else updateBoard(countIncorrect)
             
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
        
    