# Hopfield Networks
# Darren Hou


import math
import random
import numpy as np
import matplotlib.pyplot as pyp


def to_pattern(letter):
    """
    Converts a "letter" String into a 1d numpy array of 1s and 0s
    """
    return np.array([1 if c == 'X' else 0 for c in
                    letter.replace('\n', '')])


def display(pattern):
    """
    Passes a numpy array
    Displays the letter pattern in grid format

    The "letter" should be of dimension n by n
    """
    n = math.sqrt(pattern.size)  # side length of pattern
    pyp.imshow(pattern.reshape((n, n)),
               cmap=pyp.cm.binary, interpolation='nearest')
    pyp.show()


def train(patterns):
    """
    Trains a list of patterns

    Returns the weight matrix as a 2d array
    """
    n = patterns[1].size  # side length
    result = [[0 for x in range(n)] for x in range(n)]
    print("size" + str(n))
    for pattern in patterns:
        for i in xrange(n):
            for j in xrange(n):
                if i != j:
                    result[i][j] += (2 * pattern[i] - 1) * (2 * pattern[j] - 1)
    return np.array(result)


def recall(pattern, weights, pause):
    """
    Given a pattern, uses the weight matrix to fix any distortions

    Returns a numpy array
    """
    size = pattern.size
    previous_pattern = np.array([0])
    previous_pattern2 = np.array([1])
    iterations = 0
    while not (np.array_equal(previous_pattern, previous_pattern2)):
        print("iterations: " + str(iterations))
        display(pattern)
        for i in xrange(size):
            sum = 0
            for j in xrange(size):
                # print(str(i) + " " + str(j)) # debug
                sum += pattern[j] * weights[j, i]
            if sum >= 0:
                pattern[i] = 1
            else:
                pattern[i] = 0

        previous_pattern2 = np.array(previous_pattern)
        previous_pattern = np.array(pattern)
        iterations += 1

    return pattern


def distort(pattern, distortions):
    """
    Passes a 1 x n pattern array
    Changes a number of indicies within the given pattern

    Returns the pattern distorted
    """
    distort_list = random.sample(range(pattern.size), distortions)
    for coordinate in distort_list:
        pattern[coordinate] = 0 if 1 else 1
    return pattern

A = """
.XXX.
X...X
XXXXX
X...X
X...X
"""

E = """
XXXXXXXX
X.......
X.......
XXXXXX..
X.......
X.......
XXXXXXXX
........
"""

equals = """
........
XXXXXXXX
........
XXXXXXXX
........
XXXXXXXX
........
........
"""

Z = """
XXXXX...
...X....
..X.....
.X......
XXXXX...
.......X
......X.
XXXXXX..
"""


# display(to_pattern(A))
# distortion = distort(to_pattern(A), 5)
# display(distortion)

training = train([to_pattern(E), to_pattern(equals), to_pattern(Z)])

pattern = to_pattern(E)
distortion = distort(pattern, 10)

result = recall(distortion, training, True)

print(result)
display(result)

