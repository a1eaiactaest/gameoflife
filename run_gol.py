#!/usr/bin/env python3
from time import sleep
import numpy as np

from file_handler import loadfile
from gol_utils import get_neighbors, is_alive

def render_ascii(grid):
  # looks like printing np ndarray but without square braces
  for _, row in enumerate(grid): # "_", because "i" is useless here
    for j, char in enumerate(row):
      if j == len(row)-1:
        print(char)
      else:
        print(char, end=' ')
  print('\n')


def main(file_name):
  board = loadfile(file_name) 
  gen = 0

  rows = len(board)
  cols = len(board[0])

  while (1):
    print(gen)
    render_ascii(board) 
    # empty 2d array
    next_gen = np.zeros((cols, rows), str) 
    
    # calculate next generation
    for y in range(cols):
      for x in range(rows):
        cell = board[y][x] # current state we're at
        neighbors = get_neighbors(board, x, y, (rows,cols))

        # enough to grow, reproduction
        if not is_alive(cell) and len(neighbors) == 3:
          next_gen[y][x] = '#'

        # over and underpopulation
        elif is_alive(cell) and (len(neighbors) < 2 or len(neighbors) > 3):
          next_gen[y][x] = '.'
        
        # leave as it is
        else:
          next_gen[y][x] = cell

    board = next_gen
    gen+=1
    sleep(1)


if __name__ == "__main__":
  main('test_gen0.txt')
  #board=loadfile('test_gen0.txt')
  #print(get_neighbors(board, 4, 3, (10,10)))
  #print(is_alive(board[3][4]))
