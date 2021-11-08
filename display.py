#!/usr/bin/env python3
import pygame

from colors import colors

class Display:
  def __init__(self, array):
    #self.W = len(array[0]) * self.ratio
    #self.H = len(array) * self.ratio
    self.grid_W = len(array[0])
    self.grid_H = len(array)
    self.W = 600
    self.H = 600
    self.screen = pygame.display.set_mode((self.W, self.H))
    self.screen.fill(colors.WHITE)
    self.draw_mesh()

  def render(self):
    pygame.init()
    running = True
    while running:
      for event in pygame.event.get():
        # title bar quit
        if event.type == pygame.QUIT:
          print("%s pressed, quitting" % event.type)
          running = False
        # esc key quit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          print("%s pressed, quitting" % event.key)
          running = False
      pygame.display.flip()

  def draw_mesh(self):
    for row in range(self.grid_H
    
if __name__ == "__main__":
  from gol import Grid
  g = Grid('random_gen0.txt')
  d = Display(g.grid)
  d.render()
