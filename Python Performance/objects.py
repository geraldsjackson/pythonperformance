class Player:

    __objects = []
    
    def __init__(self):
        self.__objects[0] = "Nothing"
        

class Room:
    
    __contents = []
    __name
    __description
    
    def __init__(self):
        self.__contents[0] = "Empty"
        
    def placeContents(self, objects):
        i = 0
        
        for item in objects:
            self.__contents[i] = item
            
    def checkContents(self, item):
        
    def removeItem(self, item):
        
    def giveDescription(self):
        
class Thing:
    
    __description
    __type
    __name
    

        
    