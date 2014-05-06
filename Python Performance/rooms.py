import random
from character import NPC, Player


class Room:
    
    
    def __init__(self, name):
        
        self.name = name
        
        self.folks = []
        self.items = []
        
    def addFolks(self, user):
        self.folks.append(user)
        
    def removeFolks(self, user):
        self.folks.remove(user)
            
    
    def getFolks(self):
        return self.folks
    
    def listFolks(self):
        if len(self.folks) == 0:
            print "Room Empty of inhabitants.\n"
        for folk in self.folks:
            print folk.handle
            
    def addItems(self, item):
        self.items.append(item)
        
    def removeItems(self, item):
        self.items.remove(item)
    
    def listItems(self):
        if len(self.items) == 0:
            print "No Items in this Room\n"
        else:
            for i in self.items:
                print i
    
    def takeItem(self, player, item):
        if item not in self.items:
            print "That item does not exist here.\n"
            return
        else:
            player.stuff.append(item)
            self.removeItems(item)
            
    def getRandomPerson(self):
        
        if len(self.folks) == 0:
            print "Empty"
        else:
            return random.choice(self.folks)
        
    
        
#End room
#begin board
            
class Board():
    
    def __init__(self, rooms):
        self.size = 0 
        
        
        if rooms > 0:        
            self.size = rooms
        
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        
        for i in range(self.size):
               for j in range(self.size):
                    self.board[i][j] = Room('empty')
                
    def placeOnBoard(self, player, location=[0,0]):
         if location[0] != 0 and location[1] != 0:
             current_room = location
         else:
             current_room = player.location
         
         if not player.isplayer:
             self.board[current_room[0]][current_room[1]].folks.append(player)
             self.board[current_room[0]][current_room[1]].name = player.handle
             
             for item in player.things:
                 self.board[current_room[0]][current_room[1]].items.append(item)
         
         
         
    def removeFromBoard(self, player):
         current_room = player.location
         
         if player in self.board[current_room[0]][current_room[1]].folks:
             self.board[current_room[0]][current_room[1]].folks.remove(player)
             
    
    def checkBoard(self):
        for i in range(self.size):
            for j in range(self.size):
               print self.board[i][j].name, self.board[i][j].description
    
    def roomStats(self, location):
        current_room = self.board[location[0]][location[1]]
        
        
        
        print "\n" + current_room.name + "'s Room\n"
             
        print "%-45s %-55s" % ("Fellow Travelers", "Local Items")
        print "%-45s %-55s" % ("===============", "===============")
        
        for x, y in map(None, current_room.folks, current_room.items):
             if y == None:
                 y = ' '
             if x == None:
                 x = Player(' ', ' ')
                 
             print "%-45s %-55s" % (x.handle, y)
        
        print '\n'
        
       
        
        
    def getRoom(self, location):
        return self.board[location[0]][location[1]]
        
    def findPerson(self, character):
        for i in range(self.size):
               for j in range(self.size):
                    if character in self.board[i][j].folks:
                        return self.board[i][j]
                        
    def moveOnBoard(self, user, move):
   
       self.removeFromBoard(user)
       user.move(move)
       self.placeOnBoard(user)    
    
    def massMove(self):
         for i in range(self.size):
               for j in range(self.size):
                    for k in self.board[i][j].folks:
                        moves = ['hop','skip','jump','retreat']
                        self.moveOnBoard(k, random.choice(moves))
   