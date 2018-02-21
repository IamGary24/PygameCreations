# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:32:59 2018

@author: Gary
"""
import random
#-- Class to choose a word --

#-- Base Class that holds the generic topic --

class Word:
    
    wordChoices = []
    topic = ''

#-- inherited classes that each form a topic --
# these need to hold the dictionary of words and choose the random word from those dictionarys
# also they will need to know who they are as in what topic


#-- Person topic
class Person(Word):
    
    wordChoices = ['Doctor Strange', 'Thor God of Thunder', 'Captain America']
    
    #return a random word from the list
    def random_word(self):
        return self.wordChoices[random.randint(0,(len(self.wordChoices))-1)]

#-- Place topic       
class Place(Word):
    
    wordChoices = ['Asgard', 'New York', 'Wakanda']
    
    def random_word(self):
        return self.wordChoices[random.randint(0,(len(self.wordChoices))-1)]
    
#-- Thing topic
class Thing(Word):
    
    wordChoices = ['Mjolnir', 'Shield', 'Eye of Agamotto']
    
    def random_word(self):
        return self.wordChoices[random.randint(0,(len(self.wordChoices))-1)]
