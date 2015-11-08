def to_pattern(letter):
    from numpy import array
    return array([+1 if c=='X' else -1 for c in letter.replace('\n','')])

def display(pattern):
    from matplotlib.pyplot import imshow, cm, show
    imshow(pattern.reshape((5,5)),cmap=cm.binary, interpolation='nearest')
    show()

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
