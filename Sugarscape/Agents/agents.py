import numpy as np


# class for representing a species, includes methods that are common between all species
class Agents:
    def __init__(self):
        # initial position
        self.x = None
        self.y = None

        # vision range
        self.v = None

        # metabolic rates
        self.m = None

        # sugar level
        self.wealth = None

        # age
        self.max_age = None
        self.age = 0

    # setters
    def init_vision_range(self):
        self.v = np.random.randint(1, 7)

    def init_metabolic_rate(self):
        self.m = np.random.randint(1, 5)

    def init_wealth(self):
        self.wealth = np.random.randint(5, 26)

    def init_pos(self, rows, cols):
        self.x = np.random.randint(0, cols)
        self.y = np.random.randint(0, rows)

    def init_age(self):
        self.max_age = np.random.uniform(60, 101)

    def set_wealth(self, w):
        self.wealth = w

    def set_new_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # getters
    def get_pos(self):
        return self.x, self.y

    def get_wealth(self):
        return self.wealth

    def get_vision(self):
        return self.v

    def get_metabolic_rate(self):
        return self.m

    def get_vision_range(self, sugar_grid):
        v = self.get_vision()
        x, y = self.get_pos()
        rows, cols = np.shape(sugar_grid)

        vision_range = []

        for n in range(v+1):
            i = n+1
            if (y+i) < rows:
                vision_range.append((y+i, x))
            if (x+i) < cols:
                vision_range.append((y, x+i))
            if (y-i) > 0:
                vision_range.append((y-i, x))
            if (x-i) > 0:
                vision_range.append((y, x-i))
        return vision_range

    def move(self, sugar_grid):
        vision_range = self.get_vision_range(sugar_grid)

        max_sugar = 0

        for coord in vision_range:
            y_vis, x_vis = coord[0], coord[1]

            if sugar_grid[y_vis, x_vis] >= max_sugar:
                max_sugar = sugar_grid[y_vis, x_vis]
                max_x, max_y = x_vis, y_vis

        self.wealth += sugar_grid[max_y, max_x]
        sugar_grid[max_y, max_x] -= sugar_grid[max_y, max_x]
        self.set_new_pos(max_x, max_y)

    def burn_sugar(self):
        m = self.get_metabolic_rate()
        wealth = self.get_wealth()
        self.set_wealth(wealth-m)

    def grow_older(self):
        self.age += 1

    def isAlive(self):
        m = self.get_metabolic_rate()
        wealth = self.get_wealth()
        age = self.age
        max_age = self.max_age
        return ((wealth-m) > 0) and (age <= max_age)

    def init_agent(self, rows, cols):
        self.init_vision_range()
        self.init_metabolic_rate()
        self.init_wealth()
        self.init_age()
        self.init_pos(rows, cols)


