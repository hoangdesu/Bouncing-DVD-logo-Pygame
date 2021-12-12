from DVD import *
# from DVD_backgroud import *

def main():
    pg.init()
    
    window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Pygame - Bouncing DVD logo")
    
    dvd = DVD(window)
    pg.display.set_icon(dvd.logo)
    
    # 1 for foreground color change (default), 2 for background color change
    option = 1
    if option == 2:
        dvd.logo = pg.transform.smoothscale(dvd.sprite, (dvd.width, dvd.height)) 
        dvd.color = (0, 0, 0, 0)
        
    clock = pg.time.Clock()
    
    running = True
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
