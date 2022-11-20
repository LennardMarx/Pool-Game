import pygame
import numpy as np
from objects import Ball

def integrate(ball, force, scale, dt):
    # velocity verlet integration
    half_step_v = ball.v + ball.a*(dt*0.5)
    new_x = ball.x + (half_step_v*dt)*scale
    new_a = ball.apply_forces(force)
    new_v = half_step_v + new_a*(dt*0.5)
    # updating the values
    ball.x = new_x
    ball.v = new_v
    ball.a = new_a



