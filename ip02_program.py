# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:08:40 2023

@author: AfiqahHasbullah
"""


#declare function

def game_opening(players) :
    print('do something fancy')

def setup_game_board(players):
    pass

def setup_game_state(players) :
    pass

def move(players) :
    pass

def update_game_state(players):
    return True

def swap_turn(players):
    print('swap the players')


#First a game opening and ask names of 2 players
players = ['Habil','Qabil']
game_opening(players)

#then, setup the game:set location of pieces,
#who to play first, if there is a GUI, setup the GUI
setup_game_board(players)
setup_game_state(players)

#let's play 
finish = False
while not finish:
    move(players)
    finish = update_game_state(players)
    swap_turn(players)
    
