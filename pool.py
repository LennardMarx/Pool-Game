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

# own files
# sys.getfilesystemencoding()
sys.path.insert(0, '/home/lennard/Projects/Pool/include')
from event_checks import checkEvents, checkContacts
from objects import Ball, Cue_Ball, Table, Cue
from integration import integrate

# initialize pygame and create window
pygame.init()
window = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Pool")

# changing the icon in the task bar
pygame_icon = pygame.image.load("/home/lennard/Projects/Pool/resources/pool_icon.png")
pygame.display.set_icon(pygame_icon)

# clock for controlling the framerate
clock = pygame.time.Clock()

# create objects
table = Table(100, 100, "resources/table.png")
cue = Cue(150, 50, "resources/cue.png")

# offset to have coords relative to table center
offset = np.array([table.x[0] + table.w/2, table.x[1] + table.h/2])

# creating the balls
cue_ball = Cue_Ball(-300, 0, "resources/cue_ball.png")
ball_1 = Ball(200, 0, "resources/ball_1.png")
ball_2 = Ball(235, 20, "resources/ball_2.png")
ball_3 = Ball(235, -20, "resources/ball_3.png")
ball_4 = Ball(270, 40, "resources/ball_4.png")
ball_5 = Ball(270, -40, "resources/ball_5.png")
ball_6 = Ball(305, 20, "resources/ball_6.png")
ball_7 = Ball(305, -20, "resources/ball_7.png")
ball_8 = Ball(340, 0, "resources/ball_8.png")
ball_9 = Ball(270, 0, "resources/ball_9.png")
# array of all balls
balls = np.array([cue_ball, ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, ball_7, ball_8, ball_9])

mouse = np.array([0, 0])

# display font
test_font = pygame.font.Font("resources/RetroGaming.ttf", 25)
text_surface = test_font.render("Hallo", False, "Yellow")

# velvet integration variables
dt = 0.01 # time step
scale = 680 # /(dt/0.01) # pool ball: 57mm & 30pixels -> 1 meter ~ 526pixels normalized to timestep 0.01

cue_force = 35 # applied total force in Newton
#angle = 0 # anlge of force in degree
#angle = math.radians(angle) # converstion to radians


#========== game loop ======================================
while True:
    contact_angle = 0

    # check contacts (brute force)
    checkContacts(balls, table, offset)

    # check for clicks and button presses
    checkEvents(cue)

    # get mouse position
    m = pygame.mouse.get_pos()
    mouse[0] = m[0] - offset[0]
    mouse[1] = m[1] - offset[1]

    # calculate angle between mouse and cue ball
    angle = np.arctan2(cue_ball.x[1] - mouse[1], cue_ball.x[0] - mouse[0])
    applied_cue_force = 0
    if cue.shoot == True:
        applied_cue_force = np.array([math.cos(angle)*cue_force, math.sin(angle)*cue_force])
    cue.shoot = False

    # verlet integration for all balls
    #for x in range(5): # 10 integrations per time step
    integrate(cue_ball, applied_cue_force, scale, dt)
    for ball in balls[1:]:
        integrate(ball, 0, scale, dt)

#===   ======= render screen =====================================
    window.fill("black")
    window.blit(table.surface, (table.x[0], table.x[1]))
    window.blit(cue.surface, (cue.x[0], cue.x[1]))

    # rendering balls
    for ball in balls:
        window.blit(ball.surface, (ball.x[0] + offset[0] - ball.r, ball.x[1] + offset[1] - ball.r))

    #window.blit(text_surface, (300, 300))

    # update display
    pygame.display.update()
    clock.tick(60)