#!/usr/bin/env python3
import pygame

from gol import Grid
from colors import colors

class Display:
  def __init__(self, array):
    self.ratio = 50
    self.W = len(array[0]) * self.ratio
    self.H = len(array) * self.ratio
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
    block_size = self.ratio
    for y in range(self.H):
      for x in range(self.W):
        rect = pygame.Rect(x*(block_size+1), y*(block_size+1), block_size, block_size)
        pygame.draw.rect(self.screen, colors.BLACK, rect)

if __name__ == "__main__":
  g = Grid('test_gen0.txt')
  d = Display(g.grid)
  d.render()
