# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:27:30 2023

@author: Ryang
"""

import simpleGE, pygame, random

class RedGamePellets(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.x = 3
        self.y = 3
        self.boundAction = self.STOP
        self.images = {
            "damage": pygame.image.load("DarkCoin.png"),
            "heal": pygame.image.load("GreenCoin.png"),
            "even": pygame.image.load("GreyCoin.png"),
            "divide": pygame.image.load("RedCoin.png"),
            "orange": pygame.image.load("OrangeCoin.png"),
            "blue": pygame.image.load("BlueCoin.png"),
            "butterfly": pygame.image.load("Butterfly.png")
        }
        self.imageMaster = self.images["even"]
        
        
    def hide(self):
        self.oldPosition = self.rect.center
        self.setPosition((0, 0))
        self.visible = False
        
    def seekpath(self):
        self.scene.diffVar += (self.scene.diffVar)/1e4
        self.evenSpeed = self.distanceTo(self.scene.playerChar.rect.center)
        self.diceOfFate = random.randint(1,90)
        if self.diceOfFate <= 25:
            self.imageMaster = self.images["damage"]
        if 100 > self.diceOfFate > 90:
            self.imageMaster = self.images["divide"]
        if 50 >= self.diceOfFate > 25:
            self.imageMaster = self.images["blue"]
        if 75 >= self.diceOfFate > 50:
            self.imageMaster = self.images["orange"]
        if 90 >= self.diceOfFate > 80:
            self.imageMaster = self.images["even"]
        if 80 >= self.diceOfFate > 75:
            self.imageMaster = self.images["heal"]
        if self.diceOfFate == 100:
            self.imageMaster = self.images["butterfly"]
            self.setPosition((self.screen.get_width()/2, self.screen.get_height()/2))
            self.dir = random.randint(-180,180)
            

        if self.imageMaster != self.images["butterfly"]:
            self.dir = self.dirTo(self.scene.playerChar.rect.center) + (self.scene.diffVar * random.randint(-1,1))
        
    def movePellet(self):
        
        if self.imageMaster == self.images["damage"]:
            self.forward((self.distanceTo(self.scene.playerChar.rect.center))/(100/self.scene.diffVar))

        if self.imageMaster == self.images["divide"]:
            self.forward((self.distanceTo(self.scene.playerChar.rect.center))/(100/self.scene.diffVar))

        if self.imageMaster == self.images["blue"]:
            self.forward(self.evenSpeed/(100/self.scene.diffVar))

        if self.imageMaster == self.images["orange"]:
            self.forward(self.evenSpeed/(100/self.scene.diffVar))

        if self.imageMaster == self.images["even"]:
            self.forward((self.distanceTo(self.scene.playerChar.rect.center))/(100/self.scene.diffVar))

        if self.imageMaster == self.images["heal"]:
            self.forward(self.evenSpeed/(100/self.scene.diffVar))
            
        if self.imageMaster == self.images["butterfly"]:
            self.addForce(random.randint(-1, 1)/10, (self.dirTo(self.scene.playerChar.rect.center)))

        
    def checkEvents(self):
        #self.addForce(0.01, self.dirTo(self.scene.playerChar.rect.center)+90)
        if self.scene.gamestatePause == "Active":
            self.movePellet()
            if self.x > self.screen.get_width():
                self.speed = 0
                self.x = self.screen.get_width()
                self.y = random.randint(0, self.screen.get_height())
                self.scene.score += 1
                self.seekpath()
                "This might be ok."        
            if self.y > self.screen.get_height():
                self.speed = 0
                self.y = self.screen.get_height()
                self.x = random.randint(0, self.screen.get_width())
                self.scene.score += 1
                self.seekpath()
                "Well."            
            if self.x < 0:
                self.speed = 0
                self.x = 0
                self.y = random.randint(0, self.screen.get_height())
                self.scene.score += 1
                self.seekpath()
                "Figure it out."            
            if self.y < 0:
                self.speed = 0
                self.y = 0
                self.x = random.randint(0, self.screen.get_width())
                self.scene.score += 1
                self.seekpath()
                "Are you listening?"
                
            if self.collidesWith(self.scene.playerChar):
                self.pelletHit()
                
            
                
    def pelletHit(self):
                if self.imageMaster == self.images["damage"]:
                    self.x = 0
                    self.y = 0
                    self.scene.currentHealth -= self.scene.diffVar
                    self.seekpath()
                if self.imageMaster == self.images["divide"]:
                    self.x = 0
                    self.y = 0
                    self.scene.currentHealth /= self.scene.diffVar
                    self.seekpath()
                if self.imageMaster == self.images["blue"]:
                    if self.scene.playerChar.speed != 0:
                        self.x = 0
                        self.y = 0
                        self.scene.currentHealth -= self.scene.diffVar
                        self.seekpath()
                    else:
                        pass
                if self.imageMaster == self.images["orange"]:
                    if self.scene.playerChar.speed == 0:
                        self.x = 0
                        self.y = 0
                        self.scene.currentHealth -= self.scene.diffVar
                        self.seekpath()
                    else:
                        pass
                if self.imageMaster == self.images["even"]:
                    self.x = 0
                    self.y = 0
                    self.scene.currentHealth = self.scene.maxHealth
                    self.seekpath()
                if self.imageMaster == self.images["heal"]:
                    self.x = 0
                    self.y = 0
                    self.scene.currentHealth += 1   
                    self.seekpath()
                    
                    
                    
                    
class GreenGamePellets(RedGamePellets):
    def __init__(self, scene):
        super().__init__(scene)
        self.x = 3
        self.y = 3
        self.boundAction = self.STOP
        self.images = {
            "damage": pygame.image.load("DarkCoin.png"),
            "heal": pygame.image.load("GreenCoin.png"),
            "even": pygame.image.load("GreyCoin.png"),
            "divide": pygame.image.load("RedCoin.png"),
            "orange": pygame.image.load("OrangeCoin.png"),
            "blue": pygame.image.load("BlueCoin.png"),
            "butterfly": pygame.image.load("Butterfly.png")
        }
        self.imageMaster = self.images["even"]
        self.evenSpeed = 5
                    
    def checkEvents(self):
        #self.addForce(0.01, self.dirTo(self.scene.playerChar.rect.center)+90)
        if self.scene.gamestatePause == "Active":
            self.movePellet()
            if self.x > self.screen.get_width():
                self.speed = 0
                self.x = self.screen.get_width()
                self.y = random.randint(0, self.screen.get_height())
                self.scene.score += 1
                self.seekpath()
                "This might be ok."        
            if self.y > self.screen.get_height():
                self.speed = 0
                self.y = self.screen.get_height()
                self.x = random.randint(0, self.screen.get_width())
                self.scene.score += 1
                self.seekpath()
                "Well."            
            if self.x < 0:
                self.speed = 0
                self.x = 0
                self.y = random.randint(0, self.screen.get_height())
                self.scene.score += 1
                self.seekpath()
                "Figure it out."            
            if self.y < 0:
                self.speed = 0
                self.y = 0
                self.x = random.randint(0, self.screen.get_width())
                self.scene.score += 1
                self.seekpath()
                "Are you listening?"
                
            if self.collidesWith(self.scene.playerChar):
                pain = False
                if self.path == 2 and self.scene.playerChar.shield != 2:
                    self.pelletHit()
                    pain = True
                if self.path == 1 and self.scene.playerChar.shield != 1:
                    self.pelletHit()
                    pain = True

                if self.path == 3 and self.scene.playerChar.shield != 3:
                    self.pelletHit()
                    pain = True

                if self.path == 4 and self.scene.playerChar.shield != 4:
                    self.pelletHit()
                    pain = True

                self.seekpath()
                if pain != True:
                    self.scene.score += 1
                    pain = False
                      
    def movePellet(self):
            self.forward(self.evenSpeed)            
    
    def seekpath(self):
        self.scene.diffVar += (self.scene.diffVar)/1e4
        self.evenSpeed = random.randint(3, 5)
        self.diceOfFate = random.randint(1,90)
        if self.diceOfFate <= 25:
            self.imageMaster = self.images["damage"]
        if 100 > self.diceOfFate > 90:
            self.imageMaster = self.images["divide"]
        if 50 >= self.diceOfFate > 25:
            self.imageMaster = self.images["blue"]
        if 75 >= self.diceOfFate > 50:
            self.imageMaster = self.images["orange"]
        if 90 >= self.diceOfFate > 80:
            self.imageMaster = self.images["even"]
        if 80 >= self.diceOfFate > 75:
            self.imageMaster = self.images["heal"]
        if self.diceOfFate == 100:
            self.imageMaster = self.images["butterfly"]
            self.setPosition((self.screen.get_width()/2, self.screen.get_height()/2))
            self.dir = random.randint(-180,180)
            
            '''  2
               1   4
                 3
            '''
        if self.imageMaster != self.images["butterfly"]:
            self.path = random.randint(1,4)
            if self.path == 1:
                self.x = 0
                self.y = self.scene.playerChar.rect.y
            if self.path == 2:
                self.x = self.scene.playerChar.rect.x
                self.y = 0
            if self.path == 3:
                self.x = self.scene.playerChar.rect.x
                self.y = self.screen.get_height()
            if self.path == 4:
                self.x = self.screen.get_width()
                self.y = self.scene.playerChar.rect.y
            self.dir = self.dirTo(self.scene.playerChar.rect.center)

    def pelletHit(self):
                if self.imageMaster == self.images["damage"]:
                    self.scene.currentHealth -= self.scene.diffVar
                if self.imageMaster == self.images["divide"]:
                    self.scene.currentHealth /= self.scene.diffVar
                if self.imageMaster == self.images["blue"]:
                    if self.scene.playerChar.speed != 0:
                        self.scene.currentHealth -= self.scene.diffVar
                    else:
                        pass
                if self.imageMaster == self.images["orange"]:
                    if self.scene.playerChar.speed == 0:
                        self.scene.currentHealth -= self.scene.diffVar
                    else:
                        pass
                if self.imageMaster == self.images["even"]:
                    self.scene.currentHealth = self.scene.maxHealth
                if self.imageMaster == self.images["heal"]:
                    self.scene.currentHealth += 1   
                    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.mode = "Normal"
        self.gamestatePause = "Active"
        self.playerChar = simpleGE.SuperSprite(self)
        self.playerChar.boundAction = self.playerChar.WRAP
        self.bullets = []
        for bullet in range(25):
            self.bullets.append(GreenGamePellets(self))
            
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50, 50)
        self.score = 0

        self.lblTime = simpleGE.Label()
        self.lblTime.center = (550, 50)
        
            
        self.lblDiff = simpleGE.Label()
        self.lblDiff.center = (self.screen.get_width()/2, self.screen.get_height()/2)

        self.lblHealth = simpleGE.Label()
        self.lblHealth.text = "Health: 5"
        self.lblHealth.center = (300, 50)
        self.maxHealth = 5
        self.currentHealth = self.maxHealth
        self.boostH = self.score
        self.diffVar = 1
        
        self.timer = simpleGE.Timer()
        
        self.lblAdvice = simpleGE.MultiLabel()
        self.lblAdvice.size = (360,150)
        self.lblAdvice.hide()
        
        self.resumeButton = simpleGE.Button()
        self.quitButton = simpleGE.Button()
        self.resumeButton.hide()
        self.quitButton.hide()
        


        self.sprites = [self.quitButton, self.resumeButton, self.lblAdvice, self.lblScore, self.lblHealth, self.lblTime, self.playerChar, self.bullets]
        if self.DEBUG:
            self.sprites.insert(0, self.lblDiff)

        
    
    def update(self):
        if self.mode == ["Normal", "Debug"]:
            if self.score / 10 >= self.boostH + 3:
                self.maxHealth += 1
                self.boostH += 3
        self.lblHealth.text = f"Health: {self.currentHealth:.1f}/{self.maxHealth:.1f}"
        self.lblTime.text = f"Time: {self.timer.getElapsedTime():.2f}"
        self.lblScore.text = f"score: {self.score}"
        self.playerChar.addForce(0.01, self.playerChar.rotation)
        self.playerChar.rotateBy(random.randint(-10,10))
        if self.DEBUG:
            self.lblDiff.text = f"Diff: {self.diffVar:.4f}"
        
        if self.currentHealth < self.maxHealth:
            self.currentHealth += (1/30)/self.diffVar
        
        if self.DEBUG:
            pass
        else:
            
            if self.currentHealth <= 0:
                self.stop()

        
        
def main():
    game = Game()
    game.setCaption("CHAOS, CHAOS!")
    game.start()
    
if __name__ == "__main__":
    main()