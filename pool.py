#!/usr/bin/env python

#===============================================================
# Pool Game
# 
# Created by: Lennard Marx
#===============================================================

# official libraries
import pygame
import sys
import math
import numpy as np

# own files
sys.path.insert(0, '/home/lennard/Projects/Pool/include')
from event_checks import checkEvents, checkContacts
import objects as obj
from integration import integrate

# initialize pygame and create window
pygame.init()
window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Pool")

# changing the icon in the task bar
pygame_icon = pygame.image.load("/home/lennard/Projects/Pool/resources/pool_icon.png")
pygame.display.set_icon(pygame_icon)

# clock for controlling the framerate
clock = pygame.time.Clock()

# create objects
table = obj.Table(100, 100, "resources/table.png")
cue = obj.Cue(150, 50, "resources/cue.png")

# offset to have coords relative to table center
offset = np.array([table.x[0] + table.w/2, table.x[1] + table.h/2])

# creating the balls
cue_ball = obj.Cue_Ball(-300, 0, "resources/cue_ball.png")
ball_1 = obj.Ball(200, 0, "resources/ball_1.png")
ball_2 = obj.Ball(ball_1.x[0] + 35, ball_1.x[1] + 20, "resources/ball_2.png")
ball_3 = obj.Ball(ball_1.x[0] + 35, ball_1.x[1] - 20, "resources/ball_3.png")
ball_4 = obj.Ball(ball_1.x[0] + 70, ball_1.x[1] + 40, "resources/ball_4.png")
ball_5 = obj.Ball(ball_1.x[0] + 70, ball_1.x[1] - 40, "resources/ball_5.png")
ball_6 = obj.Ball(ball_1.x[0] + 105, ball_1.x[1] + 20, "resources/ball_6.png")
ball_7 = obj.Ball(ball_1.x[0] + 105, ball_1.x[1] - 20, "resources/ball_7.png")
ball_8 = obj.Ball(ball_1.x[0] + 140, ball_1.x[1] + 0, "resources/ball_8.png")
ball_9 = obj.Ball(ball_1.x[0] + 70, ball_1.x[1] + 0, "resources/ball_9.png")
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

#========== game loop ======================================
while True:
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

    # calculate force vector dependent on angle 
    applied_cue_force = 0 # reset the cue_force
    if cue.shoot == True: # check if mouse was clicked
        applied_cue_force = np.array([math.cos(angle)*cue_force, math.sin(angle)*cue_force])
    cue.shoot = False

    # verlet integration for all balls
    #integrate(cue_ball, applied_cue_force, scale, dt)
    for ball in balls:
        integrate(ball, applied_cue_force, scale, dt)

#============= render screen =====================================
    window.fill("black") # reset screen by filling it black
    window.blit(table.surface, (table.x[0], table.x[1])) # render the table
    window.blit(cue.surface, (cue.x[0], cue.x[1])) # render the cue

    # rendering balls
    for ball in balls:
        window.blit(ball.surface, (ball.x[0] + offset[0] - ball.r, ball.x[1] + offset[1] - ball.r))
        # stop ball a little earlier
        #if np.linalg.norm(ball.v) < 0.008:
        #    ball.v = np.array([0, 0])

    # update display
    pygame.display.update()
    clock.tick(100)