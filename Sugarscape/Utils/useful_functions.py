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
def moore_neighbourhood(grid, x, y):
    indexes = [(x-1, y), (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1), (x+1, y), (x+1, y+1), (x+1, y-1)]
    values = []
    iMax = len(grid) - 1

    copy = indexes.copy()

    for coord in copy:
        x = coord[0]
        y = coord[1]

        if (x < 0) or (y < 0):
            indexes.remove(coord)

        elif (x > iMax) or (y > iMax):
            indexes.remove(coord)

    for i in indexes:
        values.append(grid[i[0]][i[1]])
    return values, indexes


def clear_dir(directory, extension):
    files = glob.glob(directory+'/*'+extension)
    for f in files:
        os.remove(f)
