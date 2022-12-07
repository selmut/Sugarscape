import numpy as np
import glob
import os


# choose an option with probability p
def p_choice(p):
    test = np.random.uniform(0, 1)
    if p >= test:
        return True
    else:
        return False


# returns distance from (x0, y0)
def compute_distance(x, x0, y, y0):
    return np.sqrt((x-x0)**2+(y-y0)**2)


# Moore neighbourhood with non-periodic boundary conditions
def moore_neighbourhood(N, row, col):
    indexes = [(row-1, col), (row-1, col+1), (row-1, col-1), (row, col+1), (row, col-1), (row+1, col), (row+1, col+1), (row+1, col-1)]
    iMax = N-1

    copy = indexes.copy()

    for coord in copy:
        row = coord[0]
        col = coord[1]

        if (col < 0) or (row < 0):
            indexes.remove(coord)

        elif (col > iMax) or (row > iMax):
            indexes.remove(coord)
    return indexes


def clear_dir(directory, extension):
    files = glob.glob(directory+'/*'+extension)
    for f in files:
        os.remove(f)
