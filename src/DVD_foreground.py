import pygame as pg
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
LOGO_PATH = '../stuffs/dvd.png'

class DVD:
    def __init__(self, window) -> None:
        self.window = window
        
        self.sprite = pg.image.load(LOGO_PATH)
        self.scaleDown_ratio = 8
        self.width = self.sprite.get_width() // self.scaleDown_ratio
        self.height = self.sprite.get_height() // self.scaleDown_ratio
        self.logo = pg.transform.scale(self.sprite, (self.width, self.height))
        
        self.gap = 10
        self.screen_offset = 5
        self.x = random.randint(self.gap, int(SCREEN_WIDTH - self.width) - self.gap)
        self.y = random.randint(self.gap, int(SCREEN_HEIGHT - self.height) - self.gap)
        
        self.velocity = 4
        self.dx = self.velocity if random.randint(0, 1) == 1 else -self.velocity
        self.dy = self.velocity if random.randint(0, 1) == 1 else -self.velocity
        
        self.color = (0, 0, 0)
        self.newColor = self.getRandomRGBColor()
        
    def getRandomRGBColor(self):
        # limit color range to avoid blending in the black background
        return (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
        
    def changeColor(self):
        pg.PixelArray(self.logo).replace(self.color, self.newColor)
        self.color = self.newColor
        self.newColor = self.getRandomRGBColor()
        
    def update(self):
        # touching left and right edges -> flip dx + change color
        if self.x < -self.screen_offset or self.x > SCREEN_WIDTH - self.width + self.screen_offset:
            self.dx = -self.dx
            self.changeColor()
            
        # touching top and bottom edges -> flip dy
        if self.y < -self.screen_offset or self.y > SCREEN_HEIGHT - self.height + self.screen_offset:
            self.dy = -self.dy
            self.changeColor()
            
        self.x += self.dx
        self.y -= self.dy
    
        
    def render(self):
        self.window.blit(self.logo, (self.x, self.y))