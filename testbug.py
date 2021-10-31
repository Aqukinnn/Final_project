import cv2
import numpy as np
import time
import PoseModule as pm

import pygame
import sys
import time
from pygame.locals import *

from time import time, sleep

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (50,50,50)

W = 1280
H = 720
#if only for loading screen....
#def load_screen(next_pose):

#if for loading screen while display score
#def load_screen(next_pose,time)
def load_screen(minutes,seconds):
    pygame.init()
    mainClock = pygame.time.Clock()

    timer1 = minutes
    timer2 = seconds

    time_out = float(15)
    Fake_time_out = int(0)

    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Loading...')

    bg_img = pygame.image.load('img/ojou.jpg')

    game = True
    clock = pygame.time.Clock()
    done  = True
    count_time = 0
    

    while game == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        screen.blit(bg_img,(0,0))



        Font = pygame.font.SysFont('Roboto-Bold', 100)
        color = GRAY
        Fake_time_out = int(time_out)
        text = Font.render(f'Time left {Fake_time_out} seconds',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5 / 5)
        Surface.blit(text, text_rect)

        pygame.display.flip()
        mainClock.tick(100000)

        if done:
            count_time += 1
            if count_time > 100 * 9:
                ##hight_scoretime
                game = False
               
                   
            else:
                continue




load_screen(1,20)
pygame.quit()
quit()