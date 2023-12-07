# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:17:33 2023

@author: Ryang
"""
import simpleGE, pygame

class RedPlayer(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Target.png")
        self.setAngle(90)
        self.setSize(25, 25)
        self.health = 5
        self.x = self.screen.get_width()/2
        self.y = self.screen.get_height()/2
        self.boundAction = self.BOUNCE
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.addForce(.2, self.rotation + 90)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.addForce(.2, self.rotation - 90)
        if self.scene.isKeyPressed(pygame.K_UP):
            self.addForce(.2, self.rotation)
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.addForce(-.2, self.rotation)
        if self.scene.isKeyPressed(pygame.K_x):
            self.speed = 0
        if self.speed != 0:
            self.addForce(((-self.speed)/40), self.dir)
            


class BluePlayer(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Target.png")
        self.setAngle(90)
        self.setSize(25, 25)
        self.health = 5
        self.x = self.screen.get_width()/2
        self.y = self.screen.get_height()/2
        self.boundAction = self.BOUNCE
        
    def checkEvents(self):
        
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.addForce(.5, self.rotation + 90)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.addForce(.5, self.rotation - 90)
        if self.y <= self.screen.get_height():
            self.addForce(self.distanceTo((self.x, self.screen.get_height()))/100, -90)
        if self.y >= self.screen.get_height():
            self.y = self.screen.get_height()

        if self.scene.isKeyPressed(pygame.K_UP):
            if self.y == self.screen.get_height():
                self.addForce(10, self.rotation)
            if self.y <= self.screen.get_height():
                self.addForce(2, self.rotation)

        if self.scene.isKeyPressed(pygame.K_x):
            self.speed = 0
        if self.speed != 0:
            self.addForce(((-self.speed)/40), self.dir)
        
            
class GreenPlayer(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("GreenDot.png")
        self.setAngle(90)
        self.setSize(25, 25)
        self.health = 5
        self.x = self.screen.get_width()/2
        self.y = self.screen.get_height()/2
        self.boundAction = self.STOP
        self.shield = 2
        
    def checkEvents(self):
        
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.rotation = 180
            self.shield = 1
        if self.scene.isKeyPressed(pygame.K_UP):
            self.rotation = 90
            self.shield = 2
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.rotation = -90
            self.shield = 3
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.rotation = 0
            self.shield = 4
        
        if self.scene.isKeyPressed(pygame.K_x):
            self.speed = 0
        if self.speed != 0:
            self.addForce(((-self.speed)/40), self.dir)
        
            
            
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.DEBUG = False
        self.mode = "Normal"
        self.gamestatePause = "Active"
        self.playerChar = GreenPlayer(self)
        
        self.sprites = [self.playerChar]
        
    
    #def update(self):
        

        
        
def main():
    game = Game()
    game.setCaption("Don't Get A Bullseye")
    game.start()
    
if __name__ == "__main__":
    main()
