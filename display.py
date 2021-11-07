#!/usr/bin/env python3


import pygame


class Display:
  def __init__(self):
    pygame.init()
    self.size = (400, 400) 
    self.screen = pygame.display.set_mode(size)
    pygame.display.flip()
