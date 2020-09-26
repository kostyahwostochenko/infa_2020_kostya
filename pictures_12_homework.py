import pygame
from pygame.draw import *

pygame.init()

# Size of screen
x = 550
y = 800

FPS = 30
WHITE = (255, 255, 255)
BLUE = (129, 239, 247)
GRAY = (158, 168, 168)
DARKGREEN = (27, 181, 43)
LIGHTGREEN = (124, 242, 135) 
PURPLE = (237, 97, 250)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((x, y))

# Draw petal for flower in the specified coordinates and scale.  
def petal(coordinate_x, coordinate_y, long_ellipse_x, long_ellipse_y, surf):
    # hereinafter we will use the simplification of writing long variables 
    # in functions to a, b, c, d
    a = coordinate_x
    b = coordinate_y
    c = long_ellipse_x
    d = long_ellipse_y
    pi = 3.14
    ellipse(surf, WHITE, (a, b, c, d))
    arc(surf, BLACK, (a, b, c, d), 0, 2*pi) 


# Draw one flower in the specified coordinates and scale.  
def flower(coordinate_x, coordinate_y, scale, angle):
    a = coordinate_x
    b = coordinate_y
    c = scale
    i = a - c*x/35
    j = b - c*y/60
    surface = pygame.Surface((c*x/11, c*y/20))
    surface.fill(DARKGREEN)
    ellipse(surface, (255, 255, 0), (a-i, b-j, c*x/27, c*y/64))
    petal(a + c*x/1000 - i, b - c*y/100 - j, c*x/27, c*y/64, surface) 
    petal(a + c*x/65 - i, b - c*y/175 - j, c*x/27, c*y/64, surface)
    petal(a + c*x/45 - i, b + c*y/400 - j, c*x/27, c*y/64, surface)
    petal(a + c*x/70 - i, b + c*y/70 - j, c*x/27, c*y/64, surface)
    petal(a - c*x/60 - i, b + c*y/80 - j, c*x/27, c*y/64, surface)
    petal(a - c*x/35 - i, b + c*y/250 - j, c*x/27, c*y/64, surface)
    petal(a - c*x/45 - i, b - c*y/175 - j, c*x/27, c*y/64, surface)
    screen.blit(pygame.transform.rotate(surface, angle), (a - c*x/9, b - c*y/16))


# Draw five flowers in flower bed in the specified coordinates and scale.  
def flowers(coordinate_x, coordinate_y, scale):
    a = coordinate_x
    b = coordinate_y
    c = scale
    ellipse(screen, DARKGREEN, (a - c*x/6, b - c*y*11/90, c*x/3, c*x/3))
    flower(a + c*x/18, b + c*y/11, c, -20)
    flower(a + c*x/7, b + c*y/30, c, -50)
    flower(a - c*x/25, b + c*y/30, c*9/10, 20)
    flower(a - c*x/40, b - c*y/30, c*4/5, 20)
    flower(a + c*x/10, b - c*y/30, c*9/10, -10)  


# Draw leg of lama in the specified coordinates and scale.  
def leg(coordinate_x, coordinate_y, scale):
    a = coordinate_x
    b = coordinate_y
    c = scale
    ellipse(screen, WHITE, (a, b, c*x/43, c*y/30))
    ellipse(screen, WHITE, (a, b + c*y/34, c*x/43, c*y/30))
    ellipse(screen, WHITE, (a + c*x/200, b + c*y/17, c*x/37, c*y/90))


# Draw lama in the specifield coordinates and scale.  
def lama(coordinate_x, coordinate_y, scale):
    a = coordinate_x
    b = coordinate_y
    c = scale
    # Draw body.  
    ellipse(screen, WHITE, (a, b, c*x/4, c*y/14))
    # Draw neck.  
    ellipse(screen, WHITE, (a + c*x*19/100, b - c*y/12, c*x/16, c*y/8))
    # Draw head.                            
    ellipse(screen, WHITE, (a + c*x*19/100, b - c*y/9, c*x/10, c*y/23))
    # Draw eye.  
    ellipse(screen, PURPLE, (a + c*x*213/1000, b - c*y*105/1000, c*y/32, c*y/40))                
    ellipse(screen, BLACK, (a + c*x*232/1000, b - c*y*100/1000, c*y/65, c*y/70))
    ellipse(screen, WHITE, (a + c*x*225/1000, b - c*y*100/1000, c*x/60, c*y/120)) 
    # Draw ears.  
    polygon(screen, WHITE, [[a + c*x*210/1000, b - c*y*105/1000],
                            [a + c*x*20/100, b - c*y*122/1000],
                            [a + c*x*221/1000, b - c*y*1095/10000]]) 
                           
    polygon(screen, WHITE, [[a + c*x*194/1000, b - c*y*92/1000],
                            [a + c*x*17/100, b - c*y*118/1000],
                            [a + c*x*205/1000, b - c*y*100/1000]])
    
    leg(a + c*x/45, b + c*y/33, 9*c/5)
    leg(a + c*x/7, b + c*y/33, 9*c/5)
    leg(a + c*x/13, b + c*y/18, 9*c/5)
    leg(a + 183*c*x/1000, b + c*y/18, 9*c/5)
  
    
# Draw flipped leg of lama in the specified coordinates and scale.  
def legflipped(coordinate_x, coordinate_y, scale):
    a = coordinate_x
    b = coordinate_y
    c = scale
    ellipse(screen, WHITE, (a, b, c*x/43, c*y/30))
    ellipse(screen, WHITE, (a, b + c*y/34, c*x/43, c*y/30))
    ellipse(screen, WHITE, (a - c*x/200, b + c*y/17, c*x/37, c*y/90))  
    
  
# Draw flipped lama in the specifield coordinates and scale.  
def lamaflipped(coordinate_x, coordinate_y, scale):
    a = coordinate_x
    b = coordinate_y
    c = scale
    # Draw body.  
    ellipse(screen, WHITE, (a, b, c*x/4, c*y/14))
    # Draw neck.  
    ellipse(screen, WHITE, (a - c*x/1000, b - c*y/12, c*x/16, c*y/8))
    # Draw head.                            
    ellipse(screen, WHITE, (a - c*x*33/1000, b - c*y/9, c*x/10, c*y/23))
    # Draw eye.  
    ellipse(screen, PURPLE, (a - c*x/1000, b - c*y*105/1000, c*y/32, c*y/40))                
    ellipse(screen, BLACK, (a + c*x/200, b - c*y*100/1000, c*y/65, c*y/70))
    ellipse(screen, WHITE, (a + c*x*15/1000, b - c*y*100/1000, c*x/60, c*y/120)) 
    # Draw ears.  
    polygon(screen, WHITE, [[a + c*x*45/1000, b - c*y*97/1000],
                            [a + c*x*55/1000, b - c*y*127/1000],
                            [a + c*x*36/1000, b - c*y*1050/10000]]) 
                           
    polygon(screen, WHITE, [[a + c*x*65/1000, b - c*y*92/1000],
                            [a + c*x*70/1000, b - c*y*118/1000],
                            [a + c*x*50/1000, b - c*y*100/1000]])
    
    legflipped(a + c*x/45, b + c*y/33, 9*c/5)
    legflipped(a + c*x/7, b + c*y/33, 9*c/5)
    legflipped(a + c*x/13, b + c*y/18, 9*c/5)
    legflipped(a + 183*c*x/1000, b + c*y/18, 9*c/5)
    
    
# Draw background.  
rect(screen, GRAY, (0, 0, x, y))

polygon(screen, LIGHTGREEN, [[0, y/2], [10*x/18, y/2], [10*x/18, 3*y/5],
                             [x, 3*y/5], [x, y], [0, y]])

aalines(screen, LIGHTGREEN, True,  [[0, y/2], [10*x/18, y/2], [10*x/18, 3*y/5],
                                    [x, 3*y/5], [x, y], [0, y]])

polygon(screen, BLUE, [[0, y/4], [x/8, y/16], [x/4, 3*y/16], [3*x/8, y/8],
                       [29*x/40, 3*y/8], [17*x/20, 5*y/64], [9*x/10, y/8],
                       [x, y/32], [x, 0], [0, 0]])

aalines(screen, BLUE, True, [[0, y/4], [x/8, y/16], [x/4, 3*y/16],
                             [3*x/8, y/8], [29*x/40, 3*y/8], [17*x/20, 5*y/64],
                             [9*x/10, y/8], [x, y/32], [x, 0], [0, 0]])


flowers(x, 95*y/100, 1/2)
flowers(95*x/100, 75*y/100, 3/4)
flowers(75*x/100, 90*y/100, 65/100)
flowers(93*x/100, 59*y/100, 1/2)
flowers(75*x/100, 63*y/100, 1/4)
flowers(3*x/100, 52*y/100, 1/4)

lama(-1*x/3, 95*y/100, 2)
lama(x/5, 6*y/10, 1/2)
lama(4*x/10, 5*y/10, 1/2)
lamaflipped(87*x/100, 7*y/10, 1)
lamaflipped(50*x/100, 68*y/100, 1/2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
