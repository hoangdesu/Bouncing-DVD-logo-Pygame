import pygame as pg
import random

from pygame.constants import FULLSCREEN

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600

class DVD:
    def __init__(self, window) -> None:
        self.window = window
        
        self.sprite = pg.image.load('./dvd.png').convert_alpha()
        self.scaleDown_ratio = 10
        self.width = self.sprite.get_width() // self.scaleDown_ratio
        self.height = self.sprite.get_height() // self.scaleDown_ratio
        self.logo = pg.transform.smoothscale(self.sprite, (self.width, self.height))
        
        self.gap = 10
        self.screen_offset = 5
        self.x = random.randint(self.gap, int(SCREEN_WIDTH - self.width) - self.gap)
        self.y = random.randint(self.gap, int(SCREEN_HEIGHT - self.height) - self.gap)
        
        self.velocity = 4
        self.dx = self.velocity if random.randint(0, 1) == 1 else -self.velocity
        self.dy = self.velocity if random.randint(0, 1) == 1 else -self.velocity
        
        self.color = (0, 0, 0, 0)
        self.newColor = self.getRandomRGBColor()
        
    def getRandomRGBColor(self):
        # limit color range from 50 to avoid blending in the black background
        return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255), 255)
        
    def changeColor(self):
        pg.PixelArray(self.logo).replace(self.color, self.newColor)
        self.color = self.newColor
        self.newColor = self.getRandomRGBColor()
        
    def update(self):
        # touching left and right edges -> flip dx + change color
        if self.x < -self.screen_offset or self.x > SCREEN_WIDTH - self.width + self.screen_offset:
            self.dx = -self.dx
            self.changeColor()
            # self.logo.fill(getRandomRGBColor(), special_flags=pg.BLEND_ADD) --> doesnt work after a few bounces!
            
        # touching top and bottom edges -> flip dy
        if self.y < -self.screen_offset or self.y > SCREEN_HEIGHT - self.height + self.screen_offset:
            self.dy = -self.dy
            self.changeColor()
            
        self.x += self.dx
        self.y -= self.dy
    
        
    def render(self):
        self.window.blit(self.logo, (self.x, self.y))

def main():
    pg.init()
    
    window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Pygame Bouncing DVD")
    
    dvd = DVD(window)
    clock = pg.time.Clock()
    
    running = True
    print(dvd.logo.get_at((50, 50)))
    while running:
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                running = False

        window.fill('#000000')
        
        dvd.update()
        
        dvd.render()
        
        clock.tick(60)
        pg.display.flip()

if __name__ == '__main__':
    main()
    
    
# NOTES: 2 ways to change color:
#     1. simple: fill the logo with blend mode (after some times, it will blend to white -> no more color changes)
#     2. replace pixel array