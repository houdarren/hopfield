# Hopfield Networks
# Darren Hou


import math
import random
import numpy as np
import matplotlib.pyplot as pyp


def to_pattern(letter):
    """
    Converts a "letter" String into a 1d numpy array of 1s and 0s

    Returns a numpy array
    """
    return np.array([0 if c == 'X' else 1 for c in
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

    Returns the weight matrix as a 2d numpy array
    """
    n = patterns[1].size  # side length
    result = [[0 for x in range(n)] for x in range(n)]
    print("size " + str(n))  # debug
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
    iterations = 1
    energy = 0
    for i in xrange(size):
        for j in xrange(size):
            energy += weights[i, j] * pattern[i] * pattern[j]
    energy = -0.5 * energy
    print(energy)
    while not (np.array_equal(previous_pattern, previous_pattern2)):
        energy = 0
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
            for i in xrange(size):
                for j in xrange(size):
                    energy += weights[i, j] * pattern[i] * pattern[j]
        energy = -0.5 * energy
        print(energy)
        previous_pattern2 = np.array(previous_pattern)
        previous_pattern = np.array(pattern)
        iterations += 1
    print("iterations: " + str(iterations))
    return pattern


def calculate_energy(pattern):
    size = 


def distort(pattern, distortions):
    """
    Passes a 1 x n pattern array
    Changes a number of indicies within the given pattern

    Returns the pattern distorted
    """
    distort_list = random.sample(range(pattern.size), distortions)
    for coordinate in distort_list:
        if pattern[coordinate] == 1:
            pattern[coordinate] = 0
        else:
            pattern[coordinate] = 1
    return pattern


def check(actual, expected):
    """
    TODO: fix check
    """
    for pattern in expected:
        if np.array_equal(actual, expected):
            print("actual equals expected")
            return
        reverse = np.array(expected)
        for coordinate in reverse:
            if coordinate == 1:
                coordinate = 0
            else:
                coordinate = 1
        if np.array_equal(actual, reverse):
            print("actual equals reverse")
            return
    print("no result")


A = """
...XX...
..X..X..
.X....X.
X......X
XXXXXXXX
X......X
X......X
X......X
"""

E = """
XXXXXXX.
X.......
X.......
XXXXXX..
X.......
X.......
XXXXXXX.
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
XXXXXXXX
......X.
.....X..
....X...
...X....
..X.....
.X......
XXXXXXXX
"""

patterns = [to_pattern(A), to_pattern(E), to_pattern(equals), to_pattern(Z)]

training = train(patterns)

pattern = to_pattern(equals)
distortion = distort(pattern, 60)

result = recall(distortion, training, True)

print(result)
display(result)
