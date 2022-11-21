#!/usr/bin/env python

#===============================================================
# Pool Game
# Created by: Lennard Marx
# 
#===============================================================

# official libraries
import pygame
import sys
import math
import numpy as np
#np.seterr(divide='ignore', invalid='ignore')

# own files
sys.getfilesystemencoding()
sys.path.insert(0, '/home/lennard/Projects/Pool/include')
from event_checks import checkEvents, checkContacts
from objects import Ball, Cue_Ball, Table, Cue
from integration import integrate

# initialize pygame and create window
pygame.init()
pygame_icon = pygame.image.load("/home/lennard/Projects/Pool/resources/pool_icon.png")
pygame.display.set_icon(pygame_icon)
window = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Pool Test")

# clock for controlling the framerate
clock = pygame.time.Clock()

# create objects
table = Table(50, 50, "resources/table.png")
cue = Cue(150, 150, "resources/cue.png")

# creating the balls
cue_ball = Ball(200, 300, "resources/cue_ball.png")
ball_1 = Ball(700, 300, "resources/ball_1.png")
ball_2 = Ball(728, 316, "resources/ball_2.png")
ball_3 = Ball(728, 284, "resources/ball_3.png")
ball_4 = Ball(756, 331, "resources/ball_4.png")
ball_5 = Ball(756, 269, "resources/ball_5.png")
ball_6 = Ball(784, 316, "resources/ball_6.png")
ball_7 = Ball(784, 284, "resources/ball_7.png")
ball_8 = Ball(812, 300, "resources/ball_8.png")
ball_9 = Ball(756, 300, "resources/ball_9.png")
# array of all balls
balls = np.array([cue_ball, ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, ball_7, ball_8, ball_9])

# display font
test_font = pygame.font.Font("resources/RetroGaming.ttf", 25)
text_surface = test_font.render("Hallo", False, "Yellow")

# velvet integration variables
dt = 0.01 # time step
scale = 526 # /(dt/0.01) # pool ball: 57mm & 30pixels -> 1 meter ~ 526pixels normalized to timestep 0.01

cue_force = 20 # applied total force in Newton
angle = 0.5 # anlge of force in degree
angle = math.radians(angle) # converstion to radians


#========== game loop ======================================
while True:
    contact_force = 0
    contact_angle = 0

    # check contacts (brute force)
    checkContacts(balls)
        
    # get mouse position
    mouse = pygame.mouse.get_pos()

    # calculate angle between mouse and 
    angle = np.arctan2(cue_ball.x[1] - mouse[1], cue_ball.x[0] - mouse[0])

    checkEvents(cue)
    applied_cue_force = 0
    if cue.shoot == True:
        applied_cue_force = np.array([math.cos(angle)*cue_force, math.sin(angle)*cue_force])
    cue.shoot = False

    # verlet integration for all balls
    # MAKE LOOP!
    for x in range(10): # 10 integrations per time step
        integrate(cue_ball, applied_cue_force, scale, dt/10)
        integrate(ball_1, 0, scale, dt/10)
        integrate(ball_2, 0, scale, dt/10)
        integrate(ball_3, 0, scale, dt/10)
        integrate(ball_4, 0, scale, dt/10)
        integrate(ball_5, 0, scale, dt/10)
        integrate(ball_6, 0, scale, dt/10)
        integrate(ball_7, 0, scale, dt/10)
        integrate(ball_8, 0, scale, dt/10)
        integrate(ball_9, 0, scale, dt/10)
    
#========== render screen =====================================
    window.fill("black")
    window.blit(table.surface, (table.x, table.y))
    window.blit(cue.surface, (cue.x, cue.y))

    # MAKE LOOP!
    window.blit(cue_ball.surface, (cue_ball.x[0] - cue_ball.r, cue_ball.x[1] - cue_ball.r))
    window.blit(ball_1.surface, (ball_1.x[0] - ball_1.r, ball_1.x[1] - ball_1.r))
    window.blit(ball_2.surface, (ball_2.x[0] - ball_2.r, ball_2.x[1] - ball_2.r))
    window.blit(ball_3.surface, (ball_3.x[0] - ball_3.r, ball_3.x[1] - ball_3.r))
    window.blit(ball_4.surface, (ball_4.x[0] - ball_4.r, ball_4.x[1] - ball_4.r))
    window.blit(ball_5.surface, (ball_5.x[0] - ball_5.r, ball_5.x[1] - ball_5.r))
    window.blit(ball_6.surface, (ball_6.x[0] - ball_6.r, ball_6.x[1] - ball_6.r))
    window.blit(ball_7.surface, (ball_7.x[0] - ball_7.r, ball_7.x[1] - ball_7.r))
    window.blit(ball_8.surface, (ball_8.x[0] - ball_8.r, ball_8.x[1] - ball_8.r))
    window.blit(ball_9.surface, (ball_9.x[0] - ball_9.r, ball_9.x[1] - ball_9.r))

    #window.blit(text_surface, (300, 300))

    # update display
    pygame.display.update()
    clock.tick(120)
