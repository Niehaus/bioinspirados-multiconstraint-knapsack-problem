from util import Util
from ant_system import AntSystem, Ant

if __name__ == '__main__':
    util = Util('instances/PB1.txt')
    util.show_entries()

    evaporation_rate = 0.5
    Q = 100
    ant_system = AntSystem(util, evaporation_rate, Q)

    x1 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    # x2 = [0, 1, 0]
    ant_pop = Ant.generate_ant_pop(util.object_count)
    # print(ant_pop)
    # for ant in ant_pop:
    #     print(ant.trail)

