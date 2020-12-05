"""
**** Ant System ****
authors: Barbara Boechat, Juliana Araujo, Tiago Trotta
date: 20/11/2020

"""

from ant_system import AntSystem, Ant
from util import Util
from sys import argv
import math_op
import io_op

if __name__ == '__main__':
    evaporation_rate = 0.05
    Q = 0.001

    instance_file, file_out, n_ant, iter_max, alfa, beta = io_op.parse_args(argv)

    util = Util(instance_file)
    util.show_entries()

    ant_system = AntSystem(util, evaporation_rate, Q, alfa, beta)

    iteration = 0
    ant_pop = Ant.generate_ant_pop(util.object_count, n_ant)
    while iteration < iter_max:
        for ant in ant_pop:
            ant.prepare_for_tour()
            ant_system.move(ant)
            ant_system.update_best_solution(ant.trail)
        ant_system.update_pheromone(ant_pop)

        # mean = math_op.calc_mean(util, ant_pop, n_ant)
        # sd = math_op.calc_std_deviation(util, ant_pop, n_ant, mean)
        # io_op.write_statistics_to_file(file_out, iteration, ant_system.get_best_solution()[0], mean, sd)

        iteration += 1
    
    ant_system.clear_pheromone_matrix()
    optimum, solution = ant_system.get_best_solution()

    print(f"\nNúmero de Objetos: {util.object_count} \nSolução: {optimum} -> {solution}")
    io_op.write_to_file([str(n_ant), str(iter_max), str(alfa), str(beta)], file_out, str(optimum))
