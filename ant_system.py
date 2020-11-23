"""
**** Ant System ****
authors: Barbara Boechat, Juliana Araujo, Tiago Trotta
date: 20/11/2020

"""
import math
import random


class AntSystem:
    def __init__(self, util, evaporation_rate, q, alpha, beta):
        self.util = util
        self.constraints = self.util.constraints
        self.object_count = self.util.object_count
        self.knapsack_count = self.util.knapsack_count
        self.pheromone_matrix = {}
        self.evaporation_rate = evaporation_rate
        self.obj_probability = [0] * self.object_count
        self.Q = q
        self.alpha = alpha
        self.beta = beta
        self.best_solution = {
            'best_fo': -math.inf,
            'best_solution': [] * self.object_count
        }

        for i in range(self.knapsack_count):
            self.pheromone_matrix[i] = [10 ** -16] * self.object_count

    def move(self, ant):
        trail_size = 0
        while len(ant.obj_index) < self.object_count:
            # last_object = self.util._knapsack_count
            # last_object = len(ant.trail) - 1

            self.probability_of_move(ant)

            total_probability = 0
            for i in range(0, self.object_count):
                total_probability += self.obj_probability[i]

            lucky_number = random.uniform(0, total_probability)
            selected_city = 0
            for backpack in range(0, self.knapsack_count):
                for i in range(0, self.object_count):
                    selected_city += self.obj_probability[i]
                    if selected_city >= lucky_number and self.constraints[backpack][i] != 0:
                        ant.make_visit(i)
                        trail_size += 1
                        break

    def probability_of_move(self, ant):
        pheromone = 0
        for i in range(0, self.knapsack_count):
            for j in range(0, self.object_count):
                if not ant.ant_has_visited(j) and self.constraints[i][j] != 0:
                    pheromone += pow(self.pheromone_matrix[i][j], self.alpha) * pow(1 / self.constraints[i][j],
                                                                                    self.beta)
        for i in range(0, self.knapsack_count):
            for j in range(0, self.object_count):
                if self.constraints[i][j] != 0:
                    if ant.ant_has_visited(j):
                        self.obj_probability[j] = 0
                    else:
                        n = pow(self.pheromone_matrix[i][j], self.alpha) * pow(1 / self.constraints[i][j], self.beta)
                        self.obj_probability[j] = n / pheromone

    def update_pheromone(self, ant_pop):
        for i in range(0, self.knapsack_count):
            for j in range(0, self.object_count):
                self.pheromone_matrix[i][j] *= self.evaporation_rate

        for ant in ant_pop:
            if len(ant.obj_index) > 1:
                ant_contribution = self.Q / self.util.calculate_fo(ant.trail)
            else:
                ant_contribution = 0

        for i in range(0, self.knapsack_count):
            for j in range(0, len(ant.trail) - 1):
                if ant.trail[j] == 1:  # Se o objeto está na mochila atualiza matriz
                    self.pheromone_matrix[i][j] += ant_contribution

    def update_best_solution(self, candidate_solution):
        candidate_fo = self.util.calculate_fo(candidate_solution)
        if candidate_fo > self.best_solution['best_fo']:
            self.best_solution['best_fo'] = candidate_fo
            self.best_solution['best_solution'] = candidate_solution[:]

    def get_best_solution(self):
        return self.best_solution['best_fo'], self.best_solution['best_solution']

    def clear_pheromone_matrix(self):
        for i in range(0, self.object_count):
            self.pheromone_matrix[i] = [10 ** -16] * self.object_count


class Ant:
    def __init__(self, _object_count):
        self.trail = [0] * _object_count
        self.obj_index = []
        self.object_count = _object_count

    def ant_initial_position(self):
        initial_object = random.randint(0, 1)
        if initial_object == 1:
            self.obj_index.append(0)
        self.trail[0] = initial_object

    @staticmethod
    def generate_ant_pop(object_count):
        """ Initial position of ant set randomly """
        ant_pop = []
        for _ in range(object_count):
            ant_pop.append(Ant(object_count))
        return ant_pop

    def make_visit(self, carry_object):
        self.obj_index.append(carry_object)
        self.trail[carry_object] = 1

    def forget_tour(self):
        self.trail = [0] * self.object_count
        self.obj_index = []

    def prepare_for_tour(self):
        self.forget_tour()
        self.ant_initial_position()

    def ant_has_visited(self, obj):
        if obj in self.obj_index:
            return True
        else:
            return False
