#===============================================================
# Verlet Integration
# 
# Function handling the verlet integration
# Created by: Lennard Marx
#===============================================================

import pygame
import numpy as np
from objects import Ball

def integrate(ball, force, scale, dt):
    # velocity verlet integration
    half_step_v = ball.v + ball.a*(dt*0.5) # half step update of the velocity
    new_x = ball.x + (half_step_v*dt)*scale # updating the coordinates scaled up by the ratio of pixels to meters
    new_a = ball.apply_forces(force) # acceleration calculated by applied forces
    new_v = half_step_v + new_a*(dt*0.5) # updating the velocity (full step)
    # updating the values
    ball.x = new_x
    ball.v = new_v
    ball.a = new_a



