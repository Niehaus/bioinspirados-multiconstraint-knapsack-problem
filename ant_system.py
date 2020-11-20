"""
**** Ant System ****
authors: Barbara Boechat, Juliana Araujo, Tiago Trotta
date: 20/11/2020

"""
import random
import math


class AntSystem:
    def __init__(self, util, evaporation_rate, Q):
        self.util = util
        self.object_count = self.util.object_count
        self.pheromone_matrix = {}  # TODO: acho que não precisa ser matriz(??)
        self.evaporation_rate = evaporation_rate
        self.Q = Q
        self.best_solution = {
            'best_fo': math.inf,
            'best_solution': [] * self.object_count
        }

    def move(self):
        pass

    def probability_of_move(self, ant):
        pass

    def update_pheromone(self, ant_pop):
        for i in range(0, self.object_count):
            self.pheromone_matrix[i][i] *= self.evaporation_rate

        for ant in ant_pop:
            if len(ant.trail) > 1:
                ant_contribution = self.Q / self.util.calculate_fo(ant.trail)
            else:
                ant_contribution = 0

        for i in range(0, len(ant.trail) - 1):
            if ant.trail[i] == 1:  # Se o objeto está na mochila atualiza matriz
                self.pheromone_matrix[i][i] += ant_contribution

    def update_best_solution(self, candidate_solution):
        candidate_fo = self.util.calculate_fo(candidate_solution)
        if candidate_fo > self.best_solution['best_fo']:
            self.best_solution['best_fo'] = candidate_fo
            self.best_solution['best_solution'] = candidate_solution[:]

    @property
    def get_best_solution(self):
        return self.best_solution['best_fo'], self.best_solution['best_solution']

    def clear_pheromone_matrix(self):
        for i in range(0, self.object_count):
            self.pheromone_matrix[i] = [10 ** -16] * self.object_count


class Ant:
    def __init__(self, _object_count):
        self.trail = []
        self.object_count = _object_count

    def ant_initial_position(self):
        initial_object = random.randint(0, 1)
        self.trail.append(initial_object)

    @staticmethod
    def generate_ant_pop(object_count):
        """ Initial position of ant set randomly """
        ant_pop = []
        for _ in range(object_count):
            ant_pop.append(Ant(object_count))
        return ant_pop

    def make_visit(self, carry_object):
        self.trail.append(carry_object)

    def forget_tour(self):
        self.trail = []

    def prepare_for_tour(self):
        self.forget_tour()
        self.make_visit()

    def ant_has_visited(self, obj):
        if obj in self.trail:
            return True
        else:
            return False
