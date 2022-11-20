import pygame
import numpy as np

# maybe create an object class with all shared member variables

class Ball:
    def __init__(self, x, y, img):
        # sprite image and size
        self.d = 30 # diameter in pixels
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.d, self.d))
        self.x = np.array([x, y]) # coordinates
        self.v = np.array([0, 0]) # velocity
        self.v_old = np.array([0, 0]) # previous velocity
        self.a = np.array([0, 0]) # acceleration
        self.mass = 0.165
        self.friction = 0.07
    def apply_forces(self, external):
        self.fric_force = 9.81*self.mass*self.friction*self.v # table cloth friction
        self.fric_acc = self.fric_force/self.mass # acc from table cloth friction
        self.ext_acc = external/self.mass # acc from external forces
        return self.ext_acc-self.fric_acc # total applied acc

class Cue_Ball(Ball):
    def move(self):
        pass

class Table:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (1000, 500))

class Cue:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.surface = pygame.image.load(img).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (400, 10))