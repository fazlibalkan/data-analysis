"""
Create a function named calculate() in mean_var_std.py that uses 
Numpy to output the mean, variance, standard deviation, max, min, 
and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. 
The function should convert the list into a 3 x 3 Numpy array, 
and then return a dictionary containing the mean, variance, 
standard deviation, max, min, and sum along both axes and for 
the flattened matrix.
"""

import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  np_array = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ])

  num = 0
  for i in range(3):
    for j in range(3):
      np_array[i][j] = list[num]
      num += 1

  
  calculations = {
    'mean': [np_array.mean(axis=0).tolist(), np_array.mean(axis=1).tolist(), np_array.mean()],
    'variance': [np_array.var(axis=0).tolist(), np_array.var(axis=1).tolist(), np_array.var()],
    'standard deviation': [np_array.std(axis=0).tolist(), np_array.std(axis=1).tolist(), np_array.std()],
    'max': [np_array.max(axis=0).tolist(), np_array.max(axis=1).tolist(), np_array.max()],
    'min': [np_array.min(axis=0).tolist(), np_array.min(axis=1).tolist(), np_array.min()],
    'sum': [np_array.sum(axis=0).tolist(), np_array.sum(axis=1).tolist(), np_array.sum()]
  }


  return calculations