# Hopfield Networks
# Darren Hou

# Converts a "letter" String into a list of 1s and 0s

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def to_pattern(letter):
    # from numpy import array
    return np.array([+1 if c=='X' else 0 for c in letter.replace('\n','')])

# Displays a letter pattern in grid format
# The "letter" should be of dimension n by n
def display(pattern):
    length = math.sqrt(pattern.size)
    plt.imshow(pattern.reshape((length,length)), cmap=plt.cm.binary, interpolation='nearest')
    plt.show()

# Trains a list of patterns
def train(patterns):
    r,c = patterns.shape
    W = np.zeros((c,c))
    for p in patterns:
        W = W + np.outer(p,p)
    W[np.diag_indices(c)] = 0
    return W/r

def recall(W, patterns, steps=5):
    sgn = vectorize(lambda x: -1 if x<0 else +1)
    for _ in xrange(steps):        
        patterns = sgn(dot(patterns,W))
    return patterns

def distort(pattern, distortions):
    distort_list = random.sample(range(pattern.size), distortions)
    for coordinate in distort_list:
        if pattern[coordinate] == 1:
            pattern[coordinate] = 0
        else:
            pattern[coordinate] = 1
    return pattern

A = """
.XXX.
X...X
XXXXX
X...X
X...X
"""
 
Z = """
XXXXX
...X.
..X..
.X...
XXXXX
"""

distortion = distort(to_pattern(A), 10)
display(distortion)
