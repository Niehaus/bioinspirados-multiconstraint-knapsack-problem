from util import Util
from ant_system import AntSystem, Ant

if __name__ == '__main__':
    util = Util('instances/PB1.txt')
    util.show_entries()

    evaporation_rate = 0.5
    Q = 100
    ant_system = AntSystem(util, evaporation_rate, Q, 1, 1)

    x1 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    # x2 = [0, 1, 0]
    ant_pop = Ant.generate_ant_pop(util.object_count)

    iter_max = 10
    iteration = 0
    while iteration < iter_max:
        for ant in ant_pop:
            ant.prepare_for_tour()
            ant_system.move(ant)
            ant_system.update_best_solution(ant.trail)

        ant_system.update_pheromone(ant_pop)
        iteration += 1
    ant_system.clear_pheromone_matrix()
    optimum, solution = ant_system.get_best_solution()
    print(f"Número de Objetos: {util.object_count} \nSolução: {optimum} -> {solution}")


