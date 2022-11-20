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

cue_ball = Ball(200, 240, "resources/cue_ball.png")
ball_1 = Ball(750, 250, "resources/ball_1.png")
#ball_8 = Ball(800, 300, "resources/ball_8.png")
balls = np.array([cue_ball, ball_1])

# display font
test_font = pygame.font.Font("resources/RetroGaming.ttf", 25)
text_surface = test_font.render("Hallo", False, "Yellow")

# velvet integration variables
dt = 0.01 # time step
scale = 526 # /(dt/0.01) # pool ball: 57mm & 30pixels -> 1 meter ~ 526pixels normalized to timestep 0.01

cue_force = 13 # applied total force in Newton
angle = 0 # anlge of force in degree
angle = math.radians(angle) # converstion to radians

# ========= game loop ======================================0
while True:
    contact_force = 0
    contact_angle = 0
    # check for contacts between balls
    for it, ball in enumerate(balls):
        for others in balls[it+1:balls.size]:
            if np.sqrt((others.x[0] - ball.x[0])**2 + (others.x[1] - ball.x[1])**2) < ball.d/2 + others.d/2:
                contact_angle = np.arctan2(others.x[1] - ball.x[1], others.x[0] - ball.x[0])
                
                v1 = 2/7*np.sqrt(49/53*ball.v[0]**2)
                v2 = np.sqrt(49/53*ball.v[0]**2)
                print("v0: ", ball.v[0])
                print("v1: ", v1)
                print("v2: ", v2)

                ball.v = np.array([math.sin(contact_angle)*v1, math.cos(contact_angle+np.pi/2)*v2])
                others.v = np.array([math.cos(contact_angle)*v2, math.sin(contact_angle)*v2])
                # vel = np.sqrt(ball.v[0]**2 + ball.v[1]**2)
                # others.v = np.array([math.cos(contact_angle)*vel, math.sin(contact_angle)*vel])
                # ball.v = np.array([math.cos(contact_angle)*vel, -math.sin(contact_angle)*vel])
                # contact_force = ball.mass*(ball.v - ball.v_old)/dt
                # #contact_force = np.sqrt(contact_force[0]**2 + contact_force[1]**2)
                contact_angle = contact_angle*180/np.pi
                print(contact_angle)

    # force divided into 2 dimensions
    applied_cue_force = np.array([math.cos(angle)*cue_force, math.sin(angle)*cue_force])
    #contact_force = np.array([math.cos(contact_angle)*contact_force, math.sin(contact_angle)*contact_force])
    # verlet integration
    #for x in range(10):
    integrate(cue_ball, applied_cue_force, scale, dt)
    integrate(ball_1, 0, scale, dt)
    #integrate(cue_ball, -contact_force, scale, dt)
    #integrate(ball_1, contact_force, scale, dt)

    # reset external cue force
    cue_force = 0
# ========= event checks ====================================
    cue_ball.x[0], cue_ball.x[1] = checkEvents(cue_ball.x[0], cue_ball.x[1])
    
# ========= render screen =====================================
    window.fill("black")
    window.blit(table.surface, (table.x, table.y))
    window.blit(cue.surface, (cue.x, cue.y))

    window.blit(cue_ball.surface, (cue_ball.x[0], cue_ball.x[1]))
    window.blit(ball_1.surface, (ball_1.x[0], ball_1.x[1]))
    #window.blit(ball_8.surface, (ball_8.x[0], ball_8.x[1]))
    
    
    #window.blit(text_surface, (300, 300))

    # update display
    pygame.display.update()
    clock.tick(120)
