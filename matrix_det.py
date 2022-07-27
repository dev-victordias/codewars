""" 
DESCRIPTION:
Write a function that accepts a square matrix (N x N 2D array) 
and returns the determinant of the matrix. 
"""

import numpy as np 

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) >= 3:
        return round(np.linalg.det(matrix))