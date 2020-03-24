
import pygame
from pygame.locals import *

import configparser, os

class Cursor():
    """ Cursor class, generic class for a Cursor """
    def __init__(self, tw, x, y):
        self.tw = tw
        self.position = [x, y]
        self.mapx = 0
        self.mapy = 0
        config = configparser.ConfigParser()
        config.readfp(open('config/cursor.cfg'))
        sectionname = "imagename" + str(tw)
        imagename = config.get('cursor', sectionname)
        #self.image, self.rect = loader.load_png(imagename)

