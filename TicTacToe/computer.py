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
            #if left middle is open and right middle is open
            elif not board[1][0] == 'e' and not board[1][0] == 'c' and not board[1][2] == 'c' and not board [1][2] == 'e':
                board[1][0] = 'e'
                index = 1,0
            #if we have left middle and center and right middle is open
            elif not board[1][2] == 'c' and board[1][0] == 'e' and board[1][1] == 'e':
                board[1][2] = 'e'
                index = 1,2
            #if top middle is open and bottom middle is open
            elif not board[0][1] == 'e' and not board[0][1] == 'c' and not board[2][1] == 'c' and not board[2][1] == 'e':
                board [0][1] = 'e'
                index = 0,1
            #if we have top middle and center and bottom middle is open
            elif not board[2][1] == 'c' and board[1][1] == 'e' and board[0][1] == 'e':
                board[2][1] = 'e'
                index = 2,1
            #if top left is open
            elif not board[0][0] == 'e' and not board[0][0] == 'c':
                board [0][0] = 'e'
                index = 0,0
            #if we own top left and center and bottom right is open
            elif not board[2][2] == 'c' and board[1][1] == 'e' and board[0][0] == 'e':
                board[2][2] = 'e'
                index = 2,2
            #if we own top left and middle left and bottom left is open
            elif not board[2][0] == 'c' and board[0][0] == 'e' and board[1][0] == 'e':
                board[2][0] = 'e'
                index = 2,0
            #if top right is open
            elif not board[0][2] == 'e' and not board[0][2] == 'c':
                board [0][2] = 'e'
                index = 0,2
            #if bottom right is open
            elif not board[2][2] == 'e' and not board[2][2] == 'c':
                board [2][2] = 'e'
                index = 2,2
            
                
        if self.token == "circles":
            #if center is open
            if not board[1][1] == 'e' and not board[1][1] == 'c':
                board[1][1] = 'c'
                index = 1,1
            #if top left is open
            elif not board[0][0] == 'e' and not board[0][0] == 'c':
                board[0][0] = 'c'
                index = 0,0
            #check to see if the opponenet owns the center tile, if they do check the middle tiles
            if board[1][1] == 'e' and self.checkMiddles(board):
                #they own a middle tile, now find it and block their victory
                #they own top middle
                if board[0][1] == 'e' and not board[2][1] == 'c':
                    board[2][1] = 'c'
                    index = 2,1
                #they own bottom middle
                elif board[2][1] == 'e' and not board[0][1] == 'c':
                    board[0][1] = 'c'
                    index = 0,1
                #they own right middle
                elif board[1][2] == 'e' and not board[1][0] == 'c':
                    board[1][0] = 'c'
                    index = 1,0
                #they own left middle
                elif board[1][0] == 'e' and not board[1][2] == 'c':
                    board[1][2] = 'c'
                    index = 1,2
            #check to see if the opponent owns a diagonal tile and the center, block them
            if board[1][1] == 'e' and self.checkCorners(board):                
                #they own a corner tile, now find it and block their victory
                #they own top left
                if board[0][0] == 'e' and not board[2][2] == 'c':
                    board[2][2] = 'c'
                    index = 2,2
                #they own top right
                elif board[0][2] == 'e' and not board[2][0] == 'c':
                    board[2][0] = 'c'
                    index = 2,0
                #they own bottom left
                elif board[2][0] == 'e' and not board[0][2] == 'c':
                    board[0][2] = 'c'
                    index = 0,2
                #they own bottom right
                elif board[2][2] == 'e' and not board[0][0] == 'c':
                    board[0][0] = 'c'
                    index = 0,0
            #there isn't a way to lose and there are open locations to play, so lets do that
            elif not board[1][2] =='e' and not board[1][2] =='c':
                board [1][2] = 'c'
                index = 1,2
            elif not board[2][1] =='e' and not board[2][1] =='c':
                board [2][1] = 'c'
                index = 2,1
            elif not board[1][0] =='e' and not board[1][0] =='c':
                board [1][0] = 'c'
                index = 1,0
            
            
        return board, index
    #this function is only for computer token circles, not exes
    def checkMiddles(self, board):
        #check the "plus" sign to make sure that none of them are taken
        if board[1][1] == 'e' or board[1][0] == 'e' or board[2][1] == 'e' or board[1][2] == 'e' or board[1][1] == 'e':
            return True
        
    def checkCorners(self, board):
        #check the "plus" sign to make sure that none of them are taken
        if board[1][1] == 'e' or board[1][0] == 'e' or board[2][1] == 'e' or board[1][2] == 'e' or board[1][1] == 'e':
            return True
            
        
    
        def __del__ (self):
            print("computer died")

        