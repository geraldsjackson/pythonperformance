# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 19:59:02 2014

@author: Gerald
"""
import random
import tweepy

from character import NPC, Player
from rooms import Room, Board


"""
placeOnBoard

"""    

   
   
     

def generateNPC(api):
    f = open('txt/people.txt')
    f = f.readlines()
    rand = random.choice(f)
    
    tweets = api.search(q=rand, rpp=1, show_user=True)
    name = tweets[0].user.screen_name
    desc = tweets[0].user.description    
    
    temp_npc = NPC(name, desc, api)
    return temp_npc
        
    
    
"""
parseResults takes a search from the Twitter API and breaks the data down
into useable information for the program: text, user, etc.
"""
def parseResults(results):
    
    texts = []
    words = []
    splits = []

    for tweet in results:
        texts.append(str(tweet.text))

    for item in texts:
        words.append(item)
    
    for stuff in words:
        splits.append(stuff.split()) 
    
    return splits
    
    
#Assuming a particular order for language inputs: VERB-ARTICLE-NOUN with optional object #extenions: VERB-ARTICLE-NOUN-ARTICLE-OBJECT
def parseCommand(command, list1, list2):
    
    f = open('txt/responses.txt')
    f = f.readlines()
    
    the_list = command.split()
    items = len(the_list)
    
    if items != 1:
       print '\n' + f[random.randint(0, len(f) - 1)]
       return False
    
    if command not in list1 and command not in list2 and command != 'q':
        print "I am not able to process that command\n"
        return False
        
    else:
        return command
        
    

    
  #  if checkRoom(parsed_command[0], parsed_command[1]) && checkPerson(parsed_command[0], parsed_command[1]):
        #do stuff
    
#def checkRoom(thing, direct, direct2):
 #   if thing in room && direct in room:
  #      return True
   # else:
    #    print "That is not here."
     #   return False
            
#def checkPerson(thing, direct, direct2):
 #   if think in person && direct in person:
  #      return True
   # else:
    #    return False
    
