#!/usr/bin/env python3
import numpy as np
from display import Display

class Grid:
  def __init__(self, input_file):
    self.grid_file = input_file 
    self.grid, self.W, self.H = self.load_zero_gen(self.grid_file)

  def load_zero_gen(self, input_file):
    # split on rows
    file_object = open(input_file, 'r')
    str_rows = file_object.read().strip().split('\n')
    file_object.close()
    # it's strings yet
    str_grid = [list(chars) for chars in str_rows]
    self.grid_valid(str_grid)
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

  def grid_valid(self, grid):
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
    for i, row in enumerate(grid):
      for j, cell in enumerate(row):
        if j == len(row)-1:
          print(cell)
        else:
          print(cell, end=' ')

class Cell:
  def __init__(self):
    raise NotImplementedError
     

def main():
  g = Grid('random_gen0.txt')
  d = Display(g.grid)  
  d.render()

if __name__ == "__main__":
  #g = Grid('test_gen0.txt')
  #g.render_grid()
  main()
