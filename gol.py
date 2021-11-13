#!/usr/bin/env python3
import numpy as np
from display import Display

class Grid:
  def __init__(self, input_file):
    self.grid_file = input_file 
    self.grid, self.W, self.H = self.load_zero_gen(self.grid_file)
    
  def is_in_bounds(self, x, y):
    if x <= len(self.grid[0])-1 and y <= len(self.grid)-1:
      return True
    else:
      return False

  def get_cell_neighbours(self, cords): 
    x, y = cords
    ret = []
    # up
    if self.is_in_bounds(y+1, x):
      if self.grid[y+1][x] == 1:
        ret.append((x, y+1))

    # up left
    if self.is_in_bounds(y+1, x-1):
      if self.grid[y+1][x-1] == 1:
        ret.append((x-1, y+1))

    # up right
    if self.is_in_bounds(y+1, x+1):
      if self.grid[y+1][x+1] == 1:
        ret.append((x+1, y+1))

    # down
    if self.is_in_bounds(y-1, x):
      if self.grid[y-1][x] == 1:
        ret.append((x, y-1))

    # down left
    if self.is_in_bounds(y-1, x-1):
      if self.grid[y-1][x-1] == 1:
        ret.append((x-1, y-1))

    # down right
    if self.is_in_bounds(y-1, x+1):
      if self.grid[y-1][x+1] == 1:
        ret.append((x+1, y-1))

    # left
    if self.is_in_bounds(y, x-1):
      if self.grid[y][x-1] == 1:
        ret.append((x-1, y))

    # right
    if self.is_in_bounds(y, x+1):
      if self.grid[y][x+1] == 1:
        ret.append((x+1, y))

    #return ret
    return ret

  def load_zero_gen(self, input_file):
    # split on rows
    file_object = open(input_file, 'r')
    str_rows = file_object.read().strip().split('\n')
    file_object.close()
    # it's strings yet
    str_grid = [list(chars) for chars in str_rows]
    self.validate_grid(str_grid)
    int_grid = self.str2int(str_grid)
    return int_grid, len(int_grid[0]), len(int_grid)

  def str2int(self, array):
    # turn "#" and "." to 1 and 0, respectively 
    ret = array
    for i, row in enumerate(array):
      for j, char in enumerate(array[i]):
        if char == '.':
          ret[i][j] = 0
        elif char == '#':
          ret[i][j] = 1

    return np.array(array) # keep them numpy

  def validate_grid(self, grid):
    # could use python assertions, but it's better this way
    tmp_width = len(grid[0])
    for i, row in enumerate(grid):
      if len(row) != tmp_width:
        raise AssertionError('line %d in %s is not usual. fix it and run again' % (i+1, self.grid_file))
      tmp_width = len(row)
    return True
  
  def render_grid(self, grid=None): # ascii
    if grid is None:
      grid = self.grid
    # looks like printing np ndarray but without square braces
    for _, row in enumerate(grid): # "_", because "i" is useless here
      for j, cell in enumerate(row):
        if j == len(row)-1:
          print(cell)
        else:
          print(cell, end=' ')
  
  def new_generation(self):
    new_grid = np.zeros((self.W, self.H), dtype=int)
    print(self.get_live_cells())
  
  def get_live_cells(self):
    live_cells = []
    for y, row in enumerate(self.grid):
      for x, cell in enumerate(row):
        if cell == 1:
          live_cells.append((x,y))
    return live_cells

class GOL:
  def __init__(self, file_name):
    self.g = Grid(file_name)
    self.d = Display(self.g.grid)

  def main_loop(self):
    gen = 0
    while self.d.running:
      print('generation: %d' % gen)
      self.d.render_frame()
      for cell in self.g.get_live_cells():
        cell_neighbours = self.g.get_cell_neighbours(cell)
        print(cell, 'neighbours: ', cell_neighbours)
      self.g.new_generation()
      gen+=1

if __name__ == "__main__":
  game = GOL('test_gen0.txt')
  game.main_loop()
