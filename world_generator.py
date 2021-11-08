#!/usr/bin/env python3
import random
import numpy as np

def biased_generate(width, height, freq):
  # pseudo random
  bias = freq/width
  ofile = open('random_gen0.txt', 'w+')
  for x in range(width):
    for y in range(height):  
      cell_type = np.random.choice(['.', '#'], p=[1.0-bias, bias]) # p -> biases
      ofile.write(cell_type) 
    ofile.write('\n')
  ofile.close()

if __name__ == "__main__":
  biased_generate(50, 50, 2)
