#!/usr/bin/env python3


import pygame


class Display:
  def __init__(self):
    pygame.init()
    self.size = (400, 400) 
    self.screen = pygame.display.set_mode(self.size)
    pygame.display.flip()

  def run(self):
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          break
      pygame.display.update()

if __name__ == "__main__":
  d = Display()
  d.run()
