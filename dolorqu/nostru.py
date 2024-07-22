import numpy as np

m = 5  # number of rows
k = 3  # number of columns
dens = 0.8  # density of the matrix (percentage of non-zero elements)
values_range = (1, 10)  # range of values for the matrix elements

B = np.random.choice([0, np.random.uniform(*values_range)], size=(m, k), p=[1-dens, dens])
