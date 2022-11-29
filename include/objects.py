#===============================================================
# Game Objects
# 
# This file contains all the objects used in the game 
# Created by: Lennard Marx
#===============================================================

import pygame
import numpy as np

# maybe create an object class with all shared member variables

class Ball:
    def __init__(self, x, y, img):
        self.d = 40 # diameter in pixels
        self.r = self.d/2 # radius
        # loading the image and setting the size on the screen
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.d, self.d))
        self.x = np.array([x, y]) # coordinates
        self.v = np.array([0, 0]) # velocity
        self.a = np.array([0, 0]) # acceleration
        self.mass = 0.165
        self.friction = 0.1
        self.collision_force = 0
        self.M = 1
        self.k = 1
    def apply_forces(self, external):
        self.fric_force = 9.81*self.mass*self.friction*self.v # *((1/(self.v*self.v))+0.001) # table cloth friction
        self.fric_acc = self.fric_force/self.mass # acc from table cloth friction
        self.collision_acc = self.collision_force/self.mass
        return -self.fric_acc+self.collision_acc # total applied acc
        self.collision_force = 0

class Cue_Ball(Ball):
    def apply_forces(self, external): # overridden from Ball class
        self.fric_force = 9.81*self.mass*self.friction*self.v # *((1/(self.v*self.v))+0.001) # table cloth friction
        self.fric_acc = self.fric_force/self.mass # acc from table cloth friction
        self.ext_acc = external/self.mass # acc from external forces
        self.collision_acc = self.collision_force/self.mass
        return self.ext_acc-self.fric_acc+self.collision_acc # total applied acc
        self.collision_force = 0

class Table:
    def __init__(self, x, y, img):
        self.x = np.array([x, y]) # coordinates
        self.w = 1400 # width
        self.h = 700 # height
        # sprite image and size
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))

class Cue:
    def __init__(self, x, y, img):
        self.x = np.array([x, y]) # coordinates
        self.w = 600 # width
        self.h = 12 # height
        # sprite image and size
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))
        self.shoot = False # check if mouse was clicked to apply force to the cue ball
