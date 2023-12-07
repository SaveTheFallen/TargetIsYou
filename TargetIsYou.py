# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:15:29 2023

@author: Ryang
"""
import simpleGE, pygame, random

import Player_File, Pellets_Base
            
class ButtonMaster(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.hide()
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.scene.pauseGame()
        if self.scene.resumeButton.clicked:
            self.scene.unpauseGame()
        if self.scene.quitButton.clicked:
            self.scene.stop()
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.mode = "GreenMode"
        self.gamestatePause = "Active"
        self.bullets = []
        if self.mode == "RedMode" or self.mode == "HardMode":
            self.playerChar = Player_File.RedPlayer(self)
            for bullet in range(25):
                self.bullets.append(Pellets_Base.RedGamePellets(self))
        if self.mode == "GreenMode":
            self.playerChar = Player_File.GreenPlayer(self)
            for bullet in range(5):
                self.bullets.append(Pellets_Base.GreenGamePellets(self))
            
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
        if self.mode == "HardMode":
            self.maxHealth = 20
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
        
        self.buttonMaster = ButtonMaster(self)
        


        self.sprites = [self.quitButton, self.resumeButton, self.lblAdvice, self.lblScore, self.lblHealth, self.lblTime, self.playerChar, self.bullets, self.buttonMaster]
        if self.DEBUG:
            self.sprites.insert(0, self.lblDiff)
    

    
    def pauseGame(self):
        if self.gamestatePause == "Active":
            self.playerChar.hide()
            self.lblScore.hide()
            self.lblHealth.hide()
            self.lblTime.hide()
            for pellet in self.bullets:
                pellet.hide()
            if self.DEBUG:
                self.lblDiff.hide()
            self.gamestatePause = "Paused"
            
            self.lblAdvice.show((self.screen.get_width()/2, self.screen.get_height()/3))
            adviceRoulette = random.randint(1,7)
            if adviceRoulette == 1:
                self.lblAdvice.textLines = ["Orange and Blue pellets", "are both motion-based.", "Orange can't see motion,", "and Blue is the opposite."]
            if adviceRoulette == 2:
                self.lblAdvice.textLines = ["Grey pellets set your health to max.", "Quite helpful when low health,", "but problematic if you've", "saved up health with Green pellets."]
            if adviceRoulette == 3:
                self.lblAdvice.textLines = ["Green pellets increase your", "current health, so", "grab them as often as you can!"]
            if adviceRoulette == 4:
                self.lblAdvice.textLines = ["Beware of the Red pellets..", "Their damage is percent-based,", "so they gain more power", "as you gain more health."]
            if adviceRoulette == 5:
                self.lblAdvice.textLines = ["The pellets move faster", "as you gain more points", "AND as you take damage", "so don't let your HP drop."]
            if adviceRoulette == 6:
                self.lblAdvice.textLines = ["You can instantly stop", "by pressing the [X] key.", "Think of it as...", "..a blue stop sign."]
            if adviceRoulette == 7:
                self.lblAdvice.textLines = ["There's a 1 in 100 chance", "that a butterfly will appear.", "it's harmless though,", "so just ignore it."]


            self.resumeButton.show((self.screen.get_width()/3, 2*self.screen.get_height()/3))
            self.resumeButton.text = "Continue"
            self.quitButton.show((2*self.screen.get_width()/3, 2*self.screen.get_height()/3))
            self.quitButton.text = "Quit"
            

    def unpauseGame(self):
            
        if self.gamestatePause == "Paused":
            
            self.playerChar.show()
            self.lblScore.show((50, 50))
            self.lblHealth.show((300, 50))
            self.lblTime.show((550, 50))
            for pellet in self.bullets:
                pellet.show()
            if self.DEBUG:
                self.lblDiff.show((self.screen.get_width()/2, self.screen.get_height()/2))
            self.gamestatePause = "Active"
            
            self.lblAdvice.hide()
            self.resumeButton.hide()
            self.quitButton.hide()

    
    
    def update(self):
        if self.mode in ["Normal", "Debug"]:
            if self.score / 50 >= self.boostH + 1:
                self.maxHealth += 1
                self.boostH += 1
        self.lblHealth.text = f"Health: {self.currentHealth:.1f}/{self.maxHealth:.1f}"
        self.lblTime.text = f"Time: {self.timer.getElapsedTime():.2f}"
        self.lblScore.text = f"score: {self.score}"
        if self.DEBUG:
            self.lblDiff.text = f"Diff: {self.diffVar:.4f}"
        
        if self.mode != "HardMode":
            if self.currentHealth < self.maxHealth:
                self.currentHealth += (1/30)/self.diffVar
        
        if self.DEBUG:
            if isinstance(self.playerChar, Player_File.GreenPlayer):
                self.playerChar.shield = random.randint(1,4)
                self.playerChar.rotation = self.playerChar.shield*90
            pass
            
        else:
            
            if self.currentHealth <= 0:
                self.pauseGame()
                self.lblAdvice.textLines = ["[Congratulations], YOU LOSE!"]
                self.resumeButton.hide()
                self.quitButton.show((self.screen.get_width()/2, 2*self.screen.get_height()/3))
                self.quitButton.text = "Quit"



        
        
def main():
    game = Game()
    game.setCaption("Don't Get A Bullseye")
    game.start()
    
if __name__ == "__main__":
    main()


