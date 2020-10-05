import pygame
from pygame.draw import *
from math import pi
from math import sin, cos
 
pygame.init()
 
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (130 , 150, 140)
ORANGE = (220, 140, 50)
GREEN = (50, 220, 140)
BLUE = (30, 180, 250)

screen = pygame.display.set_mode((600, 800))

 
def dog_head(x, y, k):
    
    '''
    Функция рисует собачью голову.
    x - координата ее левого уха по оси оХ
    у - координата ее левого уха по осе оУ
    k - коэффициент, отвечающий за ее размер. 
    При k = 1 голова будет 90х90 пикселей
    '''
        #border
    pygame.draw.rect(screen, BLACK, (x - 1, y - 1, 90*k + 2, 90*k + 2))
        #scale
    pygame.draw.rect(screen, GRAY, (x, y, 90*k, 90*k))
    #ears
        #border
    pygame.draw.ellipse(screen, BLACK, (x - 10*k, y, 25*k + 2, 35*k + 2))
        #leaft ear
    pygame.draw.ellipse(screen, GRAY, (x - 10*k + 1, y + 1, 25*k, 35*k))
        #border
    pygame.draw.ellipse(screen, BLACK, (x - 10*k + 85*k, y, 25*k + 2, 35*k + 2))
        #right ear
    pygame.draw.ellipse(screen, GRAY, (x - 10*k + 1 + 85*k, y + 1, 25*k, 35*k)) 
    #eyes
        #border
    pygame.draw.ellipse(screen, BLACK, (x + 20*k - 1, y + 30*k - 1, 17*k + 2, 10*k + 2))
        #left eye
    pygame.draw.ellipse(screen, WHITE, (x + 20*k, y + 30*k, 17*k, 10*k))
        #left eye dot
    pygame.draw.ellipse(screen, BLACK, (x + 53*k - 1, y + 30*k - 1, 17*k + 2, 10*k + 2))
        #border
    pygame.draw.ellipse(screen, WHITE, (x + 53*k, y + 30*k, 17*k, 10 *k))
        #right eye
    pygame.draw.ellipse(screen, BLACK, (x + 23.5*k, y + 30.5*k, 10*k, 10*k))
        #right eye dot
    pygame.draw.ellipse(screen, BLACK, (x + 56*k, y + 30.5*k, 10*k, 10*k))
    #mouth
        #-smile
    pygame.draw.arc(screen, BLACK, (x + 20*k, y + 55*k, 50*k, 50*k), pi / 8, 7*pi / 8, 5)
        #border
    pygame.draw.polygon(screen, BLACK, ( [x + 27*k, y + 62*k],
                                             [x + 37*k, y + 56*k], 
                                             [x + 35.5*k, y + 43.5*k]))
        #left tooth
    pygame.draw.polygon(screen, WHITE, ( [x + 29*k, y + 60*k],
                                                   [x + 36.5*k, y + 56.5*k],
                                                   [x + 35*k, y + 45*k] ))
        #border
    pygame.draw.polygon(screen, BLACK, ( [x + 50.5*k, y + 56.5*k],
                                             [x + 61.5*k, y + 62.5*k],
                                             [x + 52*k, y + 44*k]))
        #right tooth
    pygame.draw.polygon(screen, WHITE, ( [x + 51.5*k, y + 55.5*k],
                                                   [x + 59.5*k, y + 60.5*k],
                                                   [x + 52.5*k, y + 45*k]))
 
def dog_right(x, y, k):
    '''
    Функция рисует собаку, тело которой расположено справа относительно головы.
    x, y - координаты, использованные ранее в функции dog_head
    k - коэффициент, отвечающий за размер тела.
    При k = 1 тело соотносится с размерами головы
    так же, как это выглядит на авторском рисунке.
    '''
        #shoulders
    pygame.draw.ellipse(screen, GRAY, (x + 20*k, y + 40*k, 150*k, 90*k))
        #left leg
    pygame.draw.ellipse(screen, GRAY, (x - 15*k, y + 50*k, 50*k, 120*k))
    pygame.draw.ellipse(screen, GRAY, (x - 30*k, y + 160*k, 60*k, 20*k))
        #right leg
    pygame.draw.ellipse(screen, GRAY, (x + 70*k, y + 70*k, 50*k, 120*k))
    pygame.draw.ellipse(screen, GRAY, (x + 55*k, y + 180*k, 60*k, 20*k))
        #buttlock
    pygame.draw.ellipse(screen, GRAY, (x + 130*k, y + 40*k, 110*k , 70*k)) 
    pygame.draw.ellipse(screen, GRAY, (x + 140*k, y + 35*k, 40*k, 60*k))
        #right leg - back
    pygame.draw.ellipse(screen, GRAY, (x + 155*k, y + 85*k, 20*k, 60*k))
    pygame.draw.ellipse(screen, GRAY, (x + 140*k, y + 140*k, 30*k, 15*k))
        #left leg - back
    pygame.draw.ellipse(screen, GRAY, (x + 190*k, y + 70*k , 50*k, 50*k))
    pygame.draw.ellipse(screen, GRAY, (x + 210*k, y + 90*k, 20*k, 60*k))
    pygame.draw.ellipse(screen, GRAY, (x + 195*k, y + 145*k, 30*k, 15*k))
    
    dog_head(x, y, k)
    
def dog_left(x, y, k):
    '''
    Функция рисует собаку, тело которой расположено слева относительно головы.
    x, y - координаты, использованные ранее в функции dog_head
    k - коэффициент, отвечающий за размер тела. 
    При k = 1 тело соотносится с размерами головы
    так же, как это выглядит на авторском рисунке.
    '''   
        #shoulders
    pygame.draw.ellipse(screen, GRAY, (x - 90*k, y + 40*k, 150*k, 90*k))
        #left leg
    pygame.draw.ellipse(screen, GRAY, (x + 50*k, y + 40*k, 50*k, 120*k)) 
    pygame.draw.ellipse(screen, GRAY, (x + 50*k, y + 150*k, 60*k, 20*k))
        #right leg
    pygame.draw.ellipse(screen, GRAY, (x - 20*k, y + 60*k, 50*k, 120*k))
    pygame.draw.ellipse(screen, GRAY, (x - 20*k, y + 160*k, 60*k, 20*k))
        #buttlock
    pygame.draw.ellipse(screen, GRAY, (x - 135*k, y + 50*k, 110*k , 70*k)) 
    pygame.draw.ellipse(screen, GRAY, (x - 90*k, y + 40*k, 40*k, 60*k))
        #right leg - back
    pygame.draw.ellipse(screen, GRAY, (x - 135*k, y + 95*k, 20*k, 60*k))
    pygame.draw.ellipse(screen, GRAY, (x - 130*k, y + 145*k, 30*k, 15*k))
        #left leg - back
    pygame.draw.ellipse(screen, GRAY, (x - 150*k, y + 70*k , 50*k, 50*k)) 
    pygame.draw.ellipse(screen, GRAY, (x - 80*k, y + 90*k, 20*k, 60*k))
    pygame.draw.ellipse(screen, GRAY, (x - 75*k, y + 140*k, 30*k, 15*k))
    
    dog_head(x, y, k)
 
def kennel(x, y, k):
    '''
    Функция рисует кануру.
    x,y - координаты левого нижнего угла картинки.
    k - коэффициент, отвечающий за размер картинки.
    При k = 1 размер 190x275 пикселей. 
    '''
        #walls and roof
    pygame.draw.polygon(screen, ORANGE, [(x, y), (x, y - 100*k),
                                                 (x + 100*k, y - 70*k),
                                                 (x + 100*k, y + 30*k)], 0)
    pygame.draw.polygon(screen, ORANGE, [(x + 100*k, y + 30*k),
                                                 (x + 100*k, y - 70*k),
                                                 (x + 150*k, y - 100*k),
                                                 (x + 150*k, y)], 0)
    pygame.draw.polygon(screen, BLACK, [(x, y), (x, y - 100*k),
                                            (x + 100*k, y - 70*k),
                                            (x + 100*k, y + 30*k)], 2)
    pygame.draw.polygon(screen, BLACK, [(x + 100*k, y + 30*k),
                                            (x + 100*k, y - 70*k),
                                            (x + 150*k, y - 100*k),
                                            (x + 150*k, y)], 2)
    pygame.draw.polygon(screen, ORANGE, [(x, y - 100*k),
                                                 (x + 75*k, y - 175*k),
                                                 (x + 100*k, y - 70*k)], 0)
    pygame.draw.polygon(screen, ORANGE, [(x + 100*k, y - 70*k), 
                                                 (x + 75*k, y - 175*k),
                                                 (x + 110*k, y - 185*k),
                                                 (x + 150*k, y - 100*k)], 0)
    pygame.draw.polygon(screen, BLACK, [(x + 100*k, y - 70*k),
                                            (x + 75*k, y - 175*k),
                                            (x + 110*k, y - 185*k),
                                            (x + 150*k, y - 100*k)], 2)
    pygame.draw.polygon(screen, BLACK, [(x, y - 100*k), 
                                            (x + 75*k, y - 175*k),
                                            (x + 100*k, y - 70*k)], 2)
        #door
    pygame.draw.ellipse(screen, BLACK, (x + 30*k, y - 50*k, 50*k, 50*k))

def fence(x, y, n):
    '''
    Функция рисует забор.
    x,y - координаты левого верхнего угла левой планки.
    n - количество планок.
    '''
    for i in range(n):
        pygame.draw.polygon(screen, ORANGE, [(x + 50*i, y),
                                                     (x + 50 * (i + 1), y),
                                                     (x + 50 * (i + 1), y + 200), 
                                                     (x + 50 * i, y + 200)], 0)
        pygame.draw.polygon(screen, BLACK, [(x + 50 * i, y), (x + 50 * (i + 1), y),
                                                (x + 50 * (i + 1), y + 200),
                                                (x + 50 * i, y + 200)], 2) 
                                             
# draw background
pygame.draw.rect(screen, GREEN, (0, 0, 600, 800)) #grass
pygame.draw.rect(screen, BLUE, (0, 0, 600, 350)) #sky

'''
В этой области идет работа с описанными выше функциями.
'''
 
fence(310, 150, 7)
fence(-37, 170, 7)
fence(190, 90, 10)
fence(-25, 100, 7)
fence(0, 50, 10)
 
dog_right(400, 350, 0.7)
 
kennel(250, 500, 1)
 
dog_left(150, 550, 1)
 
dog_left(50, 400, 0.7)

dog_right(300, 500, 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
 
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
 
pygame.quit()