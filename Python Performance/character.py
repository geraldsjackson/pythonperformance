# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 11:55:30 2014

@author: Gerald
"""
import random

class Character:
    
    def __init__(self, user, profile):
        
        self.handle = user
        self.description = profile
        self.location = [0,0]
        self.isplayer = ''
        
     
    """
     react is the primary function for recieving actions from the user, with 
     conditions set on how each reaction will occur (typically by calling 
     and associated class method)
    """
  
    def move(self, direction):
        cordx = self.location[0]
        cordy = self.location[1]
        
        if direction == 'hop':
            cordx += 1
        elif direction == 'skip':
            cordy += 1
        elif direction == 'jump':
            cordx -= 1
        elif direction == 'retreat':
            cordy -= 1
        
        coordinates = [self.wrapAround(cordx), self.wrapAround(cordy)]
        self.location = coordinates
        
    """
    wrapAround just checks a coordinate and wraps movement around the board
    """
    def wrapAround(self, num):
        i = num

        if num > 2:
            i -= 3
        elif num < 0:
            i += 3
        return i
 

#End Character Class

#Begin NPC Class


class NPC(Character):
    
    def __init__(self, user, profile, api):
        Character.__init__(self, user, profile)
        self.API = api
        self.valued = []
        self.status_spectrum = ['bad', 'whatever', 'good']
        self.status = 1
        self.good_responses = self.readResponses('txt/good_responses.txt')
        self.bad_responses = self.readResponses('txt/bad_responses.txt')
        self.isplayer = False
        self.things = []
        
        self.tweets = self.API.user_timeline(screen_name=user, count=30)
        self.returnHashes()
        self.valued.append(self.things)
        
    """
    readResponses populates instance variables with canned responses from
    local text files
    """
    
    def readResponses(self, filename):
        f = open(filename)
        f = f.readlines()
        return f
        
        
    def repopulateTweets(self):
        self.tweets = self.api.user_timeline(screen_name=self.user, count=30)
    
    
    """
     react is the primary function for recieving actions from the user, with 
     conditions set on how each reaction will occur (typically by calling 
     and associated class method)
    """
    def react(self, action, player, item='nothing'):
      
         if action == 'dance':
             pass
         
         elif action == 'ask':
             if self.status > 1:
                 self.talk()
                 player.increaseStats(i=1)
             elif self.status == 1:
                 rand = random.randint(0, 1)
                 if rand == 1:
                     self.talk()
                     player.increaseStats(i=1)
                 else:
                     print self.handle + ' is indifferent to you at the moment.'
             else:
                 print self.handle + ' is not speaking to you at the moment'
                 player.increaseStats(sl=1)
         
         elif action == 'demand':
             if self.status >= 1:
                 self.talk()
                 self.reOrient('-')
                 player.increaseStats(i=-1, k=-1)
             else:
                 print self.handle + ' Will not cave to your demands!!!'
                 player.increaseStats(i=-1)
             
         elif action == 'hold':
             if self.status >= 1:
                 rand = random.randint(0, 1)
                 if rand == 1:
                     self.reOrient('+')
                     player.increaseStats(k=1)
                 else:
                     print "\nMade extremely uncomfortable, " + self.handle + " leaves the room."
                     player.increaseStats(sl=1)
                     return -1
             else:
                 print "\nMade extremely uncomfortable, " + self.handle + " leaves the room."
                 player.increaseStats(sl=1)
                 return -1
                 
         
         #elif action == 'refuse':
             
         elif action == 'give':
             if item != 'nothing' and item in self.valued:
                 print self.handle + " loves your gift!"
                 self.reOrient('+')
                 player.increaseStats(k=1, i=1)
             else:
                 rand = random.randint(-1, 1)
                 if rand < 0 and self.status == 0:
                     self.reOrient('-')
                     player.increaseStats(k=-1) 
                     print
                 else:
                     self.reOrient('-')
                     player.increaseStats(k=-1) 
                 
         print '\n'
         
    def talk(self):
        
        rand = random.randint(0,9)
        
        print '\n' + self.handle + 'says: ' + self.tweets[rand].text
        
    """
      reOrient adjusts the character's orientation (for NPC's). This controls
     how the character will react to the player and her actions, depending on context 
     and such
    """
    def reOrient(self, scale):
        if scale == '+':
            if self.status == 2:
                pass
            else:
                self.status += 1
                print '\n' + self.handle + " looks upon you favorably!"
        
        if scale == '-':
            if self.status == 0:
                pass
            else:
                self.status -= 1
                print '\n' + self.handle + " is disappointed in you." 
    
    def returnHashes(self):
        
        for i in range(3):
            extractor = str(self.tweets[i].text)
            extractor = extractor.split()
            
            for word in extractor:
                if word.startswith('#') or word.startswith('@'):
                    self.things.append(word)
        things = set(self.things)
        self.things = list(things)
        
        
        
#End NPC Class
#Begin Player Class
            

class Player(Character):
    
    def __init__(self, user, profile):
        
        Character.__init__(self, user, profile)
        self.stuff = []
        
        self.karma = 0
        self.intellect = 0
        self.self_loathing = 0
        
        self.isplayer = True
        self.turns = 0

   
                
    def increaseStats(self, k=0, i=0, sl=0):
        self.karma += k
        self.intellect += i
        self.self_loathing += sl
        
        
        if k > 0:
            print "Karma Up!"
        elif k < 0:
            print "Karma Down!"
            
        if i > 0:
            print "Intellect Up!"
        elif i < 0:
            print "Intellect Down!"
            
        if sl > 0:
            print "Self Loathing Up!\n"
        elif sl < 0:
            print "Self Loathing Down!\n"
        

        
    
    def giving(self, npc):
        print "\nInventory \n====================="
        
        if len(self.stuff) == 0:
            print 'Nothing! You have NOTHING! Good DAY sir!\n'
            return 0
        else:
            for item in self.stuff:
                print item
            
        thing = 'nothing'
        
        thing = raw_input("\nWhat would you like to give?: ")
            
    
        if thing not in self.stuff:
            print 'You can not give away what you do not have.\n'
        else:
            self.stuff.remove(thing)
            
        print "\nGave " + npc.handle + " " + thing
        npc.react('give', self, item=thing)
            
    def take(self, room):
        if len(room.items) == 0:
            room.listItems
            return
        else:
            room.listItems
            thing = raw_input("\nWhat would you like to take?> ")
        
            room.takeItem(self, thing)
        
        
    
    def printStats(self):
        print str(self.karma) + '\n' + str(self.intellect) + '\n' + str(self.self_loathing)
            
        
 
        

        
    
    