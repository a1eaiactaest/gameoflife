#!/usr/bin/env python3

def get_neighbors(grid, x, y, size):
  neighbors = []
  rows, cols = size
  # up
  if in_bounds(y-1, x, size):
    if is_alive(grid[y-1][x]):
      neighbors.append((x,y-1))

  # up-right
  if in_bounds(y-1, x+1, size):
    if is_alive(grid[y-1][x+1]):
      neighbors.append((x+1,y-1))

  # up-left
  if in_bounds(y-1, x-1, size):
    if is_alive(grid[y-1][x-1]):
      neighbors.append((x-1,y-1))

  # right
  if in_bounds(y, x+1, size):
    if is_alive(grid[y][x+1]):
      neighbors.append((x+1,y))

  # left
  if in_bounds(y, x-1, size):
    if is_alive(grid[y][x-1]):
      neighbors.append((x-1,y))

  # down
  if in_bounds(y+1, x, size):
    if is_alive(grid[y+1][x]):
      neighbors.append((x,y+1))

  # down-right
  if in_bounds(y+1, x+1, size):
    if is_alive(grid[y+1][x+1]):
      neighbors.append((x+1,y+1))

  # down-left
  if in_bounds(y+1, x-1, size):
    if is_alive(grid[y+1][x-1]):
      neighbors.append((x-1,y+1))

  return neighbors

def is_alive(cell):
  if cell == '#':
    return True
  elif cell == '.':
    return False

def in_bounds(y, x, size):
  rows, cols = size
  if x >= cols or y >= rows: 
    return False
  return True

