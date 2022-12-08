import numpy as np
from Sugarscape.Utils.plots import *
from Sugarscape.Utils.useful_functions import *
from Agents.agents import Agents
from Sugarscape.LivingArea.living_area import LivingArea


class Sugarscape:
    def __init__(self, rows, cols, max_time, sugar_growth, agents, rebirth, inheritance):
        self.rows, self.cols = rows, cols
        self.agents = agents
        self.living_area = LivingArea(rows, cols, sugar_growth)
        self.t = 0
        self.max_time = max_time
        self.rebirth = rebirth
        self.inheritance = inheritance

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

    def init_new_agent(self, agent_dict, key):
        rows, cols = self.rows, self.cols
        agent = Agents()
        agent.init_agent(rows, cols)
        agent_dict[key] = agent

    def init_new_agent_inherited(self, agent_dict, key, m, v, age):
        rows, cols = self.rows, self.cols
        agent = Agents()
        agent.init_agent_inheritance(rows, cols, m, v, age)
        agent_dict[key] = agent

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

    def get_current_metabolisms(self, agents_dict):
        metabolisms = {1: 0, 2: 0, 3: 0, 4: 0}

        for a_key in agents_dict.keys():
            current_agent = agents_dict[a_key]
            if current_agent is None:
                continue

            for m_key in metabolisms.keys():
                if current_agent.m == m_key:
                    metabolisms[m_key] += 1
        return metabolisms

    def get_current_visions(self, agents_dict):
        visions = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        for a_key in agents_dict.keys():
            current_agent = agents_dict[a_key]
            if current_agent is None:
                continue

            for v_key in visions.keys():
                if current_agent.v == v_key:
                    visions[v_key] += 1
        return visions

    def get_current_sugar_level(self, agents_dict):
        sugar_levels = np.arange(0, 160, step=1)
        n_agents = np.zeros(160)

        sugar = dict(zip(sugar_levels, n_agents))

        for a_key in agents_dict.keys():
            current_agent = agents_dict[a_key]
            if current_agent is None:
                continue

            for s_key in sugar.keys():
                if current_agent.wealth == s_key:
                    sugar[s_key] += 1
        return sugar

    def update_agents(self, sugar_grid, agent_dict):
        agents = self.agents

        for n in range(agents):
            current_agent = agent_dict[n]
            if current_agent is None:
                continue

            current_agent.move(sugar_grid)
            current_agent.burn_sugar()
            current_agent.grow_older()
            if not current_agent.isAlive() and not self.rebirth and not self.inheritance:
                agent_dict[n] = None
            elif not current_agent.isAlive() and self.rebirth and not self.inheritance:
                self.init_new_agent(agent_dict, n)
            elif not current_agent.isAlive() and self.rebirth and self.inheritance:
                self.init_new_agent_inherited(agent_dict, n, current_agent.m, current_agent.v, current_agent.age)

        out, x, y = self.get_current_positions(agent_dict)
        return out, x, y, agent_dict

    def run(self):
        living_area = self.living_area
        max_time = self.max_time
        gini_values = np.zeros(max_time)

        print('--- Building living area ---')
        area = self.init_living_area()
        agents_dict = self.init_agents()


        print('--- Starting simulation ---\n')
        agent_grid, agents_x, agents_y = self.get_current_positions(agents_dict)
        plot_living_area(area, agents_x, agents_y, 'graphics/img/sugarscape_all', self.t)
        scatter_agents(agents_x, agents_y, 'graphics/img/sugarscape_agents', self.t)
        meta0 = self.get_current_metabolisms(agents_dict)
        vis0 = self.get_current_visions(agents_dict)
        sugar0 = self.get_current_sugar_level(agents_dict)

        for t in range(max_time):
            self.t += 1
            agents_grid, agents_x, agents_y, agents_dict = self.update_agents(area, agents_dict)
            area = living_area.regrow_sugar(area)
            plot_living_area(area, agents_x, agents_y, 'graphics/img/sugarscape_all', self.t)
            scatter_agents(agents_x, agents_y, 'graphics/img/sugarscape_agents', self.t)

            '''sugar_val = self.get_current_sugar_level(agents_dict)
            lorentz_val = lorentz(sugar_val)
            gini_values[t] = gini(lorentz_val)'''

            if (t+1) % 50 == 0:
                print('--- Time step: '+str(t+1)+' ---')

            if (t+1) == 20:
                sugar20 = self.get_current_sugar_level(agents_dict)
            if (t+1) == 40:
                sugar40 = self.get_current_sugar_level(agents_dict)
            if (t+1) == 60:
                sugar60 = self.get_current_sugar_level(agents_dict)
            if (t+1) == 80:
                sugar80 = self.get_current_sugar_level(agents_dict)

        meta_end = self.get_current_metabolisms(agents_dict)
        vis_end = self.get_current_visions(agents_dict)

        lorentz0 = lorentz(sugar0)
        lorentz20 = lorentz(sugar20)
        lorentz40 = lorentz(sugar40)
        lorentz60 = lorentz(sugar60)
        lorentz80 = lorentz(sugar80)

        plot_vision_hist(vis0, vis_end)
        plot_meta_hist(meta0, meta_end)
        plot_sugar_hist(sugar0, sugar20, sugar40, sugar60, sugar80)
        plot_lorentz(lorentz0, lorentz20, lorentz40, lorentz60, lorentz80)
        plot_gini(gini_values, max_time)

        print('\n--- Generating graphics ---')
        make_gif('graphics/img/sugarscape_all', 'sugarscape')
        make_gif('graphics/img/sugarscape_agents', 'scattered_agents')





