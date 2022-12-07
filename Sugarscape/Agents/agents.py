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

        # sugar capacity
        self.sugar_cap = None
        self.wealth = 0

    # setters
    def init_vision_range(self):
        self.v = np.random.randint(1, 7)

    def init_metabolic_rate(self):
        self.m = np.random.randint(0, 4)

    def init_sugar_capacity(self):
        self.sugar_cap = np.random.randint(5, 26)

    def init_pos(self, rows, cols):
        self.x = np.random.randint(0, cols)
        self.y = np.random.randint(0, rows)

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

    def get_sugar_capacity(self):
        return self.sugar_cap


    def move(self, sugar_grid):
        v = self.get_vision()
        x, y = self.get_pos()
        sugar_cap = self.get_sugar_capacity()
        chosen_move = np.random.randint(0, 4)
        rows, cols = np.shape(sugar_grid)

        # 0: north
        if chosen_move == 0:
            for i in range(v):
                if y+i < cols and sugar_grid[x, y+i] != 0:
                    self.wealth += np.minimum(sugar_grid[x, y+i], sugar_cap-self.wealth)
                    sugar_grid[x, y+i] -= np.minimum(sugar_grid[x, y+i], sugar_cap-self.wealth)
                    self.set_new_pos(x, y+i)
                    break
            if y+v < cols and sugar_grid[x, y+v] == 0:
                self.set_new_pos(x, y + np.random.randint(0, v))

        # 1: west
        elif chosen_move == 1:
            for i in range(v):
                if x+i < rows and sugar_grid[x+i, y] != 0:
                    self.wealth += np.minimum(sugar_grid[x+i, y], sugar_cap-self.wealth)
                    sugar_grid[x+i, y] -= np.minimum(sugar_grid[x+i, y], sugar_cap-self.wealth)
                    self.set_new_pos(x+i, y)
                    break
            if x+v < rows and sugar_grid[x+v, y] == 0:
                self.set_new_pos(x + np.random.randint(0, v), y)

        # 2: south
        elif chosen_move == 2:
            for i in range(v):
                if y-i > 0 and sugar_grid[x, y-i] != 0:
                    self.wealth += np.minimum(sugar_grid[x, y-i], sugar_cap-self.wealth)
                    sugar_grid[x, y-i] -= np.minimum(sugar_grid[x, y-i], sugar_cap-self.wealth)
                    self.set_new_pos(x, y-i)
                    break
            if y-v > 0 and sugar_grid[x, y-v] == 0:
                self.set_new_pos(x, y-np.random.randint(0, v))

        # 3: east
        elif chosen_move == 3:
            for i in range(v):
                if x-i > 0 and sugar_grid[x-i, y] != 0:
                    self.wealth += np.minimum(sugar_grid[x-i, y], sugar_cap-self.wealth)
                    sugar_grid[x-i, y] -= np.minimum(sugar_grid[x-i, y], sugar_cap-self.wealth)
                    self.set_new_pos(x-i, y)
                    break
            if x-v > 0 and sugar_grid[x-v, y] == 0:
                self.set_new_pos(x-np.random.randint(0, v), y)

    def burn_sugar(self):
        m = self.get_metabolic_rate()
        wealth = self.get_wealth()
        self.set_wealth(wealth-m)

    def isAlive(self):
        m = self.get_metabolic_rate()
        wealth = self.get_wealth()
        return (wealth-m) > 0

    def init_agent(self, rows, cols):
        self.init_vision_range()
        self.init_metabolic_rate()
        self.init_sugar_capacity()
        self.init_pos(rows, cols)


