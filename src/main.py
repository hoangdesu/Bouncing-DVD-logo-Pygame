from DVD_foreground import *
# import pygame as pg

from pygame.constants import FULLSCREEN

# SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600


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

        window.fill('#101010')
        
        dvd.update()
        
        dvd.render()
        
        clock.tick(60)
        pg.display.flip()

if __name__ == '__main__':
    main()
    
    
# NOTES: 2 ways to change color:
#     1. simple: fill the logo with blend mode (after some times, it will blend to white -> no more color changes)
#     2. replace pixel array