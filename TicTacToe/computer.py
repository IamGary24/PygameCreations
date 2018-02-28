# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:55:48 2018
track the ai controlled player
@author: Gary
"""

class Computer:
    
    def __init__(self, token):
        self.token = token #this will either be circles or exes
        
    #this will take the computer's turn
    def turn(self, board):
        #if the computer is exes
        index = None
        if self.token == "exes":
            #if the center space is open
            if not board[1][1] == 'e' and not board[1][1] == 'c':
                board[1][1] = 'e'
                index = 1,1
            #if top left is open
            elif not board[0][0] == 'e' and not board[0][0] == 'c':
                board[0][0] = 'e'
                index = 0,0
            #if bottom right is open
            elif not board[2][2] == 'e' and not board[2][2] == 'c':
                board [2][2] = 'e'
                index = 2,2
                
        if self.token == "circles":
            if not board[1][1] == 'e' and not board[1][1] == 'c':
                board[1][1] = 'c'
                index = 1,1
            #if top left is open
            elif not board[0][0] == 'e' and not board[0][0] == 'c':
                board[0][0] = 'c'
                index = 0,0
            #if bottom right is open
            elif not board[2][2] == 'e' and not board[2][2] == 'c':
                board [2][2] = 'c'
                index = 2,2
        
        return board, index
        