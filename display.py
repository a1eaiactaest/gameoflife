#!/usr/bin/env python3
import asyncio

import pygame

from colors import colors

class Display:
  def __init__(self, array):
    pygame.init()
    self.board = array
    self.W = 600
    self.H = 600
    self.running = True # display is on screen
    self.screen = pygame.display.set_mode((self.W, self.H))
    self.screen.fill(colors.BLACK)
    self.draw_grid()

  def check_quit_keys(self):
    for event in pygame.event.get():
      # title bar quit
      if event.type == pygame.QUIT:
        print("%s pressed, quitting" % event.type)
        self.running = False
      # esc key quit
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        print("%s pressed, quitting" % event.key)
        self.running = False
      # q key quit
      if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        print("%s pressed, quitting" % event.key)
        self.running = False

  # put this function in a loop
  def render_frame(self):
    self.check_quit_keys() 
    pygame.display.flip()

  def draw_grid(self):
    grid_W = len(self.board[0])
    grid_H = len(self.board)
    border_width = 3
    box_size = self.W/grid_W
    print('drawing grid of size (%d,%d), with boxes sized %2.f'%(grid_W, grid_H, box_size))
    for row in range(grid_H):
      for col in range(grid_W):
        rect = pygame.Rect(row*box_size, col*box_size, box_size, box_size)
        # if 1 in grid array then no border, whole rect is white
        if self.board[col][row] == 1: 
          pygame.draw.rect(self.screen, colors.WHITE, rect, 0)
        else:
          pygame.draw.rect(self.screen, colors.WHITE, rect, 1)
    pygame.display.update()
          
    
if __name__ == "__main__":
  from gol import Grid
  g = Grid('test_gen0.txt')
  d = Display(g.grid)
  d.render()
