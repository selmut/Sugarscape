import numpy as np
from Sugarscape.Utils.plots import *
from Agents.agents import Agents
from Sugarscape.LivingArea.living_area import LivingArea


class Sugarscape:
    def __init__(self, rows, cols, max_time, sugar_growth, agents):
        self.rows, self.cols = rows, cols
        self.agents = agents
        self.living_area = LivingArea(rows, cols, sugar_growth)
        self.t = 0
        self.max_time = max_time

    def init_living_area(self):
        area = self.living_area
        dist_grid = area.add_peaks()
        return dist_grid

    def init_agents(self):
        rows, cols = self.rows, self.cols
        agents = self.agents

        agent_dir = {}

        for i in range(agents):
            agent = Agents()
            agent.init_agent(rows, cols)
            agent_dir[i] = agent
        return agent_dir

    def get_current_positions(self, agent_dir):
        rows, cols = self.rows, self.cols
        agents = self.agents

        out = np.zeros((rows, cols))
        x, y = np.zeros(agents), np.zeros(agents)

        for n in range(agents):
            current_agent = agent_dir[n]
            if current_agent is None:
                continue

            out[current_agent.x, current_agent.y] += 1
            x[n] = current_agent.x
            y[n] = current_agent.y

        return out, x, y

    def update_agents(self, sugar_grid, agent_dict):
        agents = self.agents

        for n in range(agents):
            current_agent = agent_dict[n]
            if current_agent is None:
                continue

            current_agent.move(sugar_grid)
            current_agent.burn_sugar()
            if not current_agent.isAlive():
                agent_dict[n] = None

        return self.get_current_positions(agent_dict)

    def run(self):
        living_area = self.living_area
        max_time = self.max_time

        print('--- Building living area ---')
        area = self.init_living_area()
        agents_dir = self.init_agents()

        print('--- Starting simulation ---\n')
        agent_grid, agents_x, agents_y = self.get_current_positions(agents_dir)
        plot_living_area(area, agents_x, agents_y, 'graphics/img/sugarscape_all', self.t)
        scatter_agents(agents_x, agents_y, 'graphics/img/sugarscape_agents', self.t)

        for t in range(max_time):
            self.t += 1
            agents_grid, agents_x, agents_y = self.update_agents(area, agents_dir)
            area = living_area.regrow_sugar(area)
            plot_living_area(area, agents_x, agents_y, 'graphics/img/sugarscape_all', self.t)
            scatter_agents(agents_x, agents_y, 'graphics/img/sugarscape_agents', self.t)

            if (t+1) % 50 == 0:
                print('--- Time step: '+str(t+1)+' ---')

        print('\n--- Generating graphics ---')
        make_gif('graphics/img/sugarscape_all', 'sugarscape')
        make_gif('graphics/img/sugarscape_agents', 'scattered_agents')





