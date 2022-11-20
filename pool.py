#!/usr/bin/env python

# official libraries
import pygame
import sys
import math
import numpy as np

# own files
sys.path.insert(0, '/home/lennard/Projects/Pool/include')
from event_checks import checkEvents
from objects import Ball, Cue_Ball, Table, Cue
from integration import integrate

# initialize pygame and create window
pygame.init()
window = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Pool Test")

# clock for controlling the framerate
clock = pygame.time.Clock()

# create objects
table = Table(50, 50, "resources/table.png")
cue = Cue(200, 200, "resources/cue.png")

cue_ball = Ball(200, 200, "resources/cue_ball.png")
ball_1 = Ball(750, 250, "resources/ball_1.png")
ball_8 = Ball(800, 300, "resources/ball_8.png")
balls = np.array([cue_ball, ball_1, ball_8])

# display font
test_font = pygame.font.Font("resources/RetroGaming.ttf", 25)
text_surface = test_font.render("Hallo", False, "Yellow")

# velvet integration variables
dt = 0.01 # time step
scale = 526/(dt/0.01) # pool ball: 57mm & 30pixels -> 1 meter ~ 526pixels normalized to timestep 0.01

cue_force = 15 # applied total force in Newton
angle = 7 # anlge of force in degree
angle = math.radians(angle) # converstion to radians

# ========= game loop ======================================0
while True:
    # force divided into 2 dimensions
    applied_cue_force = np.array([math.cos(angle)*cue_force, math.sin(angle)*cue_force])

    for it, ball in enumerate(balls):
        for others in balls[it+1:balls.size]:
            if np.sqrt((others.x[0] - ball.x[0])**2 + (others.x[1] - ball.x[1])**2) < 30:
                print("1")
            else:
                print("0")

    # verlet integration
    integrate(cue_ball, applied_cue_force, scale, dt)

    # reset external cue force
    cue_force = 0
    print("2")
    
# ========= event checks ====================================
    cue_ball.x[0], cue_ball.x[1] = checkEvents(cue_ball.x[0], cue_ball.x[1])
    
# ========= render screen =====================================
    window.fill("black")
    window.blit(table.surface, (table.x, table.y))
    window.blit(cue.surface, (cue.x, cue.y))

    window.blit(cue_ball.surface, (cue_ball.x[0], cue_ball.x[1]))
    window.blit(ball_1.surface, (ball_1.x[0], ball_1.x[1]))
    window.blit(ball_8.surface, (ball_8.x[0], ball_8.x[1]))
    
    
    #window.blit(text_surface, (300, 300))

    # update display
    pygame.display.update()
    clock.tick(120)
