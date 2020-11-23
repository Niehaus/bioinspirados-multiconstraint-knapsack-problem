from ant_system import AntSystem, Ant
from util import Util

if __name__ == '__main__':
    util = Util('instances/PB1.txt')
    util.show_entries()

    evaporation_rate = 0.05
    Q = 0.001
    iter_max = 10
    ant_system = AntSystem(util, evaporation_rate, Q, 1, 0.01)

    iteration = 0
    n_ant = 100
    ant_pop = Ant.generate_ant_pop(util.object_count, n_ant)
    while iteration < iter_max:
        for ant in ant_pop:
            ant.prepare_for_tour()
            ant_system.move(ant)
            ant_system.update_best_solution(ant.trail)
        ant_system.update_pheromone(ant_pop)
        iteration += 1
    ant_system.clear_pheromone_matrix()
    optimum, solution = ant_system.get_best_solution()

    print(f"\nNúmero de Objetos: {util.object_count} \nSolução: {optimum} -> {solution}")
