# Hopfield Networks
# Darren Hou


import math
import random
import numpy as np
import matplotlib.pyplot as pyp


def to_pattern(letter):
    """
    Converts a "letter" String into a numpy array of 1s and 0s
    """
    return np.array([1 if c=='X' else 0 for c in letter.replace('\n','')])


def display(pattern):
    """
    Passes a numpy array
    Displays a letter pattern in grid format

    The "letter" should be of dimension n by n
    """
    n = math.sqrt(pattern.size) # side length of pattern
    pyp.imshow(pattern.reshape((n,n)), cmap=pyp.cm.binary, interpolation='nearest')
    pyp.show()


def train(patterns):
    """
    Trains a list of patterns

    Returns the weight matrix as a 2d list
    """
    n = int(math.sqrt(patterns[1].size)) # side length
    result = [[0 for x in range(n)] for x in range(n)] 
    for pattern in patterns:
        for i in xrange(n):
            for j in xrange(n):
                result[i][j] += (2 * pattern[i] - 1) * (2 * pattern[j] - 1)
    return result

def recall(W, patterns, steps=5):
    """
    Given
    """
    sgn = vectorize(lambda x: 0 if x<0 else +1)
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

# display(to_pattern(A))
# distortion = distort(to_pattern(A), 5)
# display(distortion)

training = train([to_pattern(A), to_pattern(Z)])
display(to_pattern(training))