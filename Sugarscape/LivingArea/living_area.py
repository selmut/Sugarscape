import numpy as np
from Sugarscape.Utils.useful_functions import *


# class for modeling the living area
class LivingArea:
    def __init__(self, rows, cols, sugar_growth):
        self.rows = rows
        self.cols = cols
        self.sugar_growth = sugar_growth

    def init_grid(self):
        rows = self.rows
        cols = self.cols
        return np.zeros((rows, cols))

    def add_peaks(self):
        rows, cols = self.rows, self.cols
        out = np.zeros((rows, cols))

        x0_peak1, y0_peak1 = np.floor(cols/4), np.floor(rows/4)
        x0_peak2, y0_peak2 = np.floor(3*cols/4), np.floor(3*rows/4)

        d1 = np.floor((1/3)*np.sqrt((rows-y0_peak1)**2+(cols-x0_peak1)**2))
        d2 = np.floor((1/3)*(3/4)*np.sqrt((rows-y0_peak1)**2+(cols-x0_peak1)**2))
        d3 = np.floor((1/3)*(1/2)*np.sqrt((rows-y0_peak1)**2+(cols-x0_peak1)**2))
        d4 = np.floor((1/3)*(1/4)*np.sqrt((rows-y0_peak1)**2+(cols-x0_peak1)**2))

        for x in range(cols):
            for y in range(rows):
                if compute_distance(x, x0_peak1, y, y0_peak1) <= d1:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d1:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d2:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d2:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d3:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d3:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d4:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d4:
                    out[y, x] += 1
        return out

    def regrow_sugar(self, sugar_grid):
        sugar_growth = self.sugar_growth
        rows, cols = np.shape(sugar_grid)

        out = np.zeros((rows, cols))

        x0_peak1, y0_peak1 = np.floor(cols/4), np.floor(rows/4)
        x0_peak2, y0_peak2 = np.floor(3*cols/4), np.floor(3*rows/4)

        d1 = np.floor((1 / 3) * np.sqrt((rows - y0_peak1) ** 2 + (cols - x0_peak1) ** 2))
        d2 = np.floor((1 / 3) * (3 / 4) * np.sqrt((rows - y0_peak1) ** 2 + (cols - x0_peak1) ** 2))
        d3 = np.floor((1 / 3) * (1 / 2) * np.sqrt((rows - y0_peak1) ** 2 + (cols - x0_peak1) ** 2))
        d4 = np.floor((1 / 3) * (1 / 4) * np.sqrt((rows - y0_peak1) ** 2 + (cols - x0_peak1) ** 2))

        for x in range(cols):
            for y in range(rows):
                if compute_distance(x, x0_peak1, y, y0_peak1) <= d1 and sugar_grid[x, y]<1:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d1 and sugar_grid[x, y]<1:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d2 and sugar_grid[x, y]<2:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d2 and sugar_grid[x, y]<2:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d3 and sugar_grid[x, y]<3:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d3 and sugar_grid[x, y]<3:
                    out[y, x] += 1

                if compute_distance(x, x0_peak1, y, y0_peak1) <= d4 and sugar_grid[x, y]<4:
                    out[y, x] += 1
                elif compute_distance(x, x0_peak2, y, y0_peak2) <= d4 and sugar_grid[x, y]<4:
                    out[y, x] += 1
        return np.add(sugar_grid, out*sugar_growth)

