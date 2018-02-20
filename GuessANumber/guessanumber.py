# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:48:15 2018
Guess A Number
@author: Gary
"""

import random

GAMEGUESS = random.randint(-50,50)    

def UserGuess(x):
    try:
        if x < GAMEGUESS:
            print("The guess is too low")
            AskUser()
        elif x > GAMEGUESS:
            print("The guess is too high")
            AskUser()
        elif x == GAMEGUESS:
            print("You guessed the number!")
    except TypeError:
        print("Invalid Guess")
        AskUser()
    

def AskUser():
    print("I am thinking of a number between -50 and 50")
    answer = int(input("Guess a number: "))
    UserGuess(answer)
    
AskUser()

    