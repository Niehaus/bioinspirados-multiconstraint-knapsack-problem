from math import sqrt

# Calcula a média de todos os fitnesses
def calc_mean(util, ant_population, n_ant):
	mean = 0
	for ant in ant_population:
		mean += util.calculate_fo(ant.trail)
	return mean / n_ant

# Calcula o desvio padrão de todos os fitnesses
def calc_std_deviation(util, ant_population, n_ant, mean):
	sd = 0
	for ant in ant_population:
		sd += (util.calculate_fo(ant.trail) - mean) ** 2
	sd /= n_ant
	return sqrt(sd)