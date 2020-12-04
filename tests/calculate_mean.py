instances = ["PB1", "PB2", "PB4", "PB5", "PB6", "PB7"]
dic = {}

for instance in instances:
	print(instance)
	fileout = open(instance + "/test_mean.txt", "w")

	for i in range(1, 3):
		file = open(instance + "/test_"+str(i)+".txt", "r")
		
		for line in file:
			line = line.rstrip()
			line = line.split("\t")

			if line[0] == "N. de Formigas":
				continue
			
			key = "\t".join(line[:4])
			value = float(line[4])

			if key not in dic:
				dic[key] = value
			else:
				dic[key] += value

		file.close()

	fileout.write("N. de Formigas\tMáx. de Iterações\tAlfa\tBeta\tMelhor Fitness\n")

	for key, value in dic.items():
		fileout.write(key + "\t" + str(value / 2) + "\n")
