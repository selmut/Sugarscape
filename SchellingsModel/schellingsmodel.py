import numpy as np
import pandas as pd
from Utils.plots import *
from Utils.useful_functions import *


class SchellingsModel:
    def __init__(self, N, agentsA, agentsB, timeSteps):
        self.N = N
        self.agentsA = agentsA
        self.agentsB = agentsB
        self.timeSteps = timeSteps

    def init_grid(self):
        N = self.N
        agentsA = self.agentsA
        agentsB = self.agentsB

        grid = np.zeros((N, N))

        for a in range(agentsA):
            placed = False
            while not placed:
                row = np.random.randint(0, N)
                col = np.random.randint(0, N)

                if grid[row, col] == 0:
                    grid[row, col] += 1
                    placed = True

        for b in range(agentsB):
            placed = False
            while not placed:
                row = np.random.randint(0, N)
                col = np.random.randint(0, N)

                if grid[row, col] == 0:
                    grid[row, col] += 100
                    placed = True
        return grid

    def move(self, agents_grid):
        N = self.N
        moving_events = 0

        row, col = np.random.randint(0, N), np.random.randint(0, N)
        agent_type = agents_grid[row, col]
        happiness = 0

        if agent_type == 1:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 1:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) <= 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 1
                moving_events += 1

        if agent_type == 100:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 100:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) <= 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 100
                moving_events += 1

        return agents_grid

    def anti_gregarious_move(self, agents_grid):
        N = self.N

        row, col = np.random.randint(0, N), np.random.randint(0, N)
        agent_type = agents_grid[row, col]
        happiness = 0

        if agent_type == 1:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 1:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) > 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 1

        if agent_type == 100:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 100:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) > 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 100

        return agents_grid

    def move_frustration(self, agents_grid):
        N = self.N
        moving_events = 0

        row, col = np.random.randint(0, N), np.random.randint(0, N)
        agent_type = agents_grid[row, col]
        happiness = 0

        if agent_type == 1:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 1:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) > 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 1
                moving_events += 1

        if agent_type == 100:
            neighbourhood_indexes = moore_neighbourhood(N, row, col)

            # compute happiness
            for i in neighbourhood_indexes:
                row_i = i[0]
                col_i = i[1]
                if agents_grid[row_i, col_i] == 100:
                    happiness += 1

            # move agent
            if happiness / len(neighbourhood_indexes) <= 0.5:
                rows_empty, cols_empty = np.where(agents_grid == 0)
                i = np.random.randint(0, len(rows_empty))
                agents_grid[row, col] = 0
                agents_grid[rows_empty[i], cols_empty[i]] = 100
                moving_events += 1

        return agents_grid

    def compute_happiness(self, all_grids):
        timeSteps = self.timeSteps
        N = self.N
        happiness_total = np.zeros(timeSteps)
        happiness_A = np.zeros(timeSteps)
        happiness_B = np.zeros(timeSteps)
        agentsA = self.agentsA
        agentsB = self.agentsB
        agents = agentsA+agentsB

        for t in range(timeSteps):
            if t % 1000 != 0:
                continue
            print('Time step: '+str(t))

            grid = all_grids[:, :, t]

            current_happiness_A = 0
            current_happiness_B = 0
            current_happiness_total = 0

            for row in range(N):
                for col in range(N):
                    agent_type = grid[row, col]
                    neighbourhood_indexes = moore_neighbourhood(N, row, col)

                    # compute happiness
                    for i in neighbourhood_indexes:
                        row_i = i[0]
                        col_i = i[1]

                        if agent_type == 1:
                            if grid[row_i, col_i] == 1:
                                current_happiness_A += 1
                                current_happiness_total += 1
                        elif agent_type == 100:
                            if grid[row_i, col_i] == 100:
                                current_happiness_B += 1
                                current_happiness_total += 1

                    happiness_A[t] = current_happiness_A/len(neighbourhood_indexes)
                    happiness_B[t] = current_happiness_B / len(neighbourhood_indexes)
                    happiness_total[t] = current_happiness_total / len(neighbourhood_indexes)

        return (happiness_A[np.where(happiness_A != 0)]/agentsA)/np.max(happiness_A/agentsA), \
            (happiness_B[np.where(happiness_B != 0)]/agentsB)/np.max(happiness_B/agentsB), \
            (happiness_total[np.where(happiness_total != 0)]/agents)/np.max(happiness_total/agents)

    def compute_happiness_anti_gregarious(self, all_grids):
        timeSteps = self.timeSteps
        N = self.N
        happiness_total = np.zeros(timeSteps)
        happiness_A = np.zeros(timeSteps)
        happiness_B = np.zeros(timeSteps)
        agentsA = self.agentsA
        agentsB = self.agentsB
        agents = agentsA+agentsB

        for t in range(timeSteps):
            if t % 1000 != 0:
                continue
            print('Time step: '+str(t))

            grid = all_grids[:, :, t]

            current_happiness_A = 0
            current_happiness_B = 0
            current_happiness_total = 0

            for row in range(N):
                for col in range(N):
                    agent_type = grid[row, col]
                    neighbourhood_indexes = moore_neighbourhood(N, row, col)

                    # compute happiness
                    for i in neighbourhood_indexes:
                        row_i = i[0]
                        col_i = i[1]

                        if agent_type == 1:
                            if grid[row_i, col_i] == 100:
                                current_happiness_A += 1
                                current_happiness_total += 1
                        elif agent_type == 100:
                            if grid[row_i, col_i] == 1:
                                current_happiness_B += 1
                                current_happiness_total += 1

                    happiness_A[t] = current_happiness_A/len(neighbourhood_indexes)
                    happiness_B[t] = current_happiness_B / len(neighbourhood_indexes)
                    happiness_total[t] = current_happiness_total / len(neighbourhood_indexes)
        return (happiness_A[np.where(happiness_A != 0)]/agentsA)/np.max(happiness_A/agentsA), \
            (happiness_B[np.where(happiness_B != 0)]/agentsB)/np.max(happiness_B/agentsB), \
            (happiness_total[np.where(happiness_total != 0)]/agents)/np.max(happiness_total/agents)

    def compute_happiness_frustration(self, all_grids):
        timeSteps = self.timeSteps
        N = self.N
        happiness_total = np.zeros(timeSteps)
        happiness_A = np.zeros(timeSteps)
        happiness_B = np.zeros(timeSteps)
        agentsA = self.agentsA
        agentsB = self.agentsB
        agents = agentsA+agentsB

        for t in range(timeSteps):
            if t % 1000 != 0:
                continue
            print('Time step: '+str(t))

            grid = all_grids[:, :, t]

            current_happiness_A = 0
            current_happiness_B = 0
            current_happiness_total = 0

            for row in range(N):
                for col in range(N):
                    agent_type = grid[row, col]
                    neighbourhood_indexes = moore_neighbourhood(N, row, col)

                    # compute happiness
                    for i in neighbourhood_indexes:
                        row_i = i[0]
                        col_i = i[1]

                        if agent_type == 1:
                            if grid[row_i, col_i] == 100:
                                current_happiness_A += 1
                                current_happiness_total += 1
                        elif agent_type == 100:
                            if grid[row_i, col_i] == 100:
                                current_happiness_B += 1
                                current_happiness_total += 1

                    happiness_A[t] = current_happiness_A/len(neighbourhood_indexes)
                    happiness_B[t] = current_happiness_B / len(neighbourhood_indexes)
                    happiness_total[t] = current_happiness_total / len(neighbourhood_indexes)

        return (happiness_A[np.where(happiness_A != 0)]/agentsA)/np.max(happiness_A/agentsA), \
            (happiness_B[np.where(happiness_B != 0)]/agentsB)/np.max(happiness_B/agentsB), \
            (happiness_total[np.where(happiness_total != 0)]/agents)/np.max(happiness_total/agents)

    def compute_moving_events(self, all_grids):
        timeSteps = self.timeSteps
        N = self.N
        moving_events = np.zeros(timeSteps)
        agents = self.agentsA+self.agentsB

        for t in range(timeSteps+1):
            if t % 1001 != 0:
                continue

            grid = all_grids[:, :, t]
            prev_grid = all_grids[:, :, t-1000]
            current_moving_events = 0

            for row in range(N):
                for col in range(N):
                    if grid[row, col] != prev_grid[row, col]:
                        current_moving_events += 1
            moving_events[t] = current_moving_events

        indexes = np.where(moving_events != 0)
        times = np.arange(0, timeSteps, step=1)

        return moving_events[indexes]/agents, times[indexes]

    def run_model(self):
        timeSteps = self.timeSteps
        N = self.N

        all_grids = np.zeros((N, N, timeSteps))
        agents_grid = self.init_grid()
        plot_schellings(agents_grid, 0, 'schellings_grid')

        for t in range(timeSteps):
            agents_grid = self.move(agents_grid)
            all_grids[:, :, t] = agents_grid

            if (t+1) % 500 == 0:
                plot_schellings(agents_grid, t + 1, 'schellings_grid')
            if (t + 1) % 10000 == 0:
                print('Time step: ' + str(t + 1))
        make_gif('graphics/img/schelling', 'schellingsmodel')

        return all_grids

    def run_model_anti_gregarious(self):
        timeSteps = self.timeSteps
        N = self.N

        all_grids = np.zeros((N, N, timeSteps))
        agents_grid = self.init_grid()
        plot_schellings(agents_grid, 0, 'schellings_grid')

        for t in range(timeSteps):
            agents_grid = self.anti_gregarious_move(agents_grid)
            all_grids[:, :, t] = agents_grid

            if (t+1) % 500 == 0:
                plot_schellings(agents_grid, t + 1, 'schellings_grid')
            if (t + 1) % 10000 == 0:
                print('Time step: ' + str(t + 1))
        make_gif('graphics/img/schelling', 'schellingsmodel')

        return all_grids

    def run_model_frustration(self):
        timeSteps = self.timeSteps
        N = self.N

        all_grids = np.zeros((N, N, timeSteps))
        agents_grid = self.init_grid()
        plot_schellings(agents_grid, 0, 'schellings_grid')

        for t in range(timeSteps):
            agents_grid = self.move_frustration(agents_grid)
            all_grids[:, :, t] = agents_grid

            if (t+1) % 500 == 0:
                plot_schellings(agents_grid, t + 1, 'schellings_grid')
            if (t + 1) % 10000 == 0:
                print('Time step: ' + str(t + 1))
        make_gif('graphics/img/schelling', 'schellingsmodel')
        return all_grids

    def run_happiness(self, all_grids):
        timeSteps = self.timeSteps
        happiness_A, happiness_B, happiness_total = self.compute_happiness(all_grids)
        moving_events, moving_times = self.compute_moving_events(all_grids)

        plot_happiness(happiness_A, happiness_B, happiness_total, moving_events, moving_times, timeSteps)

        happiness_A.tofile('csv/happiness_A.csv', sep=',', format='%10.5f')
        happiness_B.tofile('csv/happiness_B.csv', sep=',', format='%10.5f')
        happiness_total.tofile('csv/happiness_total.csv', sep=',', format='%10.5f')

    def run_happiness_anti_gregarious(self, all_grids):
        timeSteps = self.timeSteps
        happiness_A, happiness_B, happiness_total = self.compute_happiness_anti_gregarious(all_grids)
        moving_events, moving_times = self.compute_moving_events(all_grids)

        plot_happiness(happiness_A, happiness_B, happiness_total, moving_events, moving_times, timeSteps)


        happiness_A.tofile('csv/happiness_A.csv', sep=',', format='%10.5f')
        happiness_B.tofile('csv/happiness_B.csv', sep=',', format='%10.5f')
        happiness_total.tofile('csv/happiness_total.csv', sep=',', format='%10.5f')

    def run_happiness_frustration(self, all_grids):
        timeSteps = self.timeSteps
        happiness_A, happiness_B, happiness_total = self.compute_happiness_frustration(all_grids)
        moving_events, moving_times = self.compute_moving_events(all_grids)

        plot_happiness(happiness_A, happiness_B, happiness_total, moving_events, moving_times, timeSteps)

        happiness_A.tofile('csv/happiness_A.csv', sep=',', format='%10.5f')
        happiness_B.tofile('csv/happiness_B.csv', sep=',', format='%10.5f')
        happiness_total.tofile('csv/happiness_total.csv', sep=',', format='%10.5f')
