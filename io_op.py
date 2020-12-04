def parse_args(args):
	iter_max = 100
	n_ant = 100
	alfa = 1
	beta = 0.5
	instance_file = 'instances/PB1.txt'
	file_out = 'tests/PB1/test.txt'

	if len(args) != 1 and len(args) == 7:
		instance_file = args[1]
		file_out = args[2]
		n_ant = int(args[3])
		iter_max = int(args[4])
		alfa = float(args[5])
		beta = float(args[6])

	return instance_file, file_out, n_ant, iter_max, alfa, beta

def write_to_file(args, file_out, optimum):
	f = open(file_out, 'a')
	f.write("\t".join(args) + "\t" + optimum + "\n")
	f.close()

def write_statistics_to_file(file_out, iteration, optimum, mean, std_deviation):
	log = open(file_out, "a")
	log.write("\t".join([str(iteration), str(optimum), str(mean), str(std_deviation)]) + "\n")
	log.close()