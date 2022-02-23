import os
import pygame
import random
import time
import math


def setup(screen, etc):
    pass

def draw(screen, etc):
    x = etc.xres / 2
    y = etc.yres / 2
    radius = 10 + int(etc.knob2 * 100)
    color = etc.color_picker(etc.knob4)
    
    for i in range(etc.yres):
        pygame.gfxdraw.filled_circle(screen, x, i, radius, color)
