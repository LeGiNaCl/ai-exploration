import pyautogui as pyag
import time  
class CharacterController:
    keyPressDelay = 0.01
    
    def __init(self):
        print("Character Controller Initialization")

    def toggleKey(self, key):
        pyag.keyDown(key)
        time.sleep(self.keyPressDelay)
        pyag.keyUp(key)

    def toggleMultipleKeys(self, keys):
        for key in keys:
            pyag.keyDown(key)
        time.sleep(self.keyPressDelay)
        for key in keys:
            pyag.keyUp(key)
    
    def moveNorth(self):
        self.toggleKey('w')
        
    def moveNorthEast(self):
        self.toggleMultipleKeys(['w','d'])
        
    def moveNorthWest(self):
        self.toggleMultipleKeys(['w','a'])
        
    def moveEast(self):
        self.toggleKey('d')
    
    def moveWest(self):
        self.toggleKey('a')
        
    def moveSouth(self):
        self.toggleKey('s')
        
    def moveSouthEast(self):
        self.toggleMultipleKeys(['s', 'd'])
        
    def moveSouthWest(self):
        self.toggleMultipleKeys(['s', 'a'])
        
    def shootNorth(self):
        self.toggleKey('up')
        
    def shootEast(self):
        self.toggleKey('right')
        
    def shootWest(self):
        self.toggleKey('left')
        
    def shootSouth(self):
        self.toggleKey('down')
        