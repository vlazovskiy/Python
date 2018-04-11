import numpy as np
from numpy.random import randn

N = 10000
counter = 0

for i in randn(N):
    x = randn()
    if (x >= -1 and x <= 1):
        counter = counter + 1

print( counter / N )
