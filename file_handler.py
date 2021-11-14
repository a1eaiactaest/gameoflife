#!/usr/bin/env python3
import numpy as np

def loadfile(file_name):
  # opens file, returns 2d array
  # open and split to rows
  file_object = open(file_name, 'r')
  rows = np.array(file_object.read().strip().split('\n'))
  file_object.close()
  
  ret_array = np.array([list(row) for row in rows])
  if array_is_valid(ret_array):
    return ret_array

def array_is_valid(array):
  # array can be only valid if every row has the same amount of characters

  assert isinstance(array, np.ndarray), f'array must be numpy.ndarray, but is {type(array)}'
  shape = array.shape
  assert len(shape) == 2, f'board array has to be 2D, but is {shape}'

  return True
  
  
