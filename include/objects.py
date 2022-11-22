#===============================================================
# Game Objects
# Created by: Lennard Marx
# 
#===============================================================

import pygame
import numpy as np

# maybe create an object class with all shared member variables

class Ball:
    def __init__(self, x, y, img):
        # sprite image and size
        self.d = 40 # diameter in pixels
        self.r = self.d/2
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.d, self.d))
        self.x = np.array([x, y]) # coordinates
        self.v = np.array([0, 0]) # velocity
        self.a = np.array([0, 0]) # acceleration
        self.mass = 0.165
        self.friction = 0.1
    def apply_forces(self, external):
        #if abs(np.linalg.norm(self.v)) > 0:
        self.fric_force = 9.81*self.mass*self.friction*self.v # *((1/(self.v*self.v))+0.001) # table cloth friction
        self.fric_acc = self.fric_force/self.mass # acc from table cloth friction
        self.ext_acc = external/self.mass # acc from external forces
        return self.ext_acc-self.fric_acc # total applied acc

class Cue_Ball(Ball):
    def move(self):
        pass

class Table:
    def __init__(self, x, y, img):
        self.x = np.array([x, y])
        self.w = 1200
        self.h = 600
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))

class Cue:
    def __init__(self, x, y, img):
        self.x = np.array([x, y])
        self.w = 600
        self.h = 12
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))
        self.shoot = False