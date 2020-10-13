'''
Правила игры:

    Ваша задача набрать как можно больше очков за время игры уничтожая шарики
    (нажимая на них мышкой). Игра заканчивается тогда, когда количество ошибок
    становится равным hightmistakes. 
    
    В игре существует два типа объектов: 
        1) обычные шарики, которые бывают случайных цветов, размеров и имеют
           разные скорости, в том числе могут и стоять. За их уничтожение
           игроку дается одно очко.
           
        2) "уничтожители" - маленькие белые шарики, которые будут пытаться
           уничтожить обычные шарики, при этом у вас будет возрастать 
           количество ошибок. Их можно уничтожать так же как и обычные шарики.
           При этом за их уничтожение будет даваться 2 очка. Они появляются
           каждый раз, когда ваш счет становится кратным 3 (с учетом счета 0).
           И при каждом их появлении они будут становиться все быстрее и
           быстрее, что будет затруднять игру. При столкновении с обычным
           шариком увеличивают количество ошибок на 1.
           
    Режим игры hardmode.
        Суть его в том, что при его активации будетучитываться столкновение
        обычных шариков друг с другом, т.е. они будутуничтожаться при
        столкновении, а количество ваших ошибок будет возрастатьна 1.
        Для активации данного режима необходимо переменной hardmode присвоить
        значение True. Для деактивации - False. Данная переменная находится
        в начале программы.
        
    Музыкальное сопровождение может быть отключено при необходимости. Для
    этого необходимо переменной soundmode присвоить значение False. Переменная
    находится в начале программы.
'''

import pygame
from pygame.draw import *
from random import randint
import random
from pygame.mixer import *
pygame.init()

# Количество обновлений экрана в секунду и размеры экрана
FPS = 30
width = 1000
height = 800

hightmistakes = 100                # Максимальное количество ошибок
number = 5                         # Количество обычных шаров на экране

minballrad = 20                    # Минимальный радиус шара
maxballrad = 50                    # Максимальный радиус шара
maxspeedx = 5                      # Максимальная скорость шара по x
maxspeedy = 5                      # Максимальная скоорость по y
raddistroyer = 10                  # Радиус "уничтожителя"
startspeedx = 2                    # Начальная скорость "уничтожителя" по x
startspeedy = 2                    # Начальная скорость "уничтожителя" по y
scoreball = 1                      # Кол-во очков за уничтожение одного шарика
scoredestroyer = 2                 # Кол-во очков за уничтожение "уничтожителя"
costmisclick = 1                   # Насколько возрастает кол-во ошибок при промахе
costdestroy = 1                    # Насколько возрастает кол-во ошибок когда 
                                   #уничтожитель уничтожает шарик

hardmode = False                    # Активация hardmode
soundmode = True                    # Активация звукого сопровождения

score = 0
mistakes = 0
click = False
a = []
b = []
screen = pygame.display.set_mode((width, height))

pygame.mixer.music.load('sound0.wav') 
sound1 = pygame.mixer.Sound('sound1.wav')
sound2 = pygame.mixer.Sound('sound2.wav')
sound3 = pygame.mixer.Sound('sound3.wav')
sound4 = pygame.mixer.Sound('sound4.wav')
sound5 = pygame.mixer.Sound('sound5.wav')
sound6 = pygame.mixer.Sound('sound6.wav')
sound7 = pygame.mixer.Sound('sound7.wav')
SOUND = [sound1, sound2, sound3, sound4, sound5, sound6, sound7]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (234, 0, 255)
LIGHTBLUE = (0, 196, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, PURPLE, LIGHTBLUE]


def balls(i):
    '''
    Функция создает шарики со случайными параметрами в начале программы
    i - количество шариков
    '''
    global a
    for g in range (0, 6*i):
        if (g%6 == 0):
            a.append(randint(width//6, 5*width//6))
        if  g%6 == 1:
            a.append(randint(height//6, 5*height//6))
        if g%6 == 2:
            a.append(randint(minballrad, maxballrad))
        if g%6 == 3:
            a.append(randint(-1*maxspeedx, maxspeedx))
        if g%6 == 4:
            a.append(randint(-1*maxspeedy, maxspeedy))
        if g%6 == 5:
            a.append(COLORS[randint(0, 7)])
        
      
def move(i):
    '''
    Функция отвечает за перемещение шариков по экрану.
    i - количество шариков, которое есть на экране
    '''
    global a
    for k in range (0, i):
        pygame.draw.circle(screen, a[6*k + 5], (a[6*k], a[6*k + 1]), a[6*k + 2])
        a[6*k] = a[6*k] + a[6*k + 3]
        a[6*k + 1] = a[6*k + 1] + a[6*k + 4]
        if a[6*k] >= width-a[6*k + 2] or a[6*k] <= a[6*k + 2]:
            a[6*k + 3] = -1*a[6*k + 3]
        if a[6*k + 1] >= height-a[6*k + 2] or a[6*k + 1] <= a[6*k + 2]:
            a[6*k + 4] = -1*a[6*k + 4]
        pygame.draw.circle(screen, a[6*k + 5], (a[6*k], a[6*k + 1]), a[6*k + 2])
   

def create(k):
    '''
    Функция создает шарик во время выполнения основной части программы.
    Отличается от функции balls() тем, что просто перезаписывает параметры
    шарика в уже имеющемся списке.
    k - номер шарика, который необходимо поменять, принадлежит [0, number)
    '''
    a[6*k] = randint(width//6, 5*width//6)
    a[6*k + 1] = randint(height//6, 5*height//6)
    a[6*k + 2] = randint(minballrad, maxballrad)
    a[6*k + 3] = randint(-1*maxspeedx, maxspeedx)
    a[6*k + 4] = randint(-1*maxspeedy, maxspeedy)
    a[6*k + 5] = COLORS[randint(0, 7)]
    pygame.draw.circle(screen, a[6*k + 5], (a[6*k], a[6*k + 1]), a[6*k + 2])           

        
def count(i):
    '''
    Функция считает количество очков при попадании мышкой в обычный шарик
    i - количество шариков
    '''
    global a
    global score
    global mistakes
    global click
    t = score
    checkscore = True
    for k in range (0, i):
        if ((event.pos[0] - a[6*k])**2 + (event.pos[1] - a[6*k + 1])**2 <= 
            a[6*k + 2]**2):
            if checkscore == True:
                score += scoreball
                checkscore = False
            create(k)
            click = True
            if soundmode == True:
                SOUND[randint(0, 6)].play()
    if score == t:
        mistakes += costmisclick
        

def collision(i):
    '''
    При активации hardmode данная функция отвечает за уничтожение обычных
    шариков при их столкноввении друг с другом.
    i - количество шариков
    '''
    global a
    global score
    global mistakes
    for k in range (0, i-1):
        for j in range (k+1, i):
            if (((a[6*k] - a[6*j])**2 + (a[6*k + 1] - a[6*j + 1])**2) <= 
                (a[6*k + 2] + a[6*j + 2])**2):
                create(k)
                create(j)
                mistakes += costmisclick
                print('Ваш счёт',score,'количество ошибок',mistakes)
                    

def createdestroyer():
    '''
    Функция создает объект уничтожитель (маленький белый шарик,
                                         который уничтожает обычные)
    '''
    global b
    b.append(width//2)
    b.append(height//2) 
    b.append(0)
    b.append(width//2)
    b.append(height//2) 
    b.append(0)
    

def movedestroyer(i):
    '''
    Функция отвечает за перемещение уничтожителя по направлению
    к ближайшему обычному шарику.
    i - количество обычных шариков
    '''
    global a
    global b
    global score
    for j in range(0, score//3+1):
        if b[3*j + 2] != -1:
            pygame.draw.circle(screen, WHITE, (b[3*j], b[3*j + 1]), raddistroyer)
            minr = (a[0] - b[3*j])**2 + (a[1] - b[3*j + 1])**2
            x = a[0]
            y = a [1]
            for k in range(0, i):
                if ((a[6*k] - b[3*j])**2 + (a[6*k + 1] - b[3*j + 1])**2) <= minr:
                    minr = (a[6*k] - b[3*j])**2 + (a[6*k + 1] - b[3*j + 1])**2
                    x = a[6*k]
                    y = a[6*k + 1]
                    b[3*j + 2] = k
            if x>=b[3*j]:
                b[3*j] = b[3*j] + startspeedx + score//3
            if x<b[3*j]:
                b[3*j] = b[3*j] - startspeedx - score//3
            if y>=b[3*j + 1]:
                b[3*j + 1] = b[3*j + 1] + startspeedy + score//3
            if y<b[3*j + 1]:
                b[3*j + 1] = b[3*j + 1] - startspeedy - score//3
            pygame.draw.circle(screen, WHITE, (b[3*j], b[3*j + 1]), raddistroyer)
                
                
def destroy():
    '''
    Функция уничтожает обычный шарик при соприкосновении его с уничтожителем
    '''
    global a
    global b
    global score
    global mistakes
    for j in range(0, score//3+1):
        h = b[3*j + 2]
        if (((a[6*h] - b[3*j])**2 + (a[6*h + 1] - b[3*j + 1])**2) <= 
            (raddistroyer + a[6*h + 2])**2) :
            create(h)
            mistakes += costdestroy
            print('Ваш счёт',score,'количество ошибок',mistakes)
   

def destroydestroyer():
    '''
    Функция уничтожает маленький белый шарик при нажатии на него
    '''
    global b
    global score
    global mistakes
    checkmistakes = True
    for j in range(0, score//3 + 1):
        if ((event.pos[0] - b[3*j])**2 + (event.pos[1] - b[3*j + 1])**2 <= 
            raddistroyer**2):
            b[3*j] = -20
            b[3*j + 1] = -20
            b[3*j + 2] = -1
            score += scoredestroyer
            if checkmistakes == True:
                mistakes -= costmisclick
                checkmistakes = False
    print('Ваш счёт',score,'количество ошибок',mistakes)
if soundmode == True:  
    pygame.mixer.music.play(-1)
createdestroyer()          
balls(number)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
           count(number)
           if (score % 3 == 0) and (click == True):
               createdestroyer()
               click = False
           destroydestroyer()
    movedestroyer(number)
    destroy()  
    move(number)          
    pygame.display.update()
    screen.fill(BLACK)
    
    if hardmode == True:
        collision(number)
        
    if mistakes >= hightmistakes:
        print('Игра окончена')
        finished = True
        
pygame.quit()
