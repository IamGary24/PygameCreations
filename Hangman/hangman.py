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
    #x is the number of incorrects, s is the word once chosen
    def updateBoard(numInc, s):
        pygame.draw.rect(screen, WHITE, boardContainer, 2)
        pygame.draw.rect(screen, choiceColor, choiceContainer, 2)
        pygame.draw.line(screen, WHITE, (290,50), (290,30))
        pygame.draw.line(screen, WHITE, (290,30), (350,30))
        pygame.draw.line(screen, WHITE, (350,30), (350,140))
        
        wordLen = len(s)
        wordLineLength = 20
        wordLineY = 240
        wordLineX = 0
        
        #the wordLen is greater than two, therefore it must be a topic choice
        #update the board reflecting the word needed to be guessed
        if wordLen > 2:
            #draw lines equivalent to word size
            for x in range(1,wordLen+1):
                if s[x-1] == " ": 
                    #if this location in the string is whitespace
                    wordLineX += 40 #move our "line drawer" to skip the line being drawn
               
                #handle "word wrapping"
                elif x > 15:
                    wordLineY = 280
                    wordLineX = (x-14) * 40
                    pygame.draw.line(screen, WHITE, (wordLineX+(wordLineLength),wordLineY),(wordLineX+(wordLineLength+20), wordLineY))

                else:
                    wordLineX = (x * 40) - 20 #we want to move by 40 px each time, but start at 20
                    pygame.draw.line(screen, WHITE, (wordLineX,wordLineY),(wordLineX+(wordLineLength), wordLineY))
            
        #-- code for incorrect guesses --
        
        #there are only 6 guesses
        if numInc == 1:
            pygame.draw.circle(screen, WHITE, (291,55), 5, 2)
        elif numInc == 2:
            print(numInc)
        elif numInc == 3:
            print(numInc)
        elif numInc == 4:
            print(numInc)
        elif numInc == 5:
            print(numInc)
        elif numInc == 6:
            print(numInc)
            
        
        
        pygame.display.flip()
        
        
    #-- receive the topic choice and choose a random word
    def receiveTopicChoice(s):
        s = s.lower()
        #if our string is too small, exit the function and return the string
        if len(s) < 2:
            return s
        elif s == " person":
            newWord = worddatabase.Person()
        elif s == " place":
            newWord = worddatabase.Place()
        elif s == " thing":
            newWord = worddatabase.Thing()
            #random_word() randomly chooses a word from the topic choices
        
        #now that we have the topic and word, remove the menu
        screen.fill(BLACK, (100,320,440,fontsize))
        #update the board to display this topic
        topictext_surface = font.render(s.title(), True, WHITE)
        screen.blit(topictext_surface, (10, 10))
        return newWord.random_word()
    
    #-- general function to blit text to screen
    def blitTextToScreen(text):
        txt_surface = font.render(text, True, color_active)
        screen.blit(txt_surface, (choiceContainer.x+5, choiceContainer.y+5))
        
        
    #-- receive the user's guess
    def receiveUserGuess(guess, word, numIncorr):
        print("guess:" + guess + " word:" + word)
        guess = guess.lower()
        word = word.lower()
        if len(guess) > 1:
            print("invalid guess, guess too long:" + guess)
            return guess
        #guess is in the word
        elif guess in word:
            allFound = False
            #the guess is in the word, but there may be multiples
            while not allFound:
                #start by finding the first location
                location = word.find(guess)
                print("location of word.find(guess):")
                print(location)              
            #now we know where it is in the string, use this information to render it to the board
            #wordLineLength = 20
                wordLineY = 220
                wordLineX = 0
                for x in range(0,len(word)):
                    if not (x == location):
                    #we move to the next line
                        wordLineX += 40
                    elif x == location:
                    #we are at the location
                        print("at location, blit to screen")
                        txt_surface = font.render(guess, True, WHITE)
                        screen.blit(txt_surface, (wordLineX+25, wordLineY))
                        pygame.display.flip()
                        wordLineX += 40
                #remove the found character from the word string
                word = word[:location] + word[location+1:]
                if guess not in word:
                    allFound = True
            return numIncorr
        
        elif guess not in word:
            numIncorr += 1
            print("no")
            return numIncorr
        else:
            print("invalid guess, computer is confused:" + guess)
            return numIncorr
            
            
            
    #-- check the guess against the chosen word    
    #def guessCheck():
        
    #-- main game loop
    topicMenu()
    drawBoard()
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
                        #this is the random word the player needs to guess
                        if len(choiceText) > 4:
                            wordToGuess = receiveTopicChoice(choiceText)
                            print(wordToGuess)
                        
                        #receive a guess
                        if len(choiceText) < 2:
                            #the guess function will update the incorrect counter
                            countIncorrect = receiveUserGuess(choiceText, wordToGuess, countIncorrect)
                            print(countIncorrect)
                        choiceText = ''
                        #clear the choice container on return
                        screen.fill(BLACK, choiceContainer)
                    elif event.key == pygame.K_BACKSPACE:
                        choiceText = choiceText[:-1]
                    else:
                        choiceText += event.unicode
       
        clock.tick(30)
        
        #render choice text to screen
        blitTextToScreen(choiceText)
        
        #update board at each tick
        #if countGuess == 0:
        updateBoard(countIncorrect, wordToGuess)


        #else updateBoard(countIncorrect)
             
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
        
    