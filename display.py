#!/usr/bin/env python3
import pygame

from colors import colors

class Display:
  def __init__(self, width, height):
    pygame.init()
    self.screen = pygame.display.set_mode((width, height))

  def render(self):
    running = True
    while running:
      for event in pygame.event.get():
        # title bar quit
        if event.type == pygame.QUIT:
          running = False
        # esc key quit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          print("%s pressed, quitting" % event.key)
          running = False
      pygame.display.flip()

if __name__ == "__main__":
  d = Display(960, 540) 
  d.render()
