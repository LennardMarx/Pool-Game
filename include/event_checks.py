#===============================================================
# Helper Functions
# Created by: Lennard Marx
# 
#===============================================================

import pygame
import numpy as np

# checking for button presses and clicks
def checkEvents(cue):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            #     x -= 20
            # if event.key == pygame.K_RIGHT:
            #     x += 20
            # if event.key == pygame.K_UP:
            #     y -= 20
            # if event.key == pygame.K_DOWN:
            #     y += 20
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cue.shoot = True

# checking for contacts (balls and walls)
def checkContacts(balls):
    for it, ball in enumerate(balls):
        for others in balls[it+1:balls.size]:
            if np.sqrt((others.x[0] - ball.x[0])**2 + (others.x[1] - ball.x[1])**2) < ball.d/2 + others.d/2:
                u1 = ball.v-(2*others.mass/(ball.mass + others.mass))*((np.dot(ball.v - others.v, ball.x - others.x))/(np.linalg.norm(ball.x - others.x)**2))*(ball.x - others.x)
                u2 = others.v-(2*ball.mass/(ball.mass + others.mass))*((np.dot(others.v - ball.v, others.x - ball.x))/(np.linalg.norm(ball.x - others.x)**2))*(others.x - ball.x)
                ball.v = u1
                others.v = u2
        if ball.x[0] < 105 + ball.r:
            ball.v[0] = -ball.v[0]
        if ball.x[0] > 1000 - ball.r:
            ball.v[0] = -ball.v[0]
        if ball.x[1] < 105 + ball.r:
            ball.v[1] = -ball.v[1]
        if ball.x[1] > 500 - ball.r:
            ball.v[1] = -ball.v[1]