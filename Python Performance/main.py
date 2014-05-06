#!/usr/bin/python

import tweepy
import random
import time

from functions import parseCommand, generateNPC
from rooms import Room, Board
from character import NPC, Player

"""

Primary Program Variables and initialization
"""
#intro = open('txt/intro.txt')
#intro = intro.readlines()
#t = 3.0

#for items in intro:
 #   print items
  #  time.sleep(t)
    
   # t -= 0.1
    
actions = ['ask', 'demand', 'give', 'hold', 'look', 'take', 'me']
movement = ['hop', 'skip', 'jump', 'retreat']
board = Board(3)
player = Player('Mysterious Player', 'The Mysterious Player you control in a mysterious fashion')

command = ''
current_room = board.getRoom(player.location)



"""
initialize Twitter authorization and access
"""
consumer_key ='pHe4zVpJynRtg0QcuFng'
consumer_secret = 'zOxKCbTKnL7NnDh64MB7jurQouR7Kr02d1WNhB0qc'
access_token = '87458583-HxhtzCcc6Qcq3qfsXN9zJij5pukfvv8jo2Cgc2XlA'
access_token_secret = '6mpCNqHdw98vdFeupb7oDEYIqlz35LVn1WdVixFnOUhZc'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

"""
intro
"""




"""
Player and two initial NPCs on Board
"""
for i in range(3):
    board.placeOnBoard(generateNPC(api))

board.placeOnBoard(player)

"""
main logic
"""




while command != 'q':
    curr = board.getRoom(player.location)
    player.turns += 1
    
    command = raw_input("What would you like to do today?> ")
    command = command.lower()
    
    if not parseCommand(command, actions, movement):
        pass
    
    if command in movement:

        board.moveOnBoard(player, command)
        board.placeOnBoard(generateNPC(api), location=player.location)
        board.placeOnBoard(generateNPC(api), location=player.location)
        board.massMove()
        
    elif command in actions:
        rand = board.getRoom(player.location)
        
        
        obj = rand.getRandomPerson()
        
        if command == 'look':
            board.roomStats(player.location)
        if command == 'give':
            player.giving(obj)
        if command =='take':
            player.take(curr)
        elif command == 'hold' or command == 'ask' or command == 'demand':
            if command == 'hold' and obj.react(command, player) < 0:
                board.moveOnBoard(obj, 'retreat')
            else:
                obj.react(command, player)
            
            
    if player.turns == 3:
        time.sleep(4)
        print "You could always try looking...\n"
    if player.turns == 6:
        time.sleep(4)
        print "Holding someone often makes them more comfortable.\n"
    

        


