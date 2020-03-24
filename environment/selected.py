
import pygame
from pygame.locals import *
from environment.item import Item

class Selected(object):
    """ Selected class, generic class for a tile """
    def __init__(self, value):
        self.value = value
        self.inqueue = False

