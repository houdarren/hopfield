# Hopfield Networks
# Darren Hou


import math
import random
import numpy as np
import matplotlib.pyplot as pyp


def to_pattern(letter):
    """
    Converts a "letter" String into a list of 1s and 0s
    """
    return np.array([1 if c=='X' else 0 for c in letter.replace('\n','')])


def display(pattern):
    """
    Displays a letter pattern in grid format

    The "letter" should be of dimension n by n
    """
    length = math.sqrt(pattern.size)
    pyp.imshow(pattern.reshape((length,length)), cmap=pyp.cm.binary, interpolation='nearest')
    pyp.show()


def train(patterns):
    """
    Trains a list of patterns

    Returns the weight matrix
    """
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

distortion = distort(to_pattern(A), 5)
display(distortion)
