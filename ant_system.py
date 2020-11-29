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
        self.obj_probability = {}
        self.Q = q
        self.alpha = alpha
        self.beta = beta
        self.best_solution = {
            'best_fo': -math.inf,
            'best_solution': [] * self.object_count
        }

        for i in range(self.knapsack_count):
            self.pheromone_matrix[i] = [10 ** 16] * self.object_count
            self.obj_probability[i] = [0] * self.object_count

    def move(self, ant):
        """
        Forma o caminho feito pela formiga (objetos na mochila)
        baseado no método da roleta utilizando o calculo de
        probabilidade dos objetos.
        :param ant: Formiga atual
        """
        while len(ant.obj_index) < self.object_count:

            self.probability_of_move(ant)

            total_probability = 0
            for knapsack in range(0, self.knapsack_count):
                for j in range(0, self.object_count):
                    total_probability += self.obj_probability[knapsack][j]

            lucky_number = random.uniform(0, total_probability)
            selected_obj = 0
            for knapsack in range(0, self.knapsack_count):
                for j in range(0, self.object_count):
                    selected_obj += self.obj_probability[knapsack][j]
                    if selected_obj >= lucky_number:
                        ant.put_obj(j)
                        break
        for obj in ant.obj_index:
            aux_trail = ant.trail[:]
            aux_trail[obj] = 1
            if self.util.calculate_fo(aux_trail) > -1 and self.better_sol(aux_trail, ant.trail):
                ant.trail[obj] = 1
            else:
                aux_trail[obj] = 0

    def probability_of_move(self, ant):
        """
        Calcula a probabilidade de uma formiga colocar ou não um item
        na lista de candidatos a mochila
        :param ant: formiga atual
        """
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
                        self.obj_probability[i][j] = 0
                    else:
                        n = pow(self.pheromone_matrix[i][j], self.alpha) * pow(1 / self.constraints[i][j], self.beta)
                        self.obj_probability[i][j] = n / pheromone

    def update_pheromone(self, ant_pop):
        """
        Atualiza a matriz de feromonio baseado no
        caminho feito pelas formigas
        :param ant_pop: População de formigas
        """
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
        """
        :param candidate_solution: solução candidata a ser a melhor já visitada
        """
        candidate_fo = self.util.calculate_fo(candidate_solution)
        if candidate_fo > self.best_solution['best_fo']:
            self.best_solution['best_fo'] = candidate_fo
            self.best_solution['best_solution'] = candidate_solution[:]

    def get_best_solution(self):
        """
        :return: retorna melhor solução e sua FO
        """
        return self.best_solution['best_fo'], self.best_solution['best_solution']

    def clear_pheromone_matrix(self):
        """
        Reseta matriz de feromonio
        :return:
        """
        for i in range(0, self.object_count):
            self.pheromone_matrix[i] = [10 ** 16] * self.object_count

    def better_sol(self, x, y):
        if self.util.calculate_fo(x) > self.util.calculate_fo(y):
            return True
        else:
            return False


class Ant:
    def __init__(self, _object_count):
        self.trail = [0] * _object_count  # Trilha de solução(mochila) da formiga
        self.obj_index = []  # Lista de objtos candidatos a entrar na mochila
        self.object_count = _object_count  # Nº de objtos que podem ser carregados
        self.last_index = 0  # index de até onde n violou a restrição

    def ant_initial_position(self):
        """
        Coloca um objeto aleatorio na mochila da
        formiga aleatoriamente
        """
        initial_object = random.randint(0, self.object_count - 1)
        self.obj_index.append(initial_object)
        self.trail[initial_object] = 1

    @staticmethod
    def generate_ant_pop(object_count, npop):
        """
        :param object_count: número de objtos que uma formiga
        deve carregar
        :param npop: quantidade formigas na população
        :return: população de formigas
        """
        ant_pop = []
        for _ in range(npop):
            ant_pop.append(Ant(object_count))
        return ant_pop

    def put_obj(self, carry_object):
        """
        :param carry_object: objeto candidato a entrar no
        trail da formiga
        """
        self.obj_index.append(carry_object)

    def forget_tour(self):
        self.trail = [0] * self.object_count
        self.obj_index = []

    def prepare_for_tour(self):
        """
        reseta os trails das formigas e
        as coloca na posição inicial novamente
        """
        self.forget_tour()
        self.ant_initial_position()

    def ant_has_visited(self, obj):
        """
        :param obj: obj para verificar se está na mochila
        :return: se o obj está ou não na mochila
        """
        if obj in self.obj_index:
            return True
        else:
            return False
