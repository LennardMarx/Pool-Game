#===============================================================
# Helper Functions
# Created by: Lennard Marx
# 
#===============================================================

import pygame
import numpy as np
import math

# checking for button presses and clicks
def checkEvents(cue):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cue.shoot = True

# checking for contacts (balls and walls)
def checkContacts(balls, table, offset):
    for it, ball in enumerate(balls):
        for others in balls[it+1:]:
            # check for collision, collision only counts of objects move towards each other (dot product)
            if np.sqrt((others.x[0] - ball.x[0])**2 + (others.x[1] - ball.x[1])**2) <= (ball.d/2 + others.d/2) and np.dot(others.x - ball.x, ball.v - others.v) > 0:
                u1 = ball.v-(2*others.mass/(ball.mass + others.mass))*((np.dot(ball.v - others.v, ball.x - others.x))/(np.linalg.norm(ball.x - others.x)**2))*(ball.x - others.x)
                u2 = others.v-(2*ball.mass/(ball.mass + others.mass))*((np.dot(others.v - ball.v, others.x - ball.x))/(np.linalg.norm(ball.x - others.x)**2))*(others.x - ball.x)
                ball.v = u1
                others.v = u2

        # wall collisions relative to table size
        if ball.x[0] < (-0.45*table.w + ball.r) or ball.x[0] > (0.45*table.w - ball.r):
            ball.v[0] = -ball.v[0]
        if ball.x[1] < (-0.4*table.h + ball.r) or ball.x[1] > (0.4*table.h - ball.r):
            ball.v[1] = -ball.v[1]
