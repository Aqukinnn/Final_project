#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| *_* |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \|     |// '.
#                  / \|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
import cv2
import numpy as np
import PoseModule as pm

import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

import os
import pygame
import sys
import time
from pygame.locals import *

bg_img = pygame.image.load('img/main.jpg')
creator_img = pygame.image.load('img/bg_creator.jpg')

#setting bg 
bg1_sample = pygame.image.load('img/1sample.jpg')
bg2_sample = pygame.image.load('img/2sample.jpg')
bg3_sample = pygame.image.load('img/3sample.jpg')
logo = pygame.image.load('img/ku-logo.jpg')
Tee = pygame.image.load('img/Tee.jpg')
Pooh = pygame.image.load('img/Pooh.jpg')
Teacher = pygame.image.load('img/Teacher.jpg')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (50,50,50)

W = 1280
H = 720


def main_menu(set):
    bg_set = set
    
    pygame.init()
    mainClock = pygame.time.Clock()
    #all_fonts = pygame.font.get_fonts()
    #Font = pygame.font.SysFont('arial', 20)
    ##W = 1280
    ##H = 720

    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('EXERCISE') 

    ##def text_print(text,color1,color2,left,top,Font=basicFont):
    ##    text = Font.render(text,True,color1,color2)
    ##    text_rect = text.get_rect()
    ##    text_rect.top = top
    ##    text_rect.left = left
    ##    Surface.blit(text, text_rect)
    game = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    text5_bool = False
    text6_bool = False
    text7_bool = False
    text8_bool = False

    
    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos


        screen.blit(bg_img,(0,0))

        Font = pygame.font.SysFont('Roboto-Bold', 100)
        color = WHITE
        text = Font.render('WELCOME TO CAMERA EXERCISES',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5 / 5)
        Surface.blit(text, text_rect)

        ##Besic start label
        Font = pygame.font.SysFont('Roboto-Bold', 100)
        color = WHITE
        text = Font.render('Select options',True,color)
        text_rect = text.get_rect()
        text_rect.center = (280,H * 1.1 / 5)
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('Basic start ( recommended for beginner )',True,color)
        text_rect = text.get_rect()
        text_rect.center = (370,H * 1.7/ 5)
        if text_rect.collidepoint(mouse_click):
            #pygame.quit()
            choice(set)
            #camera("FOREARMS", 5)
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = GREEN
        
        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('Butt Kicks',True,color)
        text_rect = text.get_rect()
        text_rect.center = (125,H * 2.1 / 5)
        if text_rect.collidepoint(mouse_click):
            chooseamount("leg_back", set)
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text4_bool:
            color = GREEN
            
        
        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('High Knee',True,color)
        text_rect = text.get_rect()
        text_rect.center = (125,H * 2.5 / 5)
        if text_rect.collidepoint(mouse_click):
            chooseamount("leg_front", set)
        if text_rect.collidepoint(mouse_pos):
            text4_bool = True
        else:
            text4_bool = False
        Surface.blit(text, text_rect)

        color = WHITE

        if text5_bool:
            color = GREEN
            
        
        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('Biceps Curls',True,color)
        text_rect = text.get_rect()
        text_rect.center = (143,H * 2.9 / 5)
        if text_rect.collidepoint(mouse_click):
            chooseamount("FOREARMS", set)
        if text_rect.collidepoint(mouse_pos):
            text5_bool = True
        else:
            text5_bool = False
        Surface.blit(text, text_rect)

        color = WHITE

        if text6_bool:
            color = GREEN
            
        
        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('Lateral Raise',True,color)
        text_rect = text.get_rect()
        text_rect.center = (148,H * 3.3 / 5)
        if text_rect.collidepoint(mouse_click):
            chooseamount("BACKARMS", set)
        if text_rect.collidepoint(mouse_pos):
            text6_bool = True
        else:
            text6_bool = False
        Surface.blit(text, text_rect)

        color = WHITE

        if text7_bool:
            color = GREEN


        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('Setting',True,color)
        text_rect = text.get_rect()
        text_rect.center = (100,H * 3.7 / 5)
        if text_rect.collidepoint(mouse_click):
            setting()
        if text_rect.collidepoint(mouse_pos):
            text7_bool = True
        else:
            text7_bool = False
        Surface.blit(text, text_rect)

        color = WHITE

        if text8_bool:
            color = GREEN


        Font = pygame.font.SysFont('Roboto-Bold', 50)
        text = Font.render('About US',True,color)
        text_rect = text.get_rect()
        text_rect.center = (115,H * 4.1 / 5)
        if text_rect.collidepoint(mouse_click):
            creator()
        if text_rect.collidepoint(mouse_pos):
            text8_bool = True
        else:
            text8_bool = False
        Surface.blit(text, text_rect)

        
        pygame.display.flip()
        mainClock.tick(100000)


def setting():
    pygame.init()
    mainClock = pygame.time.Clock()
    #all_fonts = pygame.font.get_fonts()
    #Font = pygame.font.SysFont('arial', 20)


    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('EXERCISE')

    ##bg_img = pygame.image.load('img/ojou.jpg')

    ##def text_print(text,color1,color2,left,top,Font=basicFont):
    ##    text = Font.render(text,True,color1,color2)
    ##    text_rect = text.get_rect()
    ##    text_rect.top = top
    ##    text_rect.left = left
    ##    Surface.blit(text, text_rect)
    game = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    text5_bool = False
 

    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos


        screen.blit(bg_img,(0,0))

        screen.blit(bg1_sample, (120,H * 1.8/ 5))
        screen.blit(bg2_sample, (490,H * 1.8/ 5))
        screen.blit(bg3_sample, (850,H * 1.8/ 5))

        Font = pygame.font.SysFont('Roboto-Bold', 50)
        color = WHITE
        text = Font.render('Choose background images while your exercising',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5 / 5)
        Surface.blit(text, text_rect)

        color = WHITE
        text = Font.render('Fountain',True,color)
        text_rect = text.get_rect()
        text_rect.center = (270,H * 1.5/ 5)
        Surface.blit(text, text_rect)

        color = WHITE
        text = Font.render('SideWalk',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 1.5/ 5)
        Surface.blit(text, text_rect)

        color = WHITE
        text = Font.render('Park',True,color)
        text_rect = text.get_rect()
        text_rect.center = (1000,H * 1.5/ 5)
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Select',True,color)
        text_rect = text.get_rect()
        text_rect.center = (270,H * 3.4/ 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(1)
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Select',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3.4/ 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(2)
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text4_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Select',True,color)
        text_rect = text.get_rect()
        text_rect.center = (1000,H * 3.4/ 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(3)
        if text_rect.collidepoint(mouse_pos):
            text4_bool = True
        else:
            text4_bool = False
        Surface.blit(text, text_rect)


        color = WHITE
        if text5_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Back',True,color)
        text_rect = text.get_rect()
        text_rect.center = (110,H * 4.2 / 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(set)
        if text_rect.collidepoint(mouse_pos):
            text5_bool = True
        else:
            text5_bool = False
        Surface.blit(text, text_rect)

        pygame.display.flip()
        mainClock.tick(100000)

def creator():
    pygame.init()
    mainClock = pygame.time.Clock()
    #all_fonts = pygame.font.get_fonts()
    #Font = pygame.font.SysFont('arial', 20)


    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('EXERCISE')

    ##bg_img = pygame.image.load('img/ojou.jpg')

    ##def text_print(text,color1,color2,left,top,Font=basicFont):
    ##    text = Font.render(text,True,color1,color2)
    ##    text_rect = text.get_rect()
    ##    text_rect.top = top
    ##    text_rect.left = left
    ##    Surface.blit(text, text_rect)
    game = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    text5_bool = False
 

    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos


        screen.blit(creator_img,(0,0))

        screen.blit(Pooh, (300,H * 1.2/ 5))
        screen.blit(Tee, (800,H * 1.2/ 5))
        screen.blit(logo, (590,H * 0.2/ 5))
        #screen.blit(Teacher, (560,H * 1.3/ 5))

        color = BLACK

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('Member',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 1.1/ 5)
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('Advisor   Somchoke Rueng-ittinun',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3.8/ 5)
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('Jakapat Phonyong',True,color)
        text_rect = text.get_rect()
        text_rect.center = (360,H * 2.9/ 5)
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('6110450669',True,color)
        text_rect = text.get_rect()
        text_rect.center = (360,H * 3.3/ 5)
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('Kritsada Lakhasont',True,color)
        text_rect = text.get_rect()
        text_rect.center = (880,H * 2.9/ 5)
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('Roboto-Bold', 40)
        text = Font.render('6110450014',True,color)
        text_rect = text.get_rect()
        text_rect.center = (880,H * 3.3/ 5)
        Surface.blit(text, text_rect)

        color = WHITE
        if text5_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Back',True,color)
        text_rect = text.get_rect()
        text_rect.center = (110,H * 4.8 / 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(set)
        if text_rect.collidepoint(mouse_pos):
            text5_bool = True
        else:
            text5_bool = False
        Surface.blit(text, text_rect)

        pygame.display.flip()
        mainClock.tick(100000)

def choice(set):
    pygame.init()
    mainClock = pygame.time.Clock()
    #all_fonts = pygame.font.get_fonts()
    #Font = pygame.font.SysFont('arial', 20)
    

    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('EXERCISE')


    ##def text_print(text,color1,color2,left,top,Font=basicFont):
    ##    text = Font.render(text,True,color1,color2)
    ##    text_rect = text.get_rect()
    ##    text_rect.top = top
    ##    text_rect.left = left
    ##    Surface.blit(text, text_rect)
    game = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    

    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos


        screen.blit(bg_img,(0,0))

        Font = pygame.font.SysFont('Roboto-Bold', 50)
        color = WHITE
        text = Font.render('Start from Biceps Curls > Butt Kicks > Lateral Raise > High Knee',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5 / 5)
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 1 (5)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 2/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera("FOREARMS", 5, set, 1)
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 2 (10)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera("FOREARMS", 10, set, 1)
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text4_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Back',True,color)
        text_rect = text.get_rect()
        text_rect.center = (110,H * 4.2 / 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(set)
        if text_rect.collidepoint(mouse_pos):
            text4_bool = True
        else:
            text4_bool = False
        Surface.blit(text, text_rect)


        pygame.display.flip()
        mainClock.tick(100000)

def chooseamount(tbody, set):
    pygame.init()
    mainClock = pygame.time.Clock()
    #all_fonts = pygame.font.get_fonts()
    #Font = pygame.font.SysFont('arial', 20)
    

    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('EXERCISE')


    ##def text_print(text,color1,color2,left,top,Font=basicFont):
    ##    text = Font.render(text,True,color1,color2)
    ##    text_rect = text.get_rect()
    ##    text_rect.top = top
    ##    text_rect.left = left
    ##    Surface.blit(text, text_rect)
    game = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    text5_bool = False
    text6_bool = False
    text7_bool = False
    

    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos


        screen.blit(bg_img,(0,0))

        Font = pygame.font.SysFont('Roboto-Bold', 50)
        color = WHITE
        text = Font.render('Choose amount of exercise',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5 / 5)
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 1 (10)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 1/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera(tbody, 10, set, 0)
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 2 (20)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 1.7/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera(tbody, 20, set, 0)
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text4_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 3 (30)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 2.4/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera(tbody, 30, set, 0)
        if text_rect.collidepoint(mouse_pos):
            text4_bool = True
        else:
            text4_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text5_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 4 (40)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3.1/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera(tbody, 40, set, 0)
        if text_rect.collidepoint(mouse_pos):
            text5_bool = True
        else:
            text5_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text6_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Level 5 (50)',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3.8/ 5)
        if text_rect.collidepoint(mouse_click):
            pygame.quit()
            camera(tbody, 50, set, 0)
        if text_rect.collidepoint(mouse_pos):
            text6_bool = True
        else:
            text6_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text7_bool:
            color = GREEN

        Font = pygame.font.SysFont('Roboto-Bold', 60)
        text = Font.render('Back',True,color)
        text_rect = text.get_rect()
        text_rect.center = (110,H * 4.2 / 5)
        if text_rect.collidepoint(mouse_click):
            main_menu(set)
        if text_rect.collidepoint(mouse_pos):
            text7_bool = True
        else:
            text7_bool = False
        Surface.blit(text, text_rect)


        pygame.display.flip()
        mainClock.tick(100000)


#if only for loading screen....
#def load_screen(next_pose):

#if for loading screen while display score
#def load_screen(next_pose,time)
def load_screen(next_pose, round,minutes,seconds,set):
    pygame.init()
    mainClock = pygame.time.Clock()

    timer1 = minutes
    timer2 = int(seconds)

    #time_out = float(15)
    #Fake_time_out = int(0)

    Surface = pygame.display.set_mode((W,H), 0, 32)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Loading...')

    ##bg_img = pygame.image.load('img/ojou.jpg')

    game = True
    clock = pygame.time.Clock()
    done  = True
    count_time = 0
    

    while game == True:
        #os.system('cls')
        #time_out = time_out - 0.1
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)


        screen.blit(bg_img,(0,0))

        Font = pygame.font.SysFont('Roboto-Bold', 100)
        color = WHITE
        text = Font.render(f'Total time {timer1} : {timer2} seconds',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H /2 )
        Surface.blit(text, text_rect)

        pygame.display.flip()
        mainClock.tick(100000)

        if done:
            count_time += 1
            if count_time > 100 * 9:
                ##hight_scoretime
                game = False
                if (next_pose == "end"):
                    main_menu(set)
                ##camera(next_pose)
                elif ( next_pose == "leg_back"):
                    pygame.quit()
                    camera("leg_back", round, set, 1)
                elif ( next_pose == "leg_front"):
                    pygame.quit()
                    camera("leg_front", round, set, 1)
                elif ( next_pose == "FOREARMS"):
                    pygame.quit()
                    camera("FOREARMS", round, set, 1)
                elif ( next_pose == "BACKARMS"):
                    pygame.quit()
                    camera("BACKARMS", round, set, 1)
            else:
                continue

def camera(tbody, round, set, connect): 
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0 
    count2 = 0 
    segmentor = SelfiSegmentation()

    #Timer
    seconds = float(0)
    minutes = int(0)
    
    if set == 1 :
        img2 = cv2.imread('img/1.jpg')
        img2 = cv2.resize(img2, (1280, 720))
    elif set == 2 :
        img2 = cv2.imread('img/2.jpg')
    elif set == 3 :
        img2 = cv2.imread('img/3.jpg')
        
    img3 = cv2.imread('img/tana.jpg')
    img3 = cv2.resize(img3, (1, 1))
    img_height, img_width, _ = img3.shape

    img4 = cv2.imread('img/BACKBUTTON.png')
    img4 = cv2.resize(img4, (100, 80))
    img_height2, img_width2, _ = img4.shape

    x = 50
    y = 200

    #forbackbutton
    x2 = 1
    y2 = 1

    while True:
        if seconds > 59:
            seconds = 0
            minutes = minutes+1

        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        # img = cv2.imread("AiTrainer/test.jpg")
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        imgchange = segmentor.removeBG(img, img2)

        imgchange[y:y+img_height , x:x+img_width] = img3

        imgchange[y2:y2+img_height2 , x2:x2+img_width2] = img4

        # print(lmList)
        if len(lmList) != 0:
            # Right Arm
            #angle = detector.findAngle(img, 12, 14, 16,)
            # # Left Arm
            if tbody=="leg_back" and count2 == 0:
                angle = detector.findAngle(imgchange, 27, 25, 23,)
                img3 = cv2.imread('img/Butt_Kicksleft.png')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="leg_back" and count2 > 0:
                angle = detector.findAngle(imgchange, 28, 26, 24,)
                img3 = cv2.imread('img/Butt_Kicksright.png')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="leg_front" and count2 == 0:
                angle = detector.findAngle(imgchange, 23, 25, 29,)
                img3 = cv2.imread('img/High_Knee(Left).png')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="leg_front" and count2 > 0:
                angle = detector.findAngle(imgchange, 24, 26, 30,)
                img3 = cv2.imread('img/High_Knee(right).png')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="FOREARMS" and count2 == 0:
                angle = detector.findAngle(imgchange, 12, 14, 16,)
                img3 = cv2.imread('img/Biceps_Curls(left).jpg')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="FOREARMS" and count2 > 0:
                angle = detector.findAngle(imgchange, 11, 13, 15,)
                img3 = cv2.imread('img/Biceps_Curls(right).jpg')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="BACKARMS" and count2 == 0:
                angle = detector.findAngle(imgchange, 24, 12, 16,)
                img3 = cv2.imread('img/Spare_pose(right).jpg')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            elif tbody=="BACKARMS" and count2 > 0:
                angle = detector.findAngle(imgchange, 23, 11, 15,)
                img3 = cv2.imread('img/Spare_pose(left).jpg')
                img3 = cv2.resize(img3, (200, 200))
                img_height, img_width, _ = img3.shape
            
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            # print(angle, per)

            # Check for the dumbbell curls
            color = BLUE
            if per == 100:
                color = BLUE
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = RED
                if dir == 1:
                    count += 0.5
                    dir = 0
            if count == round and count2 == 0:
                count2 = 1
                count = 0
            elif count == round and count2 == 1:
                cap.release()
                cv2.destroyAllWindows()
                if connect == 0:
                    load_screen("end" , round,minutes,seconds,set)
                elif connect == 1:
                    if tbody == "FOREARMS":
                        load_screen("leg_back" , round,minutes,seconds,set)
                    elif tbody == "leg_back":
                        load_screen("BACKARMS" , round,minutes,seconds,set)
                    elif tbody == "BACKARMS":
                        load_screen("leg_front" , round,minutes,seconds,set)
                    elif tbody == "leg_front":
                        load_screen("end" , round,minutes,seconds,set)
                
            # Draw Bar
            cv2.rectangle(imgchange, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(imgchange, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(imgchange, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

            #Draw Picture
            #cv2.rectangle(imgchange, (0, 100), (400, 300), (0, 255, 0), cv2.FILLED)

            # Draw Curl Countq
            cv2.rectangle(imgchange, (45, 450), (250, 720), GRAY, cv2.FILLED)
            cv2.putText(imgchange, str(int(count)), (85, 670), cv2.FONT_HERSHEY_PLAIN, 12,
                        WHITE, 25)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(imgchange, f'target = {round}', (40, 150), cv2.FONT_HERSHEY_PLAIN, 3.5,
                    WHITE, 5)

        os.system('cls')
        seconds = (seconds + 0.1)
        #print(minutes)
        #print(seconds)

        #-------------
        def mousePoints(event,x,y,flags,params):
            if event == cv2.EVENT_LBUTTONDOWN:
                if x >= 0 and x <= 100:
                    if y >= 0 and y <= 80:
                        #print(x,y)
                        cap.release()
                        cv2.destroyAllWindows()
                        main_menu(1)
        #-------------

        cv2.imshow("Image", imgchange)
        cv2.setMouseCallback("Image", mousePoints)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            sys.exit(0)

main_menu(1)
pygame.quit()
quit()