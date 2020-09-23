import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen,(195, 199, 179),(0,0,400,400))
circle(screen,(203, 252, 5),(200,200),100)
rect(screen,(0,0,0),(150,240,100,20))

circle(screen, (0,0,0), (240,170), 8)
circle(screen,(255,0,0),(240,170),15,7)
circle(screen,(0,0,0),(240,170),16,1)

circle(screen, (0,0,0), (160,170), 12)
circle(screen,(255,0,0),(160,170),26,14)
circle(screen,(0,0,0),(160,170),26,1)

polygon(screen,(0,0,0),([217,170],[256,135],[248,127],[210,162]))
aalines(screen,(0,0,0),True,([217,170],[256,135],[248,127],[210,162]))

polygon(screen, (0,0,0), [[180,153], [130,110], [140,100], [190,143]])
aalines(screen, (0,0,0), True, ([180,153], [130,110], [140,100], [190,143]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

